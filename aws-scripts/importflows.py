from resources import awsutils
import nipyapi

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

s3_bucket = 'big-data-dependencies'
s3_prefix = 'backups/SB-AW/flows/'

s3 = boto3.client('s3')

conf = hc.hostconfig(port='8443',username='username',password='password')

cred_loc = "/tmp/creds.json"
with open(cred_loc,"r") as file:
    credentials = file.read()


cred_json = json.loads(credentials)

conf.set_password(cred_json['password'])
conf.set_username(cred_json['username'])


amb_client = amb.ambariutils(conf)
host = amb_client.get_component_hostname('AW', 'NIFI_REGISTRY', 'NIFI_REGISTRY_MASTER')



#Configure NiPyAPI
nipyapi.config.registry_config.host = 'http://'+ host +':61080/nifi-registry-api'

reg_bucket = nipyapi.versioning.create_registry_bucket('DEVELOPMENT')


for obj in s3.list_objects_v2(Bucket=s3_bucket, Prefix=s3_prefix)['Contents']:
    if obj['Key']!=s3_prefix:
        filename = remove_prefix(obj['Key'],s3_prefix) + ".json"
        import_file= open(filename, "w+")
        contents = s3.get_object(Bucket=s3_bucket, Key=obj['Key'])
        import_file.write(contents)
        import_file.close()
        nipyapi.versioning.import_flow_version()


        #do stuff
contents = nipyapi.versioning.export_flow_version(flow.bucket_identifier, flow.identifier, mode='json')
export_file.write(contents)
export_file.close()
s3_client.upload_file(filename, s3_bucket, s3_path+filename)
