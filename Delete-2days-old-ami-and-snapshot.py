import collections
import datetime
import sys
import boto3
s = boto3.Session(profile_name='xxxxxxxxxxx')
ec = s.client('ec2', region_name='xxxxxxxxxxxxxx')
d = datetime.today() - timedelta(days=days_to_subtract)

def delete_ami(ami_id):
    ec.deregister_image(ImageId=image["ImageId"])
    return "Deleted AMI"

def deleted_snapshot(Snapshot_id):
    ec.delete_snapshot(SnapshotId=id)
    return "Deleted Snapshot"


images = ec.describe_images(
        Filters=[
            {
                'Name':'description',
                'Values': ['* ' +'2020-05-11']
            },
            {
                'Name': 'tag:backup',
                'Values': ['dailyami']
            }
        ]
)["Images"]
count = 0
im = []
for image in images:
    print(image["ImageId"])
    print(image["BlockDeviceMappings"])
    im.append(image["ImageId"])
    delete_ami(image["ImageId"])
    sn = []
    for i in range(0,len(image["BlockDeviceMappings"])):
        try:
            sn.append(image["BlockDeviceMappings"][i]["Ebs"]["SnapshotId"])
            id = image["BlockDeviceMappings"][i]["Ebs"]["SnapshotId"]
            deleted_snapshot(id)
        except:
            pass
    print(sn)
print(im)
print(len(im))
