# Sistema que substitue palavras impróprias

#leitura do arquivo
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

#interação com usuário
padrao = r'[!@#$%^&*()\-_+=\[\]{}|\\:;<>,.?/\'"]'
chat = input('Me xinga, vai!\t').upper()
mensagem = chat.split(" ")
print(mensagem)
for j in mensagem:
    mensagem = re.sub(padrao, '', j)
    
#Censura dos palavrões
improprio = []
for k in NovoPalavroes:
    if k in mensagem:
        print(k)
        improprioCensurado = re.sub(k, f'*'*len(k), mensagem)
        improprio.append(k)
    
print(f'Numero de palavrões encontrados: {len(improprio)}\nPalavrões encontrados:\t', improprio)if improprio else 'Nenhum palavrão encontrado'

print(chat)
print(improprioCensurado)
print(mensagem)
arq.close()