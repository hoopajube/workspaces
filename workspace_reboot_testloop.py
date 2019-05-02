#Alex's super shady workspaces script.
#Note that you will still get KeyError: 'NextToken' at the end of code
#because I have not built logic that will be when it doesn't get a token response
import boto3
import time

def get_workspaces_from_account(account):

client = boto3.client('workspaces')
workspace_list = [ ]
#list of workspaces where the workspace is a dictionary
response = client.describe_workspaces()
workspace_list.append(response['Workspaces'])
#so the actual hard limitation of 25 at a time works on a token exchange. you request a
#response and it gives you a max list of 25 of parameters specified...INCLUDING a generated
#token that you need to specify as a parameter to get the next 25.
NextToken = response['NextToken']
#right now...this loop will grab all the workspace ids and append them into one big ass
#list...but logic is currently rebooting them one at a time. Will work more on refactoring

while NextToken:
    response = client.describe_workspaces(NextToken=NextToken)
    workspace_list.append(response['Workspaces'])
    #for ws in workspace_list:
    #    workspaceid_list.append(ws['WorkspaceId'])
    #    workspaceid = ws['WorkspaceId']
    #    client.reboot_workspaces(RebootWorkspaceRequests=[{'WorkspaceId': workspaceid},{'WorkspaceId': workspaceid},{'WorkspaceId': workspaceid},{'WorkspaceId': workspaceid},)]
    if 'NextToken' in keys(response):
        NextToken = response['NextToken']
    else
        NextToken = ''


def workspace2json(workspace_list, key):
    json_list = []
    for ws in workspace_list:
        json_list.append({key : ws[key]})
    print(json_list)



def reboot_workspaces(workspace_list):

    workspaceid_list = workspace2json(workspace_list, 'WorkspaceId')
    for idx in range(0,length(workspace_list),25)
        client_api_call(RebootWorkspaceRequests=workspaceid_list[idx:idx+24])
