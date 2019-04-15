#Alex's super shady workspaces script.
#Note that you will still get KeyError: 'NextToken' at the end of code
#because I have not built logic that will be when it doesn't get a token response
import boto3
import time

client = boto3.client('workspaces')
workspaceid_list = [ ]
#list of workspaces where the workspace is a dictionary
response = client.describe_workspaces()
workspace_list = response['Workspaces']
#so the actual hard limitation of 25 at a time works on a token exchange. you request a
#response and it gives you a max list of 25 of parameters specified...INCLUDING a generated
#token that you need to specify as a parameter to get the next 25.
NextToken = response['NextToken']
#right now...this loop will grab all the workspace ids and append them into one big ass
#list...but logic is currently rebooting them one at a time. Will work more on refactoring
for ws in workspace_list:
    workspaceid_list.append(ws['WorkspaceId'])

while NextToken:
    response = client.describe_workspaces(NextToken=NextToken)
    workspace_list = response['Workspaces']
    for ws in workspace_list:
        workspaceid_list.append(ws['WorkspaceId'])
        workspaceid = ws['WorkspaceId']
        client.reboot_workspaces(RebootWorkspaceRequests=[{'WorkspaceId': workspaceid},])
    NextToken = response['NextToken']

#    time.sleep(2)
#    NextToken = response['NextToken']
#note to self...print() indented would print after every loop
#print(workspaceid_list)
