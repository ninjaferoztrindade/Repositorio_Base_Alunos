import requests

usuario = {
    "name": "Th/@g0",
}    
response = requests.post('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',json=usuario)

response=requests.delete('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos/6')
print(response.status_code)
print(response.json())
