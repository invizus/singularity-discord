FROM python:3.5

WORKDIR /app
COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3", "singularity3.py"]
