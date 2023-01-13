FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

# copy project
COPY . .

#
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]