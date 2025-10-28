from abc import ABCMeta, abstractmethod

# Command
class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass



# ComandoConcreto
class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()


class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.vender()


# Receiver
class Acao:

    def comprar(self):
        print('Você irá comprar ações...')

    def vender(self):
        print('Você irá vender ações...')


# Invoker
class Agente:

    def __init__(self):
        self.__fia_ordens = []

    def adicionar_ordem_na_fila(self, ordem):
        self.__fia_ordens.append(ordem)
        ordem.executar()


if __name__ == '__main__':
    # Cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    # Chamador
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)
