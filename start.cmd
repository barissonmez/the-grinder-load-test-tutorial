set GRINDERPATH=C:\grinder-4.0.0
set GRINDERCLASSPATH=%GRINDERPATH%\lib\grinder.jar;%GRINDERPATH%\lib\json-20220924.jar;

start cmd.exe /k java -cp %GRINDERCLASSPATH% net.grinder.Console

for /R %%f in (*.properties) do start cmd.exe /k java -cp %GRINDERCLASSPATH% net.grinder.Grinder "%%f" 
