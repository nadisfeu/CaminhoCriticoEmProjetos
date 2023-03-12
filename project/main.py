from functions import Functions
import pandas as pd

#arquivo = Functions("Anexo/critical_path/TOY.csv")
arquivo = Functions("C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/CaminhoCriticoEmProjetos/project/Anexo/critical_path/CienciasBiologicas.csv")
# print(arquivo.print_table())

print(arquivo.print_table())
print(arquivo.graph.adj_list)
print(arquivo.graph.dijkstra_max(0))
dijkstra_max = arquivo.graph.dijkstra_max(0)
path_critical = arquivo.graph.get_critical_path(dijkstra_max[1], (len(dijkstra_max[1])-2))
print(path_critical)

# mostrando disciplinas criticas
arquivo.critical(path_critical)
