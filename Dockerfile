FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get install gcc -y
RUN pip install six
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "./autocomplete.py" ]

