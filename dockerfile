FROM python:3.14-slim-bookworm

WORKDIR /banana

RUN apt-get update \
    apt-get upgrade 

COPY requirments.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
