# aws-ec2-ami-backup

We often need to create backup of an ec2 instance. So we go to aws console and select Action -> Image -> create image
By doing this we make backup of servers. 

Now what happens if we want daily backup of a server then it will be boring to do it via aws console. So we create python script for creating backup.
First you need to insall boto3 

> <h2> pip3 install boto3 </h2> After that create a file backyp.py

We use boto3 to talk to aws apis which is very useful to get information about anything. 
> <h4> ec = boto3.client('ec2')</h4>
here we are using only ec2 
Then we use some filter to describe the instance( means get the information about server)</br>
```
response=ec.describe_instances(
    Filters=[
        {
            'Name':'tag:ami',
            'Values': ['backup']
        }
    ]
)
```
This code fetch that servers only which has tag 
> ami - backup

```
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        instancelist.append(instance["InstanceId"])
        print(instance["InstanceId"])
        AMIid = ec.create_image(InstanceId=instance["InstanceId"], Name=instance["InstanceId"] + " - from " + create_fmt, Description=instance["InstanceId"] + " created AMI of instance  from " + create_fmt, NoReboot=True, DryRun=False)
```
