FROM python:slim
WORKDIR /tg_bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python3 main.py