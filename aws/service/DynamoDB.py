class DynamoDB:
    def __init__(self):
        self.type = 'AWS::DynamoDB::Table'
        self.propertyDict = {
            'AttributeDefinitions' : self.AttributeDefinitions(),
            'KeySchema' : self.KeySchema(),
            'ProvisionedThroughput' : self.ProvisionedThroughput()
        }


    class AttributeDefinitions:
        required = False
        type = 'List of AttributeDefinition'

    class KeySchema:
        required = True
        type = 'List of KeySchema'

    class ProvisionedThroughput:
        required = False
        type = 'ProvisionedThroughput'
