@echo off

SET fn=%1
SET pl=%2
SET flags=%3

cd /d %~dp0

If "%1"=="" (
    echo "error"
) else (
    if "%3"=="" (
        python main.py %fn% %pl% 
    ) else (
        python main.py %fn% %pl% %flags%
    )
)
