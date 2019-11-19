import CloudFormationDebugger.aws.service.S3Bucket as S3Bucket
import CloudFormationDebugger.aws.service.DynamoDB as DynamoDB

class AWS:
    serviceDict = {
        'AWS::S3::Bucket' : S3Bucket.S3Bucket(),
        'AWS::DynamoDB::Table' : DynamoDB.DynamoDB()
    }
