from entidade.preco import Preco
from entidade.qualificador import Qualificador
from entidade.categoria import Categoria
from entidade.supermercado import Supermercado

class Produto:
    def __init__(self, nome: str, descricao: str, codigo: int, supermercado: Supermercado, categoria: Categoria, qualificadores, info_precos): #verificar todos os atributos,getters e setters
        self.__nome = nome
        self.__descricao = descricao
        self.__codig = codigo
        self.__supermercado = supermercado
        self.__categoria = categoria
        self.__qualificadores = qualificadores
        self.__precos = []
    
    def add_preço(self, informacoes_preco): #rever esse comando
        preco_existe = False
        valor = informacoes_preco["valor"]
        data = informacoes_preco["data"]
        confirmacao = informacoes_preco["confirmacao"]
        for preco in self.__precos:
            if preco.valor == valor:
                preco.confirmacao += 1
                preco_existe = True
        if preco_existe == False:
            novo_preco = Preco(data, valor, confirmacao)
            self.__precos.append(novo_preco)
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def codig(self):
        return self.__codig
    
    @codig.setter
    def codig(self, codig): #rever esse codig
        self.__codig = codig
    
    @property
    def supermercado(self):
        return self.__supermercado
    
    @supermercado.setter
    def supermercado(self, supermercado):
        self.__supermercado = supermercado
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
    
    @property
    def precos(self):
        return self.__precos
    
    @precos.setter
    def precos(self, precos):
        self.__precos = precos
    
    @property
    def qualificadores(self):
        return self.__qualificadores
    
    @qualificadores.setter
    def qualificadores(self, qualificadores):
        self.__qualificadores = qualificadores

