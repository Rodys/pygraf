from cProfile import label
from tokenize import Number
from turtle import width
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import datetime 

#pegando o nome da planilha, não precisa do endereço por estar na mesma página
arquivo_excel = "Dia01.xlsx"
arquivo_excel_exon = "cttos_exonerados.xlsx"

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
explode = (0, 0.1) #variação da peça da pizza

#Parte para a criação do gráfico

fig1, ax1 = plt.subplots()

ax1.pie(sizes_pie, explode=explode, labels = label_pie, autopct='%1.1f%%', shadow=True, startangle=50)
ax1.axis('equal')
plt.show()

#trabalhando com as contagens de exonerações por ano

df_data = df_exon_tratada['dt_exoneracao'].dt.year
print(df_data)
df_exon_tratada.insert(10,"ano_exo",df_data, True)

#trabalhando com os anos e fazendo as contagens de contrato
list_bar = ['2019','2020','2021','2022']
x = np.arange(4)
cont_ano = []

ano_2019 = df_exon_tratada[df_exon_tratada['ano_exo'] == 2019].count()[0]
ano_2020 = df_exon_tratada[df_exon_tratada['ano_exo'] == 2020].count()[0]
ano_2021 = df_exon_tratada[df_exon_tratada['ano_exo'] == 2021].count()[0]
ano_2022 = df_exon_tratada[df_exon_tratada['ano_exo'] == 2022].count()[0]
cont_ano= [ano_2019, ano_2020, ano_2021, ano_2022]

print(list_bar)
print(cont_ano)
print(x)

#plotando o gráfico de barras do número de contratos por ano
fig, ax = plt.subplots()

p1 = ax.bar(x, cont_ano)
ax.set_xticks(x,list_bar)
ax.set_xlabel("Anos")
ax.set_ylabel("N° de exonerações")
ax.bar_label(p1, label_type='edge')

plt.show()

'''
#criando o arquivo df_exon_tratada.to_excel("cttos_exon_trat.xlsx")


lucro_dos_vendedores = df_dia_1.groupby(["Nome"]).sum()

relatorio = lucro_dos_vendedores.loc[:,"Valor"]

print(relatorio)

relatorio.plot(kind = 'bar')
plt.show()
'''
