
import { AppLogger } from "./AppLogger";
import { DynamoUtil } from "./DynamoUtil.js";
import { FileUtil } from "./FileUtil.js";
import { S3Util } from "./S3Util.js";

let func = process.argv[2];
let logger = AppLogger.buildDefaultLogger('Index');

switch (func) {
    case "dynamo_load_openflights_airports":
        dynamo_load_openflights_airports();
        break;
    case "dynamo_scan_openflights":
        dynamo_scan_openflights();
        break;
    case "s3_list_buckets":
        s3_list_buckets();
        break;
    default:
        displayCommandLineExamples();
        break;
}

async function dynamo_load_openflights_airports() {
    try {
        let file_util = new FileUtil();
        let dynamo = new DynamoUtil();
        let table_name = "openflights";
        let infile = '../data/openflights/json/airports.json'
        let json_lines: Array<string> = file_util.readTextFileAsLinesSync(infile);
        let line_num = 0;
        let iata_codes = {};
        let airports = Array<Object>();

        // First read the json-doc-per-line airport data, and parse them
        // into an array of objects to be loaded into Dynamo DB, below.
        json_lines.forEach((json_line) => {
            try {
                line_num++;
                let trimmed: string = json_line.trim();
                if (trimmed.length > 10) {
                    let doc = JSON.parse(json_line)
                    let iata = doc['IATA'];
                    if (iata in Object.keys(iata_codes)) {
                        logger.warn(`duplicate iata_code ${iata} on line ${line_num}`);
                    }
                    else {
                        if (iata != '\\N') {
                            iata_codes[iata] = line_num;
                            doc['pk'] = iata;
                            airports.push(doc)

                        }
                        else {
                            logger.warn(`skipping iata_code ${iata} on line ${line_num}`);
                        }
                    }
                }
            }
            catch (error) {
                logger.error('error on line number: ' + line_num);
                this.logger.errorException(error);
                return null;
            }
        });

        file_util.writeTextFileSync(
            "tmp/iata_codes.json", JSON.stringify(iata_codes, null, 2));
        file_util.writeTextFileSync(
            "tmp/airport_documents.json", JSON.stringify(airports, null, 2));

        // Load Dynamo DB with the parsed and augmented airport documents.
        let docs_loaded : number = 0;
        for (let i = 0; i < airports.length; i++) {
            if (i < 999999) {
                let doc = airports[i];
                await sleep(500);
                logger.warn(`--- loading ${i+1} ${doc['pk']}`);
                const response = await dynamo.put_document(table_name, doc);
                console.log(response);
                docs_loaded = docs_loaded + 1;
            }
        }
        logger.warn(`documents loaded: ${docs_loaded}`)
    }
    catch (error) {
        console.log(error);
    }
}

async function dynamo_scan_openflights() {
    try {
        let file_util = new FileUtil();
        let dynamo = new DynamoUtil();
        let table_name = "openflights";

        // Scan documents
        let results = await dynamo.scan_documents(table_name, "pk");
        console.log(results);
        file_util.writeTextFileSync(
            "tmp/scan.json", JSON.stringify(results, null, 2));

        // Count documents
        results = await dynamo.count_documents(table_name);
        console.log(results);
        file_util.writeTextFileSync(
            "tmp/count.json", JSON.stringify(results, null, 2));

        // Get CLT airport
        results = await dynamo.get_document(table_name, "pk", "CLT");
        console.log(results);
        file_util.writeTextFileSync(
            "tmp/get_clt.json", JSON.stringify(results, null, 2));
    }
    catch (error) {
        console.log(error);
    }
}

async function s3_list_buckets() {
    try {
        let util = new S3Util();
        let results = await util.list_buckets();
        console.log('Raw Results:');

        console.log(results);
        let buckets = results['Buckets'];

        console.log('Bucket Names:');
        buckets.forEach((b: object) => {
            console.log(b['Name']);
        });
    }
    catch (error) {
        console.log(error);
    }
}

async function sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function displayCommandLineExamples() {
    console.log('');
    console.log("node ./dist/index.js dynamo_load_openflights_airports");
    console.log("node ./dist/index.js dynamo_scan_openflights");
    console.log("node ./dist/index.js s3_list_buckets");
    console.log('');
}
