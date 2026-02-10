param(
    [string]$Path = "chroma_edge_dungeon_palace_interior_balance_pacing.md"
)

if (-not (Test-Path -Path $Path)) {
    Write-Error "File not found: $Path"
    exit 1
}

$lines = Get-Content -Path $Path
$text = Get-Content -Path $Path -Raw

$requiredMaps = @(1,2,3,4,5)
$missingMaps = @()

foreach ($m in $requiredMaps) {
    if ($text -notmatch "##\s+MAP\s+$m\b") {
        $missingMaps += $m
    }
}

$ids = [regex]::Matches($text, 'M([1-5])-[A-Z]') | ForEach-Object { $_.Value } | Select-Object -Unique
$uniqueChestCount = $ids.Count

$perMap = @{}
foreach ($m in $requiredMaps) {
    $perMap[$m] = ($ids | Where-Object { $_ -like "M$m-*" }).Count
}

$expectedPerMap = @{
    1 = 2
    2 = 8
    3 = 2
    4 = 5
    5 = 3
}

$distributionErrors = @()
foreach ($m in $requiredMaps) {
    if ($perMap[$m] -ne $expectedPerMap[$m]) {
        $distributionErrors += "Map $m chest IDs: expected $($expectedPerMap[$m]), got $($perMap[$m])"
    }
}

$hasTotalRow = $false
foreach ($line in $lines) {
    if ($line -match '\*\*TOTAL\*\*' -and $line -match '\*\*20\*\*') {
        $hasTotalRow = $true
        break
    }
}

Write-Output "Unique chest IDs found: $uniqueChestCount"
foreach ($m in $requiredMaps) {
    Write-Output ("Map {0} chest IDs: {1}" -f $m, $perMap[$m])
}
Write-Output ("Summary total row present: {0}" -f $hasTotalRow)

$hardErrors = 0

if ($missingMaps.Count -gt 0) {
    Write-Error ("Missing map sections: " + ($missingMaps -join ', '))
    $hardErrors++
}

if ($uniqueChestCount -ne 20) {
    Write-Error "Expected 20 unique chest IDs, got $uniqueChestCount"
    $hardErrors++
}

if ($distributionErrors.Count -gt 0) {
    foreach ($e in $distributionErrors) {
        Write-Error $e
    }
    $hardErrors++
}

if (-not $hasTotalRow) {
    Write-Error "Encounter summary total row with chest total 20 not found"
    $hardErrors++
}

if ($hardErrors -gt 0) {
    exit 1
}

Write-Output "Pacing/chest preflight passed."
exit 0
