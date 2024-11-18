from dataclasses import dataclass
from enum import Enum, auto
import sys
from fila_arranjo import Fila


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)

    demandas = le_arquivo(sys.argv[1])
    f = fila()
    for demanda in demandas:
        if demanda.tipo == Tipo.GERAL:
            f.enfileira_geral()
        else:
            f.enfileira_prioritaria()

    while not f.vazia():
        pos = f.desenfileira()
        print(pos, demandas[pos - 1].nome)


class Tipo(Enum):
    GERAL = auto()
    PRIORITARIA = auto()


@dataclass
class Demanda:
    nome: str
    tipo: Tipo


def le_arquivo(nome: str) -> list[Demanda]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista com as demandas.
    O arquivo deve ter uma demanda por linha, que consiste no nome
    da pessoa (geral) ou de um asterisco seguido do nome da pessoa
    (prioritária)

    Por exemplo, para o arquivo

    Pedro
    *Ana
    Paula

    a resposta produzida é
    [Demanda('Pedro', Tipo.GERAL), Demanda('Ana', Tipo.PRIORITARIA), Demanda('Paula', Tipo.GERAL)]
    '''
    try:
        with open(nome) as f:
            demandas = []
            for linha in f.readlines():
                linha = linha.strip()
                if linha[0] == '*':
                    demandas.append(Demanda(linha[1:], Tipo.PRIORITARIA))
                else:
                    demandas.append(Demanda(linha, Tipo.GERAL))
            return demandas
    except IOError as e:
        print(
            f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        sys.exit(1)


if __name__ == '__main__':
    main()
