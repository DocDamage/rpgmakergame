@echo off
REM Asset Naming Validator for Chroma's Edge
REM Run this to check if your assets follow naming conventions

cd /d "%~dp0"
python validate_naming.py ..
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Validation failed! Please fix the errors above.
    pause
    exit /b 1
) else (
    echo.
    echo All validations passed!
    pause
    exit /b 0
)
