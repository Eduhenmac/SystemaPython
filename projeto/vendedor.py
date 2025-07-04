
class Vendedor: 
    def __init__(self, nome, numero, empresa):
        self.nome = nome
        self.numero = numero
        self.empresa = empresa

    def __str__(self):
        return f"Vendedor: {self.nome}, CPF: {self.numero}, Empresa: R$ {self.empresa}"
    
    def get_nome(self):
        return self.nome
    
    def get_numero(self):
        return self.numero 
    
    def get_empresa(self):      
        return self.empresa 
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_numero(self, numero):
        self.numero = numero
        
    def set_empresa(self, empresa):
        self.empresa = empresa
    
    def toString(self):
        return f"Nome: {self.nome}, Numero: {self.numero},  Empresa: {self.empresa}"
    

