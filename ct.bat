@setlocal enableExtensions enableDelayedExpansion
@echo off

set _CURRENT_FILE_DIR=%~dp0
set _CURRENT_FILE_DIR=%_CURRENT_FILE_DIR:~0,-1%

python "%_CURRENT_FILE_DIR%\ct.py" %1 %2 %3 %4 %5 %6 %7 %8 %9

@echo on
@endlocal
