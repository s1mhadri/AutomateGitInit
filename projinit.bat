@echo off

SET fn=%1
SET pl=%2
SET flags=%3

If "%1"=="" (
    echo "error"
) else (
    if "%3"=="" (
        conda activate dllab & C:\Users\simha\miniconda3\envs\dllab\python.exe D:\ML_DL_CV\Windows_Batch\main.py %fn% %pl% 
    ) else (
        conda activate dllab & C:\Users\simha\miniconda3\envs\dllab\python.exe D:\ML_DL_CV\Windows_Batch\main.py %fn% %pl% %flags%
    )
)
