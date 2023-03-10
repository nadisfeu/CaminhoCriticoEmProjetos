from functions import Functions
import pandas as pd

arquivo = Functions("Anexo/critical_path/TOY.csv")
# print(arquivo.print_table())
arquivo.make_weightedgraph()
