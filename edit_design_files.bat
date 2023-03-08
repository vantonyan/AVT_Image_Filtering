@REM This file opens all current project files into single vim tabbed window
@REM
@rem Get the drive letter and save it in DRIVE_LET
@set DRIVE_LET=%~d0

@rem change to drive
@%DRIVE_LET%

SET F1="initial_test.py"
SET F2="AVT_filter.py"
SET F9="a.bat"
SET F10="edit_design_files.bat"

SET CONF = "-u ../Utility/_vimrc "


@set VIME="none"
@IF EXIST "C:\Users\Active\Documents\Vim\vim90\gvim.exe" SET VIME="C:\Users\Active\Documents\Vim\vim90\gvim.exe"
@IF EXIST "C:\Program Files (x86)\Vim\vim82\gvim.exe" SET VIME="C:\Program Files (x86)\Vim\vim82\gvim.exe"
@IF EXIST "C:\Program Files (x86)\Vim\vim81\gvim.exe" SET VIME="C:\Program Files (x86)\Vim\vim81\gvim.exe"
@IF EXIST "C:\Vim\vim82\gvim.exe" SET VIME="C:\Vim\vim82\gvim.exe"

@if %VIME%=="none" goto Exit_Script

@start /B "" %VIME% %CONF% "-p" %F1% %F2% %F3% %F4% %F5% %F6% %F7% %F8% %F9% %F10%
@exit

:Exit_Script
@echo "Did not find VIM, I hope you are not an Emacs fun. Exiting!"
@pause
@exit
