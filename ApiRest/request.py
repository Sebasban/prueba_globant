import requests

url = "http://localhost:8000/other_endpoint"  # Suponiendo que la aplicación esté en ejecución en localhost en el puerto 8000

response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Imprimir el contenido de la respuesta
    print(response.json())
else:
    print("Error:", response.status_code)