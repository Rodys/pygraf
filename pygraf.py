from cProfile import label
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#pegando o nome da planilha, não precisa do endereço por estar na mesma página
arquivo_excel = "Dia01.xlsx"
arquivo_excel_exon = "cttos_exonerados.xlsx"

# df_dia_1 = pd.read_excel(arquivo_excel, sheet_name="dia1",)
df_exon = pd.read_excel(arquivo_excel_exon)

#excluindo as linhas duplicadas e salvando no data frame; 
df_exon_tratada = df_exon.drop_duplicates(subset="id_imovel", ignore_index=True)

#gráfico de pizza, contagem dos tipos de imóveis

residencial = df_exon_tratada.loc[df_exon_tratada['tp_imovel'] == 'Residencial'].count()[0]
comercial = df_exon_tratada.loc[df_exon_tratada['tp_imovel'] == 'Comercial'].count()[0]
total_tipo_imovel = residencial + comercial
residencial = residencial/total_tipo_imovel
comercial = comercial/total_tipo_imovel
label_pie = 'Residencial', 'Não residencial'
sizes_pie = residencial, comercial
explode = (0, 0.1)

print(sizes_pie)
print(label_pie)
print(total_tipo_imovel)


fig1, ax1 = plt.subplots()

ax1.pie(sizes_pie, explode=explode, labels = label_pie, autopct='%1.1f%%', shadow=True, startangle=50)
ax1.axis('equal')
plt.show()

'''
#criando o arquivo df_exon_tratada.to_excel("cttos_exon_trat.xlsx")


lucro_dos_vendedores = df_dia_1.groupby(["Nome"]).sum()

relatorio = lucro_dos_vendedores.loc[:,"Valor"]

print(relatorio)

relatorio.plot(kind = 'bar')
plt.show()
'''
