
import { 
    S3Client, 
    GetObjectCommand,
    GetObjectCommandInput,
    ListBucketsCommand } from "@aws-sdk/client-s3";

/**
 * Utility class to access an AWS S3 service.
 * 
 * This is a minimal but working TypsScript class.
 * 
 * Chris Joakim, 2025
 */

export class S3Util {
    private client: S3Client;
    private region: string;

    constructor() {
        this.region = process.env.AWS_DEFAULT_REGION;
        console.log('S3Util.region: %s', this.region);
        this.client = new S3Client({region: this.region});
    }

    async list_buckets(): Promise<Object> {
        try {
            const params = {};
            const command = new ListBucketsCommand(params);
            return await this.client.send(command);
        } catch (error) {
            console.log(error);
            return null;
        }
    }
}
