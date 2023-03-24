import boto3

def lambda_handler(event, context):
    #Get IP addresses of EC2 instances
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('akshay007')
    bucket.object_versions.all().delete()
    
    
    
#function name : akshay007
