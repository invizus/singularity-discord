FROM python:3.5

WORKDIR /app
COPY ./singularity-app/* /app/
COPY requirements.txt /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3", "-u", "singularity.py"]
