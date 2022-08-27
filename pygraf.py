import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#pegando o nome da planilha, não precisa do endereço por estar na mesma página
arquivo_excel = "Dia01.xlsx"
arquivo_excel_exon = "cttos_exonerados.xlsx"

# df_dia_1 = pd.read_excel(arquivo_excel, sheet_name="dia1",)
df_exon = pd.read_excel(arquivo_excel_exon)

df_exon_tratada = df_exon.drop_duplicates(subset="id_imovel", ignore_index=True)

df_exon_tratada.to_excel("cttos_exon_trat.xlsx")


#lucro_dos_vendedores = df_dia_1.groupby(["Nome"]).sum()

#relatorio = lucro_dos_vendedores.loc[:,"Valor"]

#print(relatorio)

#relatorio.plot(kind = 'bar')
#plt.show()

