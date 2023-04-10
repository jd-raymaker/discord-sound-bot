FROM python:3.10-alpine

RUN apk update
RUN apk add libffi-dev python3-dev ffmpeg

RUN adduser -D apprunner
RUN mkdir -p /app/sounds
RUN chown -R apprunner:apprunner /app
RUN su apprunner

RUN python3 -m pip install libnacl
RUN python3 -m pip install -U "discord.py[voice]"

COPY ../bot.py /app/.
