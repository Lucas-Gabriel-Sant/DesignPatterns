from abc import ABCMeta, abstractmethod


# AbstractFactory
class BibliotecaFactory(metaclass=ABCMeta):

    @abstractmethod
    def livro_ficcao(self):
        pass

    @abstractmethod
    def livro_romance(self):
        pass



#ConcretoFactA
class LivroBrasileiro(BibliotecaFactory):

    def livro_ficcao(self):
        return MonteiroLobato()

    def livro_romance(self):
        return GoncalvesDias()

#ConcretoFactB
class LivroEstrangeiro(BibliotecaFactory):

    def livro_ficcao(self):
        return WilliamShakespeare()

    def livro_romance(self):
        return CharlesDickens()



#AbstractProdutoA
class Ficcao(metaclass=ABCMeta):

    @abstractmethod
    def leitura_simples(self):
        pass

#AbstractProdutoB
class Romance(metaclass=ABCMeta):

    @abstractmethod
    def leitura_completa(self):
        pass



#ProdutoConc
class MonteiroLobato(Ficcao):

    def __repr__(self):
        return 'Monteiro Lobato'

    def leitura_simples(self):
        print(f':: Entregando livros do {MonteiroLobato()} para uma leitura curta...\n')


class GoncalvesDias(Romance):

    def __repr__(self):
        return 'Gonçalves Dias'

    def leitura_completa(self):
        print(f':: Entregando livros do {GoncalvesDias()} para uma leitura longa...\n')

class WilliamShakespeare(Ficcao):

    def __repr__(self):
        return 'William Shakespeare'

    def leitura_simples(self):
        print(f':: Entregando livros do {WilliamShakespeare()} para uma leitura curta...\n')

class CharlesDickens(Romance):

    def __repr__(self):
        return 'Charles Dickens'

    def leitura_completa(self):
        print(f':: Entregando livros do {CharlesDickens()} para uma leitura longa...\n')



#Cliente
class Biblioteca:

    def entregar_livros(self):
        for factory in [LivroBrasileiro(), LivroEstrangeiro()]:
            self.factory = factory
            self.livro_ficcao = self.factory.livro_ficcao()
            self.livro_romance = self.factory.livro_romance()
            self.livro_ficcao.leitura_simples()
            self.livro_romance.leitura_completa()


biblioteca = Biblioteca()
biblioteca.entregar_livros()
