pip show azure-devops > a.txt
for /f "tokens=2* delims= " %%a in ('call findstr "Location" a.txt') do (set azure-devops=%%a)
echo %azure-devops%
dir .
del a.txt
mkdir .\\dist\\App\\azure
xcopy /E %azure-devops%\\azure .\\dist\\App\\azure
mkdir .\\dist\\App\\templates
xcopy /E .\\templates .\\dist\\App\\templates
dir .\\dist\\App
