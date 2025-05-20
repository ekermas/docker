FROM python:3-slim

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m venv $VIRTUAL_ENV

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY boot.py ./

CMD ["python3", "boot.py"]
