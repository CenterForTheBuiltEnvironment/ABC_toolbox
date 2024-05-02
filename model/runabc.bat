@echo off
abc<%1.json>%1_out.json
IF ERRORLEVEL 1 GOTO errorHandling
REM no error here, errolevel == 0
echo abc ran sucessfully. output %1_out.json created
if exist %1.csv del %1.csv
ren tskin.csv %1.csv
GOTO :done
:errorHandling
echo ****** Trouble running %1.json ******
type %1_out.json

:done

echo on
