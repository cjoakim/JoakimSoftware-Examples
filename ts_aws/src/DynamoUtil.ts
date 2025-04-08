
import { AppLogger } from "./AppLogger";

/**
 * Utility class to access an AWS Dynamo DB service.
 * See https://www.npmjs.com/package/@aws-sdk/client-dynamodb
 * See https://www.webdevtutor.net/blog/typescript-aws-dynamodb-client
 * 
 * This is a minimal but working TypsScript class.
 * Chris Joakim, 2025
 */

export class DynamoUtil {
    
    private logger : AppLogger;
    
    constructor() {
        this.logger = AppLogger.buildDefaultLogger('DynamoUtil');
    }


}
