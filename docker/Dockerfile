FROM ubuntu

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt -yq install libffi-dev libnacl-dev python3.10 python3-pip python3-dev ffmpeg

RUN useradd -ms /bin/bash apprunner
RUN mkdir -p /app/sounds
RUN chown -R apprunner:apprunner /app
USER apprunner

RUN python3 -m pip install libnacl
RUN python3 -m pip install -U "discord.py[voice]"

COPY ../bot.py /app/.
WORKDIR /app

ENTRYPOINT [ "python3", "bot.py" ]
