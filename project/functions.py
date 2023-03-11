from weightedGraph import WeightedGraph
import pandas as pd


class Functions:
    def __init__(self, file_path: str):
        self.table = pd.read_csv(file_path)
        self.graph = WeightedGraph(len(self.table["Código"]))
        self.make_weightedgraph()

    def print_table(self):
        return self.table

    # ideia para montar o grafo: le o codigo da linha e depois procura na coluna de dependencias
    # se algum depende dele e faz a conexão
    def make_weightedgraph(self):
        # le o codigo por matéria
        for c in range(len(self.table["Código"])):
            cod = self.table["Código"][c]  # olha a linha c e o codigo dela
            dep = self.table.loc[self.table["Dependências"] == cod]  # procura se alguma das materias tem dep
            for i in dep.index:
                self.graph.add_directed_edge(c, i, 1)  # cria a aresta no grafo com o peso 1
