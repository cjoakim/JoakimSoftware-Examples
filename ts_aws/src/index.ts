
import { Greeter } from "./Greeter.js";
import { S3Util } from "./S3Util.js";

let func = process.argv[2];

switch (func) {
    case "hello":
        hello();
        break;
    case "s3_list_buckets":
        s3_list_buckets();
        break;
    default:
        displayCommandLineExamples();
        break;
}

function hello() {
    let g = new Greeter();
    console.log(g.greet(process.argv[3]));
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
    } catch (error) {
        console.log(error);
    }
}

function displayCommandLineExamples() {
    console.log('');
    console.log("node ./dist/index.js hello Miles");
    console.log("node ./dist/index.js s3_list_buckets");
    console.log('');
}
