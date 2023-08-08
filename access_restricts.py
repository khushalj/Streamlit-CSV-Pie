# Define the registry path and value name
$registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
$valueName = "NoConnectedUser"

# Get the registry value
$policyValue = Get-ItemProperty -Path $registryPath -Name $valueName -ErrorAction SilentlyContinue

# Translate the policy value to a meaningful string
if ($policyValue -and $policyValue.$valueName -eq 1) {
    $policyStatus = "Users can't add or log on with Microsoft accounts"
} else {
    $policyStatus = "Unrestricted"
}

# Create a custom object with policy information
$policyInfo = [PSCustomObject]@{
    "PolicyName" = "Accounts: Block Microsoft accounts"
    "PolicyStatus" = $policyStatus
}

# Export the policy information to a CSV file
$policyInfo | Export-Csv -Path "C:\BlockMicrosoftAccountsPolicyReport.csv" -NoTypeInformation

Write-Host "Policy report generated: BlockMicrosoftAccountsPolicyReport.csv"