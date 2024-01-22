:: turn off the display commands in the command prompt
@echo off

@REM :: ============================ USER PARAMETERS =================
:: user 
set user=%USERNAME%
set pathExec=%~dp0
set pythonScript="%pathExec%app\app.py"

:: ============================ CALL ENV ============================
:: Activating new environment
echo "Activating project environment..."
call "%pathExec%.venv\Scripts\activate.bat"

echo %pythonScript%

:: ============================ EXECUTING ============================

@REM Init function
func start