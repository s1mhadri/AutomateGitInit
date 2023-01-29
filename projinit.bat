@echo off

SET fn=%1
SET pl=%2
SET flags=%3

SET pd=%cd%

cd /d %~dp0

If "%1"=="" (
    echo "error"
) else (
    if "%3"=="" (
        python main.py main.py %fn% %pl% %pd%
    ) else (
        python main.py main.py %fn% %pl% %pd% %flags%
    )
)
