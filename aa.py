from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor : int

class no:
    def __init__(self, x : item, prioridade = 0):
        self.dado : item = x
        self.prox : no | None = None
        self.ant : no | None = None
        self.prioridade : int = prioridade
        self.pulado : int = 0

class fila:
    def __init__(self):
        self.inicio : no | None = no(item(None))
        self.fim : no | None = no(item(None))
        self.inicio.prox = self.fim
        self.inicio.ant = None
        self.fim.prox = None
        self.fim.ant = self.inicio
        self.tamanho = 0

    def vazia(self):
        return self.tamanho == 0

    def enfileira(self, x : item):  # Insire no fim, FILO
        novo = no(x)
        novo.ant = self.fim.ant
        novo.prox = self.fim
        self.fim.ant.prox = novo
        self.fim.ant = novo
        self.tamanho += 1

    def enfileira_prioridade(self, x : item):
        novo = no(x,1)
        p = self.obtem_fim()
        
        if p.prioridade == 0 and p.pulado < 2:
            if p.ant.prioridade == 0 and p.ant.pulado < 2:
                
                i = self.obtem_indice(p.ant)
            else:
                i = self.obtem_indice(p)

            self.insere_pos(novo, i)
    
        else:
            self.insere_pos(novo, self.tamanho)



    def desenfileira(self):         # Retira do inicio, FILO
        if self.vazia():
            raise ValueError("Fila Vazia")
        else:
            rem = self.inicio.prox
            self.inicio.prox = rem.prox
            rem.prox.ant = self.inicio
            self.tamanho -= 1
            return rem.dado.valor

    def obtem_inicio(self):
        if self.vazia():
            raise ValueError("FIla Vazia")

        else:
            return self.inicio.prox.dado
        
    def obtem_fim(self):
        ''' 
        '''
        if self.vazia():
            raise ValueError("Fila Vazia")
        
        else:
            return self.fim.ant
        
    def mostra_fila(self):
        ''' Mostra os elementos da fila em um arranjo
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira(item(120))
        >>> f.enfileira(item(22))
        >>> f.enfileira(item(308))
        >>> f.enfileira(item(99))
        >>> f.vazia()
        False
        >>> f.mostra_fila()
        [120, 22, 308, 99]
        '''
        if self.vazia():
            raise ValueError("Fila Vazia")
        
        else:
            t = []
            i = 0
            ptr = self.inicio
            while i < self.tamanho:
                t.append(ptr.prox.dado.valor)
                ptr = ptr.prox
                i += 1
            return t
            
    def insere_pos(self, novo : no, n : int):
        
        i = 0
        ptr = self.inicio
        while i < n:
            ptr = ptr.prox
        
        novo.ant = ptr.ant
        novo.prox = ptr
        ptr.ant = novo


    def obtem_indice(self, x : item):
        ptr = self.primeiro
        j = 0
        while (j < self.tamanho) and (ptr.prox.dado != x):
            ptr = ptr.prox
            j += 1
        
        return j
