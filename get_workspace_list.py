import boto3

workspaceid_list = [ ]
workspaceid = response['Workspaces']

for id in workspaceid:
    workspaceid_list.append(workspaceid[0]['WorkspaceId'])
    print(workspaceid_list)

counter = 0
for c in client.describe_workspaces():
    counter = counter + 1
    print(counter)
