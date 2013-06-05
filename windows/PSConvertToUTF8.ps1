$files = Get-ChildItem -recurse "*.xml"
foreach ( $file in $files )
{
    Write-Host $file
    $MyFile = Get-Content $file
    $Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding($False)
    [System.IO.File]::WriteAllLines($file, $MyFile, $Utf8NoBomEncoding)
}