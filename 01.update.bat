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
echo "Runnign ......"
echo:
python.exe -m pip install -U pip
echo:
echo:
echo "Installing/updating ......"
echo:
pip install -r requirements.txt
pause