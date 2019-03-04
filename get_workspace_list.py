import boto3

workspaceid_list = [ ]
workspaceid = response['Workspaces']

for id in workspaceid:
    workspaceid_list.append(workspaceid[0]['WorkspaceId'])
    print(workspaceid_list)
