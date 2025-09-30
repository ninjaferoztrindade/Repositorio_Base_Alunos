import json
# Uma string no formato JSON
dados_json = '{ "nome":"Thiago", "idade":15, "cidade":"Santana de parnaiba" }'
# Convertendo a string JSON em um dicionário python 

dados_python = json.loads(dados_json)

#Agora você pode acessar os dados os como um dicionário

print (dados_python["nome"]) # Saida de string 
print (dados_python["idade"]) # Saida de inteiro
print (dados_python["cidade"])

import json

pythonValue = {'iscat': False, 'Dog': 0, 'name': 'cliford', 'felineIQ': None, 'Height': "3, 00", 'weight' : '8000 kg', 'behavior': 'clumsy', 'fur color': 'red', 'race' : 'mastins', 'genre': 'male', 'likes to do': 'play with your bone', 'age': '2 anos', 'eye color': 'black', 'tutor' : 'Emily Elizabeth'  }

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)