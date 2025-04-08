
// https://www.webdevtutor.net/blog/typescript-aws-dynamodb-client

export class DynamoUtil {
    
    constructor(
        public verbose: boolean = false) {
        // no statements required
    }

    greet(name: string): string {
        return `hello ${name}!`;
    }

}
