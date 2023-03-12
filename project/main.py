from functions import Functions
import pandas as pd

arquivo = Functions("C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/CaminhoCriticoEmProjetos/project/Anexo/critical_path/TOY.csv")
# print(arquivo.print_table())

print(arquivo.print_table())
print(arquivo.graph.adj_list)
