@ECHO OFF
ECHO deleting dummy.txt
del dummy.txt > nul
ECHO 14 = 1MB
ECHO 19 = 32MB
ECHO 20 = 64MB
ECHO 22 = 256MB
ECHO 23 = 512MB
ECHO 24 = 1GB
ECHO 27 = 8GB
ECHO 29 = 32GB
ECHO 30 = 64GB
ECHO etcetera
ECHO Creating file....
echo This is a line of ASCII text to create a very large file!  >  dummy.txt
for /l %%i in (1,1,%1) do (
rem copy files and avoid 0x1A SUB character at end of file
rem copy dummy.txt+dummy.txt dummy2.txt > nul /b /y
rem copy files and add 0x1A SUB character at end of file
    copy dummy.txt+dummy.txt dummy2.txt > nul
    del dummy.txt > nul 
    ren dummy2.txt dummy.txt > nul 
    echo loop %%i
)
echo This is the last line >> dummy.txt
ECHO Completed !
