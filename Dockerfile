FROM python

WORKDIR .

COPY . .

RUN pip install rich loguru
RUN pip install --upgrade pip

CMD ["python", "index.py"]
