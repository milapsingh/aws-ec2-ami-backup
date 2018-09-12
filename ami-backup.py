import collections
import datetime
import sys
import boto3
ec = boto3.client('ec2')
create_time = datetime.datetime.now()
create_fmt = create_time.strftime('%Y-%m-%d %H:%M:%S')
response=ec.describe_instances(
    Filters=[
        {
            'Name':'tag:ami',
            'Values': ['backup']
        }
    ]
)
print(response)
instancelist = []
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        instancelist.append(instance["InstanceId"])
        print(instance["InstanceId"])
        AMIid = ec.create_image(InstanceId=instance["InstanceId"], Name=instance["InstanceId"] + " - from " + create_fmt, Description=instance["InstanceId"] + " created AMI of instance  from " + create_fmt, NoReboot=True, DryRun=False)
print(instancelist)
