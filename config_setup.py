# from schema import Schema, And, Use, Optional, SchemaError
# import yaml
#
# schema = Schema(
#         {
#             'SAST':
#                 'Sonarqube':
#                    'repo'
#                    'SONAR_HOST_URL':,
#                    'SONAR_PROJECT_KEY':,
#
#             'DAST':,
#                 'zap':,
#                     'repo': ,
#                     'typeofscan': ,
#                     'target': ,
#                     'format': ,
#                     'options': ,
#
#             'Tekton-build-and-push':,
#                 'docker'
#                     'repo': ,
#                     'docker_username': ,
#                     'docker_password': ,
#                     'image_name':,
#                     'revision': ,
#                     'url': ,
#
#         }
#     )
#
# with open('Config.yaml') as f:
#    data = yaml.load(f)
#    try:
#        schema.validate(data)
#    except SchemaError as e:
#        print(e)

#
#
# import yaml
# from yaml.loader import SafeLoader
# import cerberus
#
# def load_doc():
#     data = ''
#     with open('./Config.yaml') as f:
#         data = yaml.load(f, Loader=SafeLoader)
#         print(data)
#     return data
#
#
# ## Now, validating the yaml file:
#
# schema = eval(open('./schema.py').read())
# v = cerberus.Validator(schema)
# doc = load_doc()
# print(v.validate(doc, schema))



## Schema Validator resource link:[ https://stackoverflow.com/questions/3262569/validating-a-yaml-document-in-python ] 


import yaml
import cerberus

def load_doc():
    with open('./Config.yaml', 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exception:
            raise exception

## Now, validating the yaml file is straightforward:

schema = eval(open('./schema.py', 'r').read())
v = cerberus.Validator(schema)
doc = load_doc()
print(v.validate(doc, schema))
print(v.errors)
