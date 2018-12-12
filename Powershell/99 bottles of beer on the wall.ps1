function Get-BottleString($bottles) {
    return "$bottles " + $(if ($bottles -ne 1) { "bottles" } else { "bottle" })
}
function Push-BottleOff($bottles) {
    if($bottles -le 0) { return }
    $str = Get-BottleString -bottles $bottles
    Write-Host "$str of beer on the wall, $str of beer."
    --$bottles
    $str = Get-BottleString -bottles $bottles
    Write-Host "Take one down and pass it around, $str of beer on the wall. `r`n"
    Push-BottleOff($bottles)
    return
}
Push-BottleOff -bottles 100