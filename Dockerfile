FROM python:3.13.3-alpine3.21

WORKDIR /usr/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./

CMD [ "python", "main_server.py" ]
EXPOSE 5000


