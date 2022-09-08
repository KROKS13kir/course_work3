FROM python:3.10-slim

WORKDIR /code
COPY datas datas
COPY static static
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY api api
COPY templates templates
COPY main_directory main_directory
COPY logger.py .
COPY tests tests
COPY utils.py .
COPY app.py .

CMD flask run -h 0.0.0.0 -p 80