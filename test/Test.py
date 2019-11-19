import CloudFormationChecker as Checker

# ========== Check 1: YAML format ==========
# correct
checker1 = Checker.CloudFormationChecker('./correct/S3Bucket.yaml')

# wrong
checker1_1 = Checker.CloudFormationChecker('./wrong/1_WrongYAMLFormat.yaml')


# ========== Check 2: name of properties ==========
# correct
checker2 = Checker.CloudFormationChecker('./correct/S3Bucket.yaml')
checker2.checkPropertyName()

# wrong
checker2_1 = Checker.CloudFormationChecker('./wrong/2_1_UnknownServiceType.yaml')
checker2_1.checkPropertyName()

checker2_2 = Checker.CloudFormationChecker('./wrong/2_2_UnknownServiceProperty.yaml')
checker2_2.checkPropertyName()


# ========== Check 3: missing required property ==========
# correct
checker3 = Checker.CloudFormationChecker('./correct/DynamoDB.yaml')
checker3.checkPropertyName()
checker3.checkMissingProperty()

print('===================')


# wrong
checker3_1 = Checker.CloudFormationChecker('./wrong/3_1_MissingRequiredProperty.yaml')
checker3_1.checkPropertyName()
checker3_1.checkMissingProperty()

