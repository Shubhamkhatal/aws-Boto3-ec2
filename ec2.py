import boto3
ec2 = boto3.client('ec2')
# Create Ec2 instance

def create_ec2_instance():
    try:
        print("Create a EC2 instance.......\n")
        ec2.run_instances(
            ImageId = 'ami-052efd3df9dad4825',
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t2.micro",
            KeyName = "ansible_key",
            SubnetId = "subnet-0184d693ae4fd4273"
        )
        print("instance created successfully\n")
    except Exception as e:
        print(e)


# Describe Ec2 Instance

def describe_ec2_instance():
    try:
        print("instance id of a EC2 instance......\n")
        instance_id = ec2.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
        return instance_id
    except Exception as e:
        print(e)

#Reboot Ec2 Instance
def reboot_ec2_instance():
    try:
        id = describe_ec2_instance()
        print("reboot a EC2 instance.....\n")
        ec2.reboot_instances(InstanceIds=[id])
        print("instance rebooted successfully\n")
    except Exception as e:
        print(e)

# Stop Ec2 Instance

def stop_ec2_instance():
    try:
        id = describe_ec2_instance()
        print("stopping a EC2 instance.....\n")
        ec2.stop_instances(InstanceIds=[id])
        print("instance stopped successfully\n")
    except Exception as e:
        print(e)


# Start Ec2 Instance
def start_ec2_instance():
    try:
        id = describe_ec2_instance()
        print("starting a EC2 instance.....\n")
        ec2.start_instances(InstanceIds=[id])
        print("instance started successfully\n")
        return
    except Exception as e:
        print(e)


# Terminate Ec2 Instance

def terminate_ec2_instance():
    try:
        id = describe_ec2_instance()
        print("termnating a EC2 instance.....\n")
        ec2.terminate_instances(InstanceIds=[id])
        print("instance termnated successfully\n")
    except Exception as e:
        print(e)


create_ec2_instance()
describe_ec2_instance()
start_ec2_instance()
reboot_ec2_instance()
stop_ec2_instance()
terminate_ec2_instance()