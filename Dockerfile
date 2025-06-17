FROM python:3.10-slim

RUN apt-get update && apt-get install -y portaudio19-dev

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["python", "chattbot.py"]
