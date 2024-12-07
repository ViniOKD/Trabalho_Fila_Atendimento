from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor : int

class no:
    def __init__(self, x : item, prioridade = 1):
        self.dado : item = x
        self.prox : no | None = None
        self.ant : no | None = None
        self.prioridade = prioridade
        self.cont = 0

class fila:
    def __init__(self):
        self.primeiro = no(item(None))
        self.primeiro.prox = None
        self.primeiro.ant = None
        self.ultimo = None
        self.tamanho = 0
        self.contador = 1

    def vazia(self):
        ''' Função que verifica se uma fila está vazia e retorna True para vazia e False para não vazia
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.vazia()
        False
        >>> f.desenfileira()
        1
        >>> f.vazia()
        True
        '''
        return self.tamanho == 0
    
    def enfileira_geral(self):
        ''' Função que enfileira elementos com prioridade normal (prioridade=1), os elementos que tem prioridade normal podem ser pulados em até 2 vezes por elementos
        de prioridade alta(prioridade=2)
        Exemplo do funcionamento de um fila:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_geral()
        3
        >>> f.enfileira_prioritaria()
        4
        >>> f.enfileira_geral()
        5
        >>> f.enfileira_prioritaria()
        6
        >>> f.vazia()
        False
        >>> f.mostra_fila()
        [1, 4, 2, 6, 3, 5]
        '''
        novo = no(item(self.contador))

        if self.vazia():
            self.primeiro.prox = novo
            novo.ant = self.primeiro

        else:
            self.ultimo.prox = novo
            novo.ant = self.ultimo
            
        novo.prox = self.primeiro    
        self.primeiro.ant = novo   
        self.ultimo = novo
        self.tamanho += 1
        self.contador += 1
        return novo.dado.valor

    def enfileira_prioritaria(self):
        ''' Função que enfileira um item com prioridade alta (prioridade=2) na fila, onde ele pode 'pular' no máximo 2 elementos de prioridade normal (prioridade=1) 
        e que tenham sido pulados menos de 2 vezes
        Exemplo do funcionamento de uma fila:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioritaria()
        3
        >>> f.enfileira_prioritaria()
        4
        >>> f.enfileira_geral()
        5
        >>> f.enfileira_prioritaria()
        6
        >>> f.vazia()
        False
        >>> f.mostra_fila()
        [3, 4, 1, 2, 6, 5]
        >>> f2 = fila()
        >>> f2.vazia()
        True
        >>> f2.enfileira_prioritaria()
        1
        >>> f2.enfileira_geral()
        2
        >>> f2.enfileira_geral()
        3
        >>> f2.enfileira_prioritaria()
        4
        >>> f2.enfileira_geral()
        5
        >>> f2.enfileira_prioritaria()
        6
        >>> f2.vazia()
        False
        >>> f2.obtem_primeiro()
        1
        >>> f2.mostra_fila()
        [1, 4, 2, 6, 3, 5]
        >>> f2.desenfileira()
        1
        >>> f2.mostra_fila()
        [4, 2, 6, 3, 5]
        >>> f2.desenfileira()
        4
        >>> f2.desenfileira()
        2
        >>> f2.enfileira_prioritaria()
        7
        >>> f2.mostra_fila()
        [6, 3, 7, 5]
        '''
        novo = no(item(self.contador), 2)
        p = self.ultimo
        if not self.vazia():
            if p.prioridade == 1 and p.cont < 2:
                if (p.ant != self.primeiro) and (p.ant.prioridade == 1) and (p.ant.cont < 2):
                    p = p.ant
                    novo.prox = p
                    novo.ant = p.ant
                    p.ant.prox = novo
                    p.ant = novo

                    p.cont += 1
                    p.prox.cont += 1
                    
                else:
                    novo.prox = p
                    novo.ant = p.ant
                    p.ant.prox = novo
                    p.ant = novo

                    novo.prox.cont += 1
                
        else:
            self.primeiro.prox = novo
            novo.ant = self.primeiro
            novo.prox = self.primeiro    
            self.primeiro.ant = novo   
            self.ultimo = novo
            
        
        self.tamanho += 1
        self.contador += 1
        return novo.dado.valor
        
    def desenfileira(self):
        ''' Função que desenfileira a fila, remove o primeiro elemento da fila e o retona
        >>> f1 = fila()
        >>> f1.vazia()
        True
        >>> f1.enfileira_geral()
        1
        >>> f1.enfileira_geral()
        2
        >>> f1.enfileira_prioritaria()
        3
        >>> f1.mostra_fila()
        [3, 1, 2]
        >>> f1.desenfileira()
        3
        >>> f1.mostra_fila()
        [1, 2]
        '''
        ptr = self.primeiro.prox
        if self.vazia():
            raise ValueError("Fila Vazia")
        
        ptr.prox.ant = self.primeiro
        self.primeiro.prox = ptr.prox
        ptr.prox = None
        ptr.ant = None 
        self.tamanho -= 1
        
        return ptr.dado.valor
        
    def obtem_primeiro(self):
        ''' Função que retorna o primeiro elemento de uma fila:
        Exemplo:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_prioritaria()            
        2
        >>> f.enfileira_geral()
        3
        >>> f.mostra_fila()
        [2, 1, 3]
        >>> f.enfileira_prioritaria()
        4
        >>> f.enfileira_geral()
        5
        >>> f.enfileira_prioritaria()
        6
        >>> f.vazia()
        False
        >>> f.mostra_fila()
        [2, 4, 1, 6, 3, 5]
        >>> f.obtem_primeiro()
        2
        >>> f.desenfileira()
        2
        >>> f.obtem_primeiro()
        4
        '''
        return self.primeiro.prox.dado.valor
    
    def obtem_ultimo(self):
        ''' Função que retorna o ultimo elemento de uma fila:
        Exemplo:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_prioritaria()            
        2
        >>> f.enfileira_geral()
        3
        >>> f.mostra_fila()
        [2, 1, 3]
        >>> f.enfileira_prioritaria()
        4
        >>> f.enfileira_geral()
        5
        >>> f.enfileira_prioritaria()
        6
        >>> f.vazia()
        False
        >>> f.mostra_fila()
        [2, 4, 1, 6, 3, 5]
        >>> f.obtem_ultimo()
        5
        '''
        return self.ultimo.dado.valor

    def mostra_fila(self):
        ''' Mostra os elementos da fila em um arranjo
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_geral()
        3
        >>> f.enfileira_prioritaria()
        4
        >>> f.enfileira_geral()
        5
        >>> f.enfileira_prioritaria()
        6
        >>> f.vazia()
        False
        >>> f.mostra_fila()
        [1, 4, 2, 6, 3, 5]
        '''
        if self.vazia():
            raise ValueError("Fila Vazia")
        
        else:
            t = []
            i = 0
            ptr = self.primeiro
            while i < self.tamanho :
                t.append(ptr.prox.dado.valor)
                ptr = ptr.prox
                i += 1
            return t