from weightedGraph import WeightedGraph
import pandas as pd


class Functions:
    def __init__(self, file_path: str):
        self.table = pd.read_csv(file_path)
        self.graph = WeightedGraph()

    def print_table(self):
        return self.table

    # ideia para montar o grafo: le o codigo da linha e depois procura na coluna de dependencias
    # se algum depende dele e faz a conexão
    def make_weightedgraph(self):
        # le o codigo
        for cod in self.table["Código"]:
            print(cod)
            # verifica quem depende desse código
            x = self.table["Dependências"] == cod
            print(x)

        # chegar em casa e tentar fazer o contrairio, ler as dependencias e procurar o código igual


