import json
from statistics import mean

with open("dados.json", encoding='utf-8') as arquivo: #abrindo o arquivo json
    objeto = json.load(arquivo) #atribuindo para objeto uma lista com o arquivo jason

maior_valor = max(objeto, key=lambda x: x['valor'])

valoresAtualizados = filter(lambda x: x['valor'] != 0, objeto)
menor_valor = min(valoresAtualizados, key=lambda x: x['valor'])

valoresAtualizadosMedia = filter(lambda x: x['valor'] != 0, objeto)
valores = [x['valor'] for x in valoresAtualizadosMedia]
media = mean(valores)

print(maior_valor)
print(menor_valor)
print(media)
