import yaml

def remove_func_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)




# another option with issue
# (https://stackoverflow.com/questions/52240554/how-to-parse-yaml-using-pyyaml-if-there-are-within-the-yaml)
# For !GetAtt
class GetAtt(object):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "~GetAtt %s" % self.data

def create_getatt(loader, node):
    value = loader.construct_sequence(node)
    return GetAtt(value)


# For !Join
class Join(object):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "~Join %s" % self.data

def create_join(loader, node):
    value = loader.construct_scalar(node)
    return Join(value)
