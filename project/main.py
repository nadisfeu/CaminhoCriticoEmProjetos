from functions import Functions
import pandas as pd

arquivo = Functions("Anexo/critical_path/TOY.csv")
# print(arquivo.print_table())

print(arquivo.print_table())
print(arquivo.graph.adj_list)
#print(arquivo.graph.dijkstra_max(0))
