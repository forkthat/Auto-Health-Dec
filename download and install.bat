@REM Assuming x64 bit computer and using a Chromium browser


@REM Install Python 3.11
start /b /wait curl https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe --output python-3.11.0-amd64.exe
start /b /wait python-3.11.0-amd64.exe


@REM Install 7zip to extract Chrome
start /b /wait curl https://www.7-zip.org/a/7z2201-x64.exe --output 7z2201-x64.exe
start /b /wait 7z2201-x64.exe


@REM Download Chromium webdriver
start /b /wait curl https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_win32.zip --output chromedriver_win32.zip
start /b /wait 7z e chromedriver_win32.zip


@REM Install Selenium
start /b /wait python.exe -m pip install --upgrade pip
start /b /wait pip install selenium


@REM Press any key to continue...
timeout /t 30