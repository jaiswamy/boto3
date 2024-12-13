import boto3

client = boto3.client('lambda')
response = client.create_function(
    FunctionName='Lambda',
    Runtime='python3.9',
    Role='arn:aws:iam::024848455634:role/Lambda_access',
    Handler='Lambda.py',
    Code={
        'S3Bucket': 'myawssugar234',
        'S3Key': 'Lambda.zip',
    },
    Description='string',
    Timeout=15
)