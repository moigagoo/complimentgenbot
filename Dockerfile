FROM python

RUN curl -OsSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py
RUN python install-poetry.py --preview -y

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml complimentgenbot.py README.md .env /usr/src/app/

RUN /root/.local/bin/poetry install

CMD [ "/root/.local/bin/poetry", "run",  "python", "complimentgenbot.py" ]

