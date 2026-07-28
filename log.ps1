$problem = Read-Host "Problem name"
$pattern = Read-Host "Pattern"
$difficulty = Read-Host "Difficulty (Easy/Medium/Hard)"
$status = Read-Host "Status (Solved/Struggled/Revised)"

$today = Get-Date -Format "yyyy-MM-dd"
if ($status -eq "Struggled") {
    $revisit = (Get-Date).AddDays(2).ToString("yyyy-MM-dd")
} else {
    $revisit = (Get-Date).AddDays(5).ToString("yyyy-MM-dd")
}

$line = "| $today | $problem | $pattern | $difficulty | $status | $revisit |"
Add-Content -Path progress.md -Value $line
Write-Host "Logged: $problem (revisit: $revisit)"
