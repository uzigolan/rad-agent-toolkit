param(
    [string]$InputJson,
    [string]$OutputJson,
    [string]$CatalogFile = '.\rad-mcp-server\skills\rad-cli-operations\references\fpga-mea\mea-commands-only-with-relation.txt',
    [string]$Family = 'etx2',
    [string]$Version = '',
    [string]$Source = 'debug mea help -r'
)

$raw = (Get-Content $InputJson -Raw | ConvertFrom-Json).result -split "`n"
$catalog = @()
foreach ($line in (Get-Content $CatalogFile -Encoding UTF8)) {
    $trim = $line.Trim()
    if (-not $trim.StartsWith('MEA ')) { continue }
    if ($trim -match '^(MEA\s+.+?)\s*-\s*Related to\s+(.+?)\.?$') {
        $catalog += $matches[1].Trim()
    } else {
        $catalog += $trim
    }
}
$catalog = $catalog | Sort-Object -Unique
$catalogSet = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)
$prefixSet = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)
foreach ($cmd in $catalog) {
    [void]$catalogSet.Add($cmd)
    $parts = $cmd -split '\s+'
    for ($i = 2; $i -le $parts.Length; $i++) {
        [void]$prefixSet.Add((($parts[0..($i-1)]) -join ' '))
    }
}

function Resolve-ExactCommand {
    param([string[]]$Stack, [string]$Name)
    for ($depth = $Stack.Count; $depth -ge 0; $depth--) {
        $parts = @('MEA')
        if ($depth -gt 0) { $parts += $Stack[0..($depth-1)] }
        $parts += $Name
        $candidate = ($parts -join ' ') -replace '\s+', ' '
        if ($catalogSet.Contains($candidate)) { return $candidate }
    }
    $leafMatches = @($catalog | Where-Object { ($_ -split '\s+')[-1].Equals($Name, [System.StringComparison]::OrdinalIgnoreCase) })
    if ($leafMatches.Count -eq 1) { return $leafMatches[0] }
    return ""
}

function Resolve-NodeStack {
    param([string[]]$Stack, [string]$Name)
    for ($depth = $Stack.Count; $depth -ge 0; $depth--) {
        $parts = @('MEA')
        if ($depth -gt 0) { $parts += $Stack[0..($depth-1)] }
        $parts += $Name
        $candidate = ($parts -join ' ') -replace '\s+', ' '
        if ($prefixSet.Contains($candidate)) {
            if ($depth -gt 0) { return @($Stack[0..($depth-1)] + $Name) }
            return @($Name)
        }
    }
    return @()
}

$commands = New-Object System.Collections.Generic.List[object]
$stack = @()
$started = $false

foreach ($lineRaw in $raw) {
    $line = ($lineRaw -replace "`r", "")
    if (-not $started) {
        if ($line -match 'List of Available Commands') { $started = $true }
        continue
    }
    if (-not $line.Trim()) { continue }
    if ($line -match '^(FPGA>>help -r|Welcome to FPGA CLI Environment|ETX-.*#|> help -r|> debug mea|debug mea)$') { continue }
    $trim = $line.Trim()
    if ($trim -notmatch ':') { continue }

    $parts = $trim -split ':', 2
    $name = $parts[0].Trim()
    $desc = $parts[1].Trim()
    if (-not $name) { continue }

    if ($desc -eq '>>') {
        if ($name -ieq 'MEA') {
            $stack = @()
            continue
        }
        $stack = @(Resolve-NodeStack -Stack $stack -Name $name)
        continue
    }

    $full = Resolve-ExactCommand -Stack $stack -Name $name
    if (-not $full) { continue }
    $commands.Add([ordered]@{
        command = $full
        label = $(if ($desc) { $desc } else { 'recursive help -r command' })
        family = $Family
        version = $Version
        source = $Source
    })
}

$unique = @{}
foreach ($c in $commands) {
    $key = $c.command + '|' + $c.label
    if (-not $unique.Contains($key)) {
        $unique[$key] = $c
    }
}

$out = [ordered]@{
    schema = 'mea-help-r.v1'
    family = $Family
    version = $Version
    source = $Source
    command_count = $unique.Count
    commands = @($unique.Values | Sort-Object command)
} | ConvertTo-Json -Depth 6

Set-Content -Path $OutputJson -Value $out -Encoding UTF8
Write-Host "Wrote $OutputJson with $($unique.Count) commands"
