# image python
FROM python:3.8.5-slim-buster

# workspace
WORKDIR /code

# requirements for app
COPY ./requirements.txt /code/requirements.txt

# install requeriments
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy main.py
COPY ./main.py /code/main.py

# code of app
COPY ./app /code/app

# command runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

