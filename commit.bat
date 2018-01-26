@echo off

echo ========================
echo RUN git status :
git status
echo ========================
set /p desc=

if not %desc% == q git add .
if not %desc% == q git commit -m "%desc%"
if not %desc% == q git push

if %desc% == q exit

git log -p

pause
