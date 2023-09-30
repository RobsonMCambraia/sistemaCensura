# Sistema que substitue palavras impróprias
import re
arq = open("palavroes.txt")
palavroes = []
NovoPalavroes = []
linhas = arq.readlines()

for linha in linhas:
    linha = linha.strip().upper()
    palavroes.append(linha)

for i in palavroes:
    if i not in NovoPalavroes:
        NovoPalavroes.append(i)

chat = input('Me xinga, vai!\t').upper().split(" ")

padrao = r'[!@#$%^&*()\-_+=\[\]{}|\\:;<>,.?/\'"]'
chatNovo = []
for j in chat:
    chatNovo.append(re.sub(padrao, '', j))


improprio = []
for k in NovoPalavroes:
    if k in chatNovo:
        improprio.append(k)

print(f'Numero de palavrões encontrados: {len(improprio)}\nPalavrões encontrados:\t', improprio)if improprio else 'Nenhum palavrão encontrado'

arq.close()