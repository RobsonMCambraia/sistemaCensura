from censurador_util import Censurador

censurador = Censurador("palavroes.txt")
chat = input('Me xinga, vai!\t')
mensagem_censurada, palavroes_encontrados = censurador.censurar_mensagem(chat)

if palavroes_encontrados:
    print(f'Número de palavrões encontrados: {len(palavroes_encontrados)}')
    print(f'Palavrões encontrados: {palavroes_encontrados}')
    print(f'Mensagem censurada: {mensagem_censurada}')
else:
    print('Nenhum palavrão encontrado')
