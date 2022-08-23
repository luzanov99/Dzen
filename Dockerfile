FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD set FLASK_APP=webapp   && set FLASK_ENV=development  && set FLASK_DEBUG=1   && flask run