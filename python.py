import boto3

client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-0614680123427b75e',
    InstanceType='t3.micro',
    KeyName='clientkey',
    SubnetId='subnet-02cb7f7c0b6e98d6f',
    MaxCount=1,
    MinCount=1
)