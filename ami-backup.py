import collections
import datetime
import sys
import boto3
ec = boto3.client('ec2')
create_time = datetime.datetime.now()
create_fmt = create_time.strftime('%Y-%m-%d')
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
        AMIid = ec.create_image(InstanceId=instance["InstanceId"], Name=instance["InstanceId"] + " - from  " + create_fmt, Description=instance["InstanceId"] + " created AMI of instance  from " + create_fmt, NoReboot=True, DryRun=False)
        print(AMIid)
        ec.create_tags(
            Resources=[
                AMIid['ImageId'],
            ],
            Tags=[
                {'Key': 'Name', 'Value': instance["InstanceId"]},
                {'Key': 'created-at', 'Value': create_fmt },
            ]
        )
print("Ami created")
