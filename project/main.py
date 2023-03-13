from functions import Functions
import pandas as pd

#arquivo = Functions("Anexo/critical_path/TOY.csv")
arquivo = Functions("C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/CaminhoCriticoEmProjetos/project/Anexo/critical_path/SJM.csv")
# print(arquivo.print_table())

print(arquivo.print_table())
print(arquivo.graph.adj_list)


# Chama a função dijkstra_critical para encontrar o caminho crítico
caminho_critico = arquivo.graph.dijkstra_max(0, len(arquivo.graph.adj_list)-1)
print(caminho_critico)

# mostrando disciplinas criticas
arquivo.critical(caminho_critico)
