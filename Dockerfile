FROM python:slim
WORKDIR /tg_bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# RUN rm .env
CMD python3 main.py