FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG USER=user

RUN useradd --system ${USER}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./main.py main.py

USER ${USER}

ENTRYPOINT ["python", "main.py"]
