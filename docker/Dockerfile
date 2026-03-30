FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn redis websockets python-jose
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]