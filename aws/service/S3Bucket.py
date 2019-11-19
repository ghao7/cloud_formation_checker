class S3Bucket:
    def __init__(self):
        self.type = 'AWS::S3::Bucket'
        self.propertyDict = {
            'AccessControl' : self.AccessControl(),
            'BucketName' : self.BucketName(),
            'WebsiteConfiguration' : self.WebsiteConfiguration()
        }


    class AccessControl:
        required = True
        type = 'String'

    class BucketName:
        required = False
        type = 'String'

    class WebsiteConfiguration:
        required = False
        type = 'WebsiteConfiguration'

    # class BucketName:
    #     required = False
    #     type = 'String'
    #     namingConvension =
