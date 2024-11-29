from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor : int | None

class no:
    def __init__(self, x : item, prioridade : int = 0):
        self.dado : item = x
        self.prox : no | None = None
        self.ant : no | None = None
        self.prioridade = prioridade
        self.cont = 0

class lista:
    def __init__(self):
        self.primeiro = no(item(None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def vazia(self) -> bool:
        return self.primeiro.prox == self.ultimo

    def busca(self, x : int):
        ptr = self.primeiro.prox
        while ptr != None:
            if ptr.dado.valor == x:
                return ptr
            ptr = ptr.prox

        return None

    def busca_item(self, x : item) -> item | None:
        ptr = self.busca(x.valor)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None

    def inserir_ini(self, x : item):
        if self.busca(x.valor) == None:
            novo = no(x)
            novo.prox = self.primeiro.prox
            novo.ant = self.primeiro

            if self.primeiro.prox != None:
                self.primeiro.prox.ant = novo

            if self.ultimo == self.primeiro:
                self.ultimo = novo

            self.primeiro.prox = novo
    
    def inserir_fim(self, x : item):
        if self.busca(x.valor) == None:
            novo = no(x)
            novo.ant = self.primeiro.ant
            novo.prox = self.primeiro

            if self.primeiro.ant != None:
                self.primeiro.ant.prox = novo

            if self.primeiro == self.ultimo:
                self.primeiro.prox = novo

            self.primeiro.ant = novo

    def imprime(self):
        if self.vazia():
            raise ValueError("Lista Vazia")
        
        else:
            ptr = self.primeiro.prox
            while ptr != None:
                print(ptr.dado.valor)
                ptr = ptr.prox


class fila():
    def __init__(self):
        self.primeiro = no(item(None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def vazia(self):
        return self.primeiro == self.ultimo
    
    def busca(self, n : int):
        if not self.vazia():
            ptr = self.primeiro
            while (ptr.prox != self.primeiro) and (ptr.prox.dado.valor != n):
                ptr = ptr.prox
            return ptr

    def busca_item(self, x : item):
        ptr = self.busca(x.valor)
        if ptr != None:
            return deepcopy(ptr)
        return None
   
    def enfileira_geral(self, x : item):
        novo = no(x)
        

        if self.busca(x.valor) == None:
            novo.ant = self.ultimo
            novo.prox = self.primeiro
            self.ultimo.prox = novo
            self.ultimo = novo
            self.primeiro.ant = self.ultimo
            


            
    def busca_indice(self, n : int):
        if self.busca != None:
            if n == 0:
                return 0
            else:
                ptr = self.primeiro.prox
                i = 0
                
                while i < n:
                    ptr = ptr.prox
                    i += 1

                return ptr


    def enfileira_prioridade(self, x: item):
        novo = no(x,prioridade=1)

        if self.busca(x.valor) == None:
            ptr = self.ultimo
            i = 0
            if ptr.ant.prioridade != 1 and ptr.ant.cont <= 2 and i <= 2:
                i += 1
                ptr = ptr.ant
            
            aux = self.busca_indice(i)
            novo.prox = aux.prox
            novo.ant = aux
            aux.prox.ant = novo
            aux.prox = novo

    def imprime(self): # NAO FUNCIONA
        if self.vazia():
            raise ValueError("Fila Vazia")
        
        else:
            ptr = self.primeiro.prox
            while ptr != self.primeiro:
                print(ptr.dado.valor)
                ptr = ptr.prox
            


f1 = fila()
f1.enfileira_geral(item(23))
f1.enfileira_geral(item(62))
#f1.enfileira_prioridade(item(99))
f1.imprime()