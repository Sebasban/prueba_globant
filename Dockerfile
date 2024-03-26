
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
RUN chmod +w request.py

# Comando para ejecutar tu aplicación cuando se inicie el contenedor
CMD ["ApiRest", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python3", "request.py"]
