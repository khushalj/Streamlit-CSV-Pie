# Import the Active Directory module
Import-Module ActiveDirectory

# Get all user accounts
$users = Get-ADUser -Filter *

# Create an array to store the results
$results = @()

# Iterate through each user
foreach ($user in $users) {
    $userProperties = @{
        "Username" = $user.SamAccountName
        "LoginAttempts" = $user.BadLogonCount
    }
    $results += New-Object PSObject -Property $userProperties
}

# Export the results to a CSV file
$results | Export-Csv -Path "LoginAttemptsReport.csv" -NoTypeInformation

Write-Host "CSV report generated: LoginAttemptsReport.csv"