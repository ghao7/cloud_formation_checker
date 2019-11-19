import yaml
import CloudFormationDebugger.util.Preprocessor as Preprocessor
import sys
import CloudFormationDebugger.aws.AWS as AWS


class CloudFormationChecker:
    def __init__(self, content):
        self.errorFound = []
        self.content = content
        self.yamlObject = self.checkYAMLFormat()

     # Check 1: Check whether the template file is in correct YAML format.
    def checkYAMLFormat(self):
        yaml.add_multi_constructor('', Preprocessor.remove_func_constructor, Loader=yaml.SafeLoader)
        try:
            dataMap = yaml.safe_load(self.content)
            # print(dataMap)
            return dataMap
        except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
            error = dict()
            error['type'] = 'Not Correct YMAL Format'
            print(e.problem_mark.line)
            error['index'] = e.problem_mark.index
            error['line'] = e.problem_mark.line
            error['column'] = e.problem_mark.column
            self.errorFound.append(error)

    # Check 2: Check whether the name of the properties declared under certain AWS resources are mentioned in the official document.
    def checkPropertyName(self):
        resources = self.yamlObject.get('Resources')
        for resourceName in resources.keys():
            print('\nCurrently checking resource: ' + resourceName)
            serviceType = resources.get(resourceName).get('Type', 'Type Undeclared')
            if serviceType not in AWS.AWS.serviceDict:
                print('''
    -------------------------------------------------------------------------
    ------ [Error NO.2] Unknown AWS service type [{}] ------
    -------------------------------------------------------------------------
                      '''.format(serviceType))
                return
            serviceObject = AWS.AWS.serviceDict.get(serviceType)
            for propertyName in resources.get(resourceName).get('Properties'):
                print('\n\tCurrently checking property: ' + propertyName)
                if propertyName not in serviceObject.propertyDict:
                    print('''
    -------------------------------------------------------------------------
    ------ [Error NO.3] Unknown property [{}] under [{}] ------
    -------------------------------------------------------------------------
                      '''.format(propertyName, serviceType))
                    return

    # Check 3: Check whether there is certain missing property that is required to create the resources.
    def checkMissingProperty(self):
        resources = self.yamlObject.get('Resources')
        for resourceName in resources.keys():
            print('\nCurrently checking resource: ' + resourceName)
            serviceType = resources.get(resourceName).get('Type')
            serviceObject = AWS.AWS.serviceDict.get(serviceType)
            # collect required properties appeared under current resource
            currRequiredPropertySet = set()
            for propertyName in resources.get(resourceName).get('Properties').keys():
                if serviceObject.propertyDict.get(propertyName).required:
                    currRequiredPropertySet.add(propertyName)
            # collect actual set of required properties needed
            resourceRequiredPropertySet = set()
            for propertyName in serviceObject.propertyDict.keys():
                if serviceObject.propertyDict.get(propertyName).required:
                    resourceRequiredPropertySet.add(propertyName)
            if len(currRequiredPropertySet) != len(resourceRequiredPropertySet):
                print('''
    -------------------------------------------------------------------------
    ------ [Error NO.4] Missing required property [{}] when creating resource [{}] ------
    -------------------------------------------------------------------------
                      '''.format(', '.join(resourceRequiredPropertySet.difference(currRequiredPropertySet)),
                                 serviceType))

    # Check 4: Check whether the value of each property is valid.
    def checkPropertyValue(self):
        resources = self.yamlObject.get('Resources')
        for resourceName in resources.keys():
            print('\nCurrently checking resource: ' + resourceName)
