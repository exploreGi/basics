ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-alpine3.19

# Install Git
RUN apk add --no-cache git

WORKDIR /app

# Clone the repository
RUN git clone https://github.com/exploreGi/basics.git . 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY displayMDFilenames.py .

ENV FLASK_APP=displayMDFilenames.py

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]



