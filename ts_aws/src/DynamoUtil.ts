
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { 
    PutCommand, 
    ScanCommand,
    DynamoDBDocumentClient } from "@aws-sdk/lib-dynamodb";

import { AppLogger } from "./AppLogger";

/**
 * Utility class to access an AWS Dynamo DB service.
 * See https://www.npmjs.com/package/@aws-sdk/client-dynamodb
 * See https://www.npmjs.com/package/@aws-sdk/lib-dynamodb
 * See https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_dynamodb_code_examples.html#basics
 * See https://www.webdevtutor.net/blog/typescript-aws-dynamodb-client
 * 
 * This is a minimal but working TypsScript class.
 * Chris Joakim, 2025
 */

export class DynamoUtil {
    private client: DynamoDBClient;
    private doc_client: DynamoDBDocumentClient;
    private region: string;
    private logger : AppLogger;

    constructor() {
        this.logger = AppLogger.buildDefaultLogger('DynamoUtil');
        this.region = process.env.AWS_DEFAULT_REGION;
        this.logger.warn(`region: ${this.region}`);
        this.client = new DynamoDBClient({region: this.region});
        this.doc_client = DynamoDBDocumentClient.from(this.client);
    }

    /**
     * Load the given Dynamo DB table name with the given document -
     * The partition key 'pk' is assumed to be populated appropriately.
     */
    async put_document(table_name: string, document: Object): Promise<Object> {
        try {
            console.log(document);
            const command = new PutCommand({
                TableName: table_name,
                Item: document
            });
            return this.doc_client.send(command);
        }
        catch (error) {
            console.log(error);
            return error;
        }
    }

    async scan_documents(table_name: string, projection_attr: string = "pk"): Promise<Object> {
        try {
            const command = new ScanCommand({
                TableName: table_name,
                ProjectionExpression: projection_attr
              });
            return this.doc_client.send(command);
        }
        catch (error) {
            console.log(error);
            return error;
        }
    }

    async count_documents(table_name: string): Promise<Object> {
        try {
            const command = new ScanCommand({
                TableName: table_name,
                Select: "COUNT"
              });
            return this.doc_client.send(command);
        }
        catch (error) {
            console.log(error);
            return error;
        }
    }

}
