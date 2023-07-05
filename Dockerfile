FROM python:3

WORKDIR /project

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt install libuv1 zlib1g -y

COPY . .

CMD ["python", "./main.py"]