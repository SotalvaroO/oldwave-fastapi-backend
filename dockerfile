# image python
FROM python:3.9

# workspace
WORKDIR /code

# requirements for app
COPY ./requirements.txt /code/requirements.txt

# install requeriments
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# code of app
COPY ./app /code/app

# command runs
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

