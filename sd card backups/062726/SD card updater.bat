REM Search for UpdateAgent 
REM If found, launch then EXIT  
REM If not found, check if file has been previously downloaded, execute, then EXIT.
REM if both are not found, open user's default browser, download, then execute
IF EXIST "C:\Program Files (x86)\Powerteq\Ignition\Ignition.exe" (
  START "" "C:\Program Files (x86)"\Powerteq\Ignition\Ignition.exe"
  EXIT
  ) 
IF EXIST "C:\Users\%USERNAME%\Downloads\UpdateAgent Installer.exe" (
  START "" "C:\Users\%USERNAME%\Downloads\UpdateAgent Installer.exe"
  EXIT
)ELSE (
  START "" "https://fusionupdate.com/Ignition/Powerteq/UpdateAgent Installer.exe"
   REM Loop until found, then execute
  :LoopStart 
  REM Allow adequate time for file to download
  timeout /t 5 /nobreak
  IF NOT EXIST "C:\Users\%USERNAME%\Downloads\UpdateAgent Installer.exe" (
	GOTO LoopStart
  )
  START "" "C:\Users\%USERNAME%\Downloads\UpdateAgent Installer.exe"
)