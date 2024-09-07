#*********************************************************************************
# Created By: Somnath Das                                                        *
# Purpose: Trigger an Azure DevOps Pipeline                                      *
# Exceptions: N/A                                                                *
#*********************************************************************************

# https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/runs/run-pipeline?view=azure-devops-rest-7.1

$AzureDevOpsPAT = "<PAT>"
$OrganizationName = "daslearning"
$ProjectName = "daslearningProject"
$PipelineId = ""

$AzureDevOpsAuthenicationHeader = @{Authorization = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$($AzureDevOpsPAT)")) }
$UriOrga = "https://dev.azure.com/$OrganizationName/" 

$jsonBody = @{
    variables = @{
        pipeVar = @{
            value = "DasLearning"
        }
    }
}

$uriBuildQueue = $UriOrga + "$($ProjectName)/_apis/pipelines/$($PipelineId)/runs?api-version=7.1-preview.1"
$targetBody = $jsonBody | ConvertTo-JSON
$buildresponse = Invoke-RestMethod -Uri $uriBuildQueue -Method POST -Headers $AzureDevOpsAuthenicationHeader -Body $targetBody -ContentType "application/json"
$runID = $buildresponse.id
$msgbody = "Your request has been queued...." + "`nBuild id: $runID" + "`nPlease use this for future reference"

Write-Host "$msgbody"
