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
