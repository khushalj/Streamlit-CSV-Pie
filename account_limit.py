# Define the security policy name
$policyName = "Accounts: Limit local account use of blank passwords to console logon only"

# Define the desired policy value
$desiredPolicyValue = 1  # 1 represents "Enabled"

# Get the current policy value
$currentPolicyValue = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "LimitBlankPasswordUse"

# Check if the current policy value matches the desired value
if ($currentPolicyValue.LimitBlankPasswordUse -ne $desiredPolicyValue) {
    # Set the policy value to the desired value
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "LimitBlankPasswordUse" -Value $desiredPolicyValue

    $status = "Policy set to Enabled"
} else {
    $status = "Policy already set to Enabled"
}

# Generate a report
$report = [PSCustomObject]@{
    PolicyName = $policyName
    DesiredValue = $desiredPolicyValue
    CurrentValue = $currentPolicyValue.LimitBlankPasswordUse
    Status = $status
}

# Define the path to the user's Documents folder
$documentsPath = [Environment]::GetFolderPath("MyDocuments")
$reportPath = Join-Path -Path $documentsPath -ChildPath "security_policy_report.csv"

# Export the report to a CSV file
$report | Export-Csv -Path $reportPath -NoTypeInformation

Write-Host "Report generated and saved to: $reportPath"