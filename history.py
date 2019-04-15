import boto3
client = boto3.client('workspaces')
response['Workspaces']
response = client.describe_workspaces()
response
workspace_list = response['Workspaces']
len(workspace_list)
response = client.describe_workspaces(Limit=50)
response['NextToken']
response = client.describe_workspaces()
response



len(workspace_list)
workspaceid_list = [ ]
for ws in workspace_list:
    workspaceid_list.append(workspaceid['WorkspaceId'])
for ws in workspace_list:
    workspaceid_list.append(ws['WorkspaceId'])
workspaceid_list
len(workspaceid_list)
response['NextToken']
NextToken = response['NextToken']
response['Workspaces']['NextToken']
client.describe_workspaces(['NextToken'])
response['Workspaces']
response['Workspaces']['NextToken']
response['NextToken']
NextToken
client.describe_workspaces(['NextToken'])
client.describe_workspaces('NextToken')
client.describe_workspaces(['WorkspaceId'])
client.describe_workspaces(WorkspaceId=['wsid'])
client.describe_workspaces(WorkspaceId=['WorkspaceIds'])
client.describe_workspaces(WorkspaceIds=['wsids'])
client.describe_workspaces(WorkspaceIds=['WorkspaceId'])
client.describe_workspaces(WorkspaceIds='WorkspaceId')
client.describe_workspaces(UserName='un')
client.describe_workspaces(NextToken=NextToken)
workspace_list2 = client.describe_workspaces(NextToken=NextToken)
workspace_list2['WorkspaceId']
response = client.describe_workspaces(NextToken=NextToken)
workspace_list2 = response['Workspaces']
workspace_list2
workspace_list2['WorkspaceId']
workspaceid_list2 = [ ]
for ws in workspace_list1:
    workspaceid_list2.append(ws['WorkspaceId'])
for ws in workspace_list2:
    workspaceid_list2.append(ws['WorkspaceId'])
workspace_list2
workspace_list
workspace_list
workspace_list2
history

workspaceid_list = [ ]
response = client.describe_workspaces()
response
response['Workspaces']
workspace_list = response['Workspaces']
workspace_list
workspace_list['WorkspaceId']
workspaceid_list = [ ]
for ws in workspace_list:
    workspace_list = response['Workspaces']
    workspaceid_list.append(ws['WorkspaceId'])
len(workspaceid_list)
workspaceid_list
response = client.describe_workspaces(NextToken=NextToken)
for ws in workspace_list:
    workspace_list = response['Workspaces']
    workspaceid_list.append(ws['WorkspaceId'])
workspaceid_list
len(workspaceid_list)
workspaceid_list = [ ]
response = client.describe_workspaces()
for ws in workspace_list:
    workspace_list = response['Workspaces']
    workspaceid_list.append(ws['WorkspaceId'])
    response = client.describe_workspaces(NextToken=NextToken)
len(workspaceid_list)

workspaceid_list = [ ]
response = client.describe_workspaces()
workspace_list = response['Workspaces']
NextToken = response['NextToken']
workspaceid_list
workspaceid_list = [ ]
response = client.describe_workspaces()
workspace_list = response['Workspaces']
NextToken = response['NextToken']
for ws in workspace_list:
    workspaceid_list.append(ws['WorkspaceId'])
len(workspaceid_list)
workspaceid_list
while NextToken:
    response = client.describe_workspaces(NextToken=NextToken)
    workspace_list = response['Workspaces']
    NextToken = response['NextToken']
    for ws in workspace_list:
        workspaceid_list.append(ws['WorkspaceId'])
len(workspaceid_list)
seen = set()
unique = []
for x in workspaceid_list:
    if x not in seen:
        unique.append(x)
        seen.add(x)
unique
len(unique)
len(seen)
workspaceid_list = [ ]
response = client.describe_workspaces()
workspace_list = response['Workspaces']
NextToken = response['NextToken']
for ws in workspace_list:
    workspaceid_list.append(ws['WorkspaceId'])
len(workspaceid_list)
while NextToken:
    response = client.describe_workspaces(NextToken=NextToken)
    workspace_list = response['Workspaces']
    for ws in workspace_list:
        workspaceid_list.append(ws['WorkspaceId'])
    NextToken = response['NextToken']
len(workspaceid_list)
