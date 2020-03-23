FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
#requirements has dependencies and etc
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#copy stuff on old machine to new machine
CMD ["python","app2.py"]
#how run command
