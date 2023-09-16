import pandas
import numpy
import matplotlib.pyplot as mpl

jogos = pandas.read_csv('./vgsales.csv')
jogo_limitado = jogos.head(400)
filtro = jogo_limitado[(jogo_limitado['Platform']  == 'Wii') & (jogo_limitado['Genre'] == 'Platform') & (jogo_limitado['Publisher'] == 'Nintendo')]
print(filtro)

left_coordinates=[1,2,3,4,5]
heights=[11.52, 3.76, 28.62, 6.59, 6.59]
bar_labels=['Super Mario Galaxy','Super Paper Mario','New Super Mario Bros. Wii','Donkey Kong Country Returns','Super Mario Galaxy']
mpl.bar(left_coordinates,heights,tick_label=bar_labels,width=0.6,color=['red','black'])
mpl.xlabel('Ano de Lançamento')
mpl.ylabel('Vendas em Milhões')
mpl.title("Informações do jogos")
mpl.show()
