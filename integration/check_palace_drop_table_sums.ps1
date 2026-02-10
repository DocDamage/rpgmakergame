param(
    [string]$Path = "chroma_edge_dungeon_palace_interior_drop_tables.md"
)

if (-not (Test-Path -Path $Path)) {
    Write-Error "File not found: $Path"
    exit 1
}

$expectedSections = @(
    "Audit Drone",
    "Seal-Leech",
    "Chrono Wisp",
    "Crownshard Sentinel",
    "Redaction Auditor",
    "Bastion Prefect Unit"
)

$lines = Get-Content -Path $Path
$sections = @{}
$current = $null

foreach ($line in $lines) {
    if ($line -match '^###\s+(.+)$') {
        $title = $Matches[1]
        $matched = $null
        foreach ($name in $expectedSections) {
            if ($title -like "*$name*") {
                $matched = $name
                break
            }
        }

        if ($matched) {
            $current = $matched
            if (-not $sections.ContainsKey($current)) {
                $sections[$current] = @()
            }
        }
        else {
            $current = $null
        }

        continue
    }

    if (-not $current) {
        continue
    }

    if ($line -match '^##\s+') {
        $current = $null
        continue
    }

    if ($line -match '\|\s*[^|]+\|\s*(\d+)%\s*\|') {
        if ($line -match 'Bonus Roll') {
            continue
        }

        $pct = [int]$Matches[1]
        $sections[$current] += $pct
    }
}

$missing = @()
$failed = @()

foreach ($name in $expectedSections) {
    if (-not $sections.ContainsKey($name) -or $sections[$name].Count -eq 0) {
        $missing += $name
        continue
    }

    $sum = ($sections[$name] | Measure-Object -Sum).Sum
    if ($sum -ne 100) {
        $failed += [pscustomobject]@{ Section = $name; Sum = $sum }
    }

    Write-Output ("{0}: {1}%" -f $name, $sum)
}

if ($missing.Count -gt 0) {
    Write-Error ("Missing sections: " + ($missing -join ', '))
}

if ($failed.Count -gt 0) {
    foreach ($item in $failed) {
        Write-Error ("Invalid sum in section '{0}': {1}%" -f $item.Section, $item.Sum)
    }
    exit 1
}

if ($missing.Count -gt 0) {
    exit 1
}

Write-Output "All primary drop tables sum to 100%."
exit 0
