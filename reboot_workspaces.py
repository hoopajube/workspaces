import boto3

client = boto3.client('workspaces')
workspaceid_list = [ ]
#list of workspaces where the workspace is a dictionary
response = client.describe_workspaces()
workspace_list = response['Workspaces']
NextToken = response['NextToken']
for ws in workspace_list:
    workspaceid_list.append(ws['WorkspaceId'])

response = client.reboot_workspaces(RebootWorkspaceRequests=[{'WorkspaceId': workspaceid},])
