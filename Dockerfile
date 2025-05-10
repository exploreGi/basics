ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY displayFiles.py .

ENV FLASK_APP=displayFiles.py

EXPOSE 5000

CMD [ "flask", "run" ,"--host=0.0.0.0" ]



