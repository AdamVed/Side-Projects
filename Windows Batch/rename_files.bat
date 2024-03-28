@echo off
mode con: cols=70 lines=15
setlocal enabledelayedexpansion

echo.
set /p search="Enter the part of the filename to replace: "
echo.

set /p replace="Enter what to replace it with (press Enter for empty): "
echo.

if "%replace%"=="" (
    set "replace="
)

set "scriptname=%~nx0"

for %%f in (*%search%*) do (
    set "filename=%%~nf"  ; Set to only the name part of the file
    set "extension=%%~xf" ; Set to only the extension part of the file
    if "%%~nxf" neq "!scriptname!" (
        set "newname=!filename:%search%=%replace%!!extension!" ; Apply replacement and add back the extension
        ren "%%f" "!newname!"
    )
)

echo Finished

pause >nul
