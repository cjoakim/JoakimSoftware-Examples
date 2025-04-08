
import { 
    S3Client, 
    GetObjectCommand,
    GetObjectCommandInput,
    ListBucketsCommand } from "@aws-sdk/client-s3";

import { AppLogger } from "./AppLogger";

/**
 * Utility class to access an AWS S3 service.
 * See https://www.npmjs.com/package/@aws-sdk/client-s3
 * 
 * This is a minimal but working TypsScript class.
 * Chris Joakim, 2025
 */

export class S3Util {
    private client: S3Client;
    private region: string;
    private logger : AppLogger;

    constructor() {
        this.logger = AppLogger.buildDefaultLogger('S3Util');
        this.region = process.env.AWS_DEFAULT_REGION;
        this.logger.warn(`region: ${this.region}`);
        this.client = new S3Client({region: this.region});
    }

    async list_buckets(): Promise<Object> {
        try {
            const params = {};
            const command = new ListBucketsCommand(params);
            return await this.client.send(command);
        }
        catch (error) {
            this.logger.errorException(error);
            return null;
        }
    }
}
