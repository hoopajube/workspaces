import boto3

client = boto3.client('workspaces')

counter = 0
for c in client.describe_workspaces():
    counter = counter + 1
    print(counter)
