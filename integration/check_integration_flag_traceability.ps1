param(
    [string]$MatrixPath = "chroma_edge_integration_flag_validation_matrix.md"
)

if (-not (Test-Path -Path $MatrixPath)) {
    Write-Error "Matrix file not found: $MatrixPath"
    exit 1
}

$matrixLines = Get-Content -Path $MatrixPath
$inTraceability = $false
$rowCount = 0
$errorCount = 0
$warnCount = 0

for ($i = 0; $i -lt $matrixLines.Count; $i++) {
    $line = $matrixLines[$i]

    if ($line -match '^##\s+3\)\s+Traceability') {
        $inTraceability = $true
        continue
    }

    if ($inTraceability -and $line -match '^##\s+') {
        break
    }

    if (-not $inTraceability) {
        continue
    }

    if ($line -notmatch '^\|') {
        continue
    }

    if ($line -match '^\|\s*-+' -or $line -match '^\|\s*Flag / Condition\s*\|') {
        continue
    }

    $cells = $line.Split('|')
    if ($cells.Count -lt 4) {
        continue
    }

    $lhs = $cells[1].Trim()
    $rhs = $cells[2].Trim()

    if ([string]::IsNullOrWhiteSpace($lhs) -or [string]::IsNullOrWhiteSpace($rhs)) {
        continue
    }

    $rowCount++

    $flags = [regex]::Matches($lhs, '[A-Z][A-Z0-9_]{2,}') | ForEach-Object { $_.Value } | Select-Object -Unique
    $refs = [regex]::Matches($rhs, '`([^`]+):(\d+)`')

    if ($refs.Count -eq 0) {
        Write-Warning "No file:line references parsed in traceability row ${rowCount}: $lhs"
        $warnCount++
        continue
    }

    foreach ($m in $refs) {
        $file = $m.Groups[1].Value
        $lineNo = [int]$m.Groups[2].Value

        if (-not (Test-Path -Path $file)) {
            Write-Error "Missing file in traceability row ${rowCount}: $file"
            $errorCount++
            continue
        }

        $fileLines = Get-Content -Path $file
        if ($lineNo -lt 1 -or $lineNo -gt $fileLines.Count) {
            Write-Error "Invalid line in traceability row ${rowCount}: ${file}:${lineNo} (max $($fileLines.Count))"
            $errorCount++
            continue
        }

        $target = $fileLines[$lineNo - 1]

        if ($flags.Count -gt 0) {
            $hasFlag = $false
            foreach ($flag in $flags) {
                if ($target -match [regex]::Escape($flag)) {
                    $hasFlag = $true
                    break
                }
            }

            if (-not $hasFlag) {
                Write-Warning "Traceability row ${rowCount} reference ${file}:${lineNo} does not contain listed flag token(s): $($flags -join ', ')"
                $warnCount++
            }
        }
    }
}

Write-Output "Rows parsed: $rowCount"
Write-Output "Warnings: $warnCount"
Write-Output "Errors: $errorCount"

if ($errorCount -gt 0) {
    exit 1
}

Write-Output "Traceability preflight passed (no hard errors)."
exit 0
