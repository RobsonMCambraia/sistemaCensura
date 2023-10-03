import re

# Leitura do arquivo de palavrões
with open("palavroes.txt") as arquivo:
    palavroes = [linha.strip().upper() for linha in arquivo]

# Interação com o usuário
chat = input('Me xinga, vai!\t').upper()
mensagem = chat.split(" ")

# Censura dos palavrões
improprio = []

for palavra in palavroes:
    for i, palavra_mensagem in enumerate(mensagem):
        mensagem_censurada = re.sub(palavra, '*' * len(palavra), palavra_mensagem)
        if mensagem_censurada != palavra_mensagem:
            mensagem[i] = mensagem_censurada
            improprio.append(palavra)

mensagem_censurada = ' '.join(mensagem)

if improprio:
    print(f'Número de palavrões encontrados: {len(improprio)}')
    print(f'Palavrões encontrados: {improprio}')
    print(f'Mensagem censurada: {mensagem_censurada}')
else:
    print('Nenhum palavrão encontrado')
