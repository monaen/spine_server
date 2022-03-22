SETLOCAL
set env_name=venv
python -m venv %env_name%
%env_name%\Scripts\python -m pip install --upgrade pip
%env_name%\Scripts\python -m pip install fastapi
%env_name%\Scripts\python -m pip install "uvicorn[standard]"
%env_name%\Scripts\python -m pip install python-multipart
ENDLOCAL

