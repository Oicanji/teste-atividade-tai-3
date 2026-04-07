class Frase:
    def __init__(self, frase:str, ano:int, tipo_citacao:str):
        self.frase = frase
        self.ano = ano
        self.tipo_citacao = tipo_citacao

    def citar_frase_completo(self):
        return self.tipo_citacao + ": " + self.frase + " / " + str(self.ano)

    def testar_no_console(self):
        print(self.citar_frase_completo())