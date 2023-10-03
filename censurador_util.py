import re

class Censurador:
    def __init__(self, arquivo_palavroes):
        self.palavroes = self.carregar_palavroes(arquivo_palavroes)
    
    def carregar_palavroes(self, arquivo_palavroes):
        with open(arquivo_palavroes) as arquivo:
            return [linha.strip().upper() for linha in arquivo]
    
    def censurar_mensagem(self, mensagem):
        mensagem = mensagem.upper()
        palavras = mensagem.split()
        improprio = []

        for palavra in self.palavroes:
            for i, palavra_mensagem in enumerate(palavras):
                if palavra in palavra_mensagem:
                    palavras[i] = re.sub(palavra, '*' * len(palavra), palavra_mensagem)
                    improprio.append(palavra)
        
        mensagem_censurada = ' '.join(palavras)

        return mensagem_censurada, improprio
