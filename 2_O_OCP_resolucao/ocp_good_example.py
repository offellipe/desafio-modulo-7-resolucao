from abc import ABC, abstractmethod

class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass
    
    @abstractmethod
    def verifica_condicoes_exame(self, exame):
        pass

class AprovaExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Exame sanguíneo aprovado!")

    def verifica_condicoes_exame(self, exame):
        # implemente as condições específicas do exame de sangue
        pass

class AprovaRaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Raio-X aprovado!")

    def verifica_condicoes_exame(self, exame):
        # implemente as condições específicas do exame de raio-x
        pass

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

# Exemplo de uso:
exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_sangue = AprovaExameSangue()
aprovador_raio_x = AprovaRaioX()

aprovador_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovador_raio_x.aprovar_solicitacao_exame(exame_raio_x)

