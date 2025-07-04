from typing import Type
from vendedor import Vendedor

class Produto:
    def __init__(self, nome, preco, empresa, vendedor, numero):
        self.numero = numero
        self.nome = nome
        self.preco = preco
        self.empresa = empresa
        self.vendedor = vendedor

    def __str__(self):
        return f"Produto(nome={self.nome}, preco={self.preco})"

    def __repr__(self):
        return f"Produto({self.nome!r}, {self.preco!r})"
    
    def get_nome(self):
        return self.nome
    
    def get_preco(self):
        return self.preco
    
    def get_empresa(self):
        return self.empresa    

    def get_numero(self):
        return self.vendedor
     
    
    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco  
    
    def set_empresa(self, empresa):
        self.empresa = empresa

    def toString(self):
        return f"Produto: {self.nome}, Preço: R$ {self.preco}, Empresa: {self.empresa}, Vendedor: {self.vendedor}"   
    