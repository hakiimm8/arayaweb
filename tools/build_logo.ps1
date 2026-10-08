# Recreate the Araya web lockup as outlined vector artwork; no runtime fonts.
Add-Type -AssemblyName System.Drawing
$logoOutput = Join-Path $PSScriptRoot '../public/assets/images/araya-logo-v2.svg'
$logoCulture = [System.Globalization.CultureInfo]::InvariantCulture
function Format-LogoNumber([single]$value) { $value.ToString('0.###', $logoCulture) }
function Get-LogoTextPath([string]$text, [single]$top) {
    $shape = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $family = [System.Drawing.FontFamily]::new('Arial')
    try {
        $shape.AddString($text, $family, [int][System.Drawing.FontStyle]::Bold, 40, [System.Drawing.PointF]::new(0,0), [System.Drawing.StringFormat]::GenericTypographic)
        $bounds = $shape.GetBounds()
        $matrix = [System.Drawing.Drawing2D.Matrix]::new((212 / $bounds.Width),0,0,(26 / $bounds.Height),(74 - $bounds.X * 212 / $bounds.Width),($top - $bounds.Y * 26 / $bounds.Height))
        $shape.Transform($matrix)
        $matrix.Dispose()
        $points = $shape.PathPoints
        $types = $shape.PathTypes
        $commands = [System.Collections.Generic.List[string]]::new()
        for ($index = 0; $index -lt $points.Length; $index++) {
            $type = $types[$index] -band 7
            $point = $points[$index]
            if ($type -eq 0) { $commands.Add(('M{0} {1}' -f (Format-LogoNumber $point.X),(Format-LogoNumber $point.Y))) }
            elseif ($type -eq 1) { $commands.Add(('L{0} {1}' -f (Format-LogoNumber $point.X),(Format-LogoNumber $point.Y))) }
            elseif ($type -eq 3) {
                $next = $points[$index + 1]; $end = $points[$index + 2]
                $commands.Add(('C{0} {1} {2} {3} {4} {5}' -f (Format-LogoNumber $point.X),(Format-LogoNumber $point.Y),(Format-LogoNumber $next.X),(Format-LogoNumber $next.Y),(Format-LogoNumber $end.X),(Format-LogoNumber $end.Y)))
                $index += 2
            }
            if (($types[$index] -band 128) -ne 0) { $commands.Add('Z') }
        }
        $commands -join ' '
    } finally { $shape.Dispose(); $family.Dispose() }
}
$topLine = Get-LogoTextPath 'PT. ARAYA' 4
$bottomLine = Get-LogoTextPath 'INTERNUSA' 35
$logoSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 64" width="290" height="64" role="img" aria-labelledby="logo-title">
  <title id="logo-title">PT. Araya Internusa</title>
  <g fill="none" stroke="#fff">
    <circle cx="31" cy="32" r="28.5" stroke-width="3"/>
    <path d="M22 12 C11 17 10 32 16 41 C23 51 38 52 46 42 V32 H21" stroke-width="4.5" stroke-linejoin="round"/>
    <path d="M31 9 V45 M24 32 H59" stroke-width="5"/>
  </g>
  <g fill="#fff" fill-rule="evenodd"><path d="$topLine"/><path d="$bottomLine"/></g>
</svg>
"@
[System.IO.File]::WriteAllText($logoOutput, $logoSvg, [System.Text.UTF8Encoding]::new($false))
Write-Output 'Built transparent outlined SVG logo.'
