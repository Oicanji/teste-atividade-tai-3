import classes.Frase as Frase

class Pessoa:
    def __init__(self, nome:str, idade:int, nacionalidade:str, profissao:str):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.profissao = profissao
        self.citacoes = []

    def todas_citacoes(self):
        texto = self.nome + " (" + self.profissao + ")" + " - " + str(self.idade) + " anos."
        texto += "\n\n" # quebra de linhas para ficar mais bonito só
        for frase in self.citacoes:
            texto += frase.citar_frase_completo() + "\n"

        return texto

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "nacionalidade": self.nacionalidade,
            "profissao": self.profissao,
            "citacoes": [frase.to_dict() for frase in self.citacoes]
        }

    def testar_no_console(self):
        print(self.todas_citacoes())