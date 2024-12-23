# Instalação 
Para utilizar o Oddity, basta compilar o arquivo principal *index.py*, utilizando o comando "python" e seguir as instruções na tela.

```sh
cd pasta_principal_do_projeto
python index.py
```

Oddity é feita com base na framework [Dash](https://dash.plot.ly/), que funciona em cima do [Flask](http://flask.pocoo.org/). Portanto o processo de Deployment é extremamente parecido, checar os links:
* https://dash.plot.ly/deployment
* http://flask.pocoo.org/docs/0.12/deploying/

# Utilização
O Oddity tem duas ferramentas principais: os boxplots e os scatterplots.

**Para ambos os casos, o usuário pode clicar num ponto do gráfico para analisar.**

Em ambas as ferramentas, é possível que o usuário clique nos grupos criados ao lado direito do gráfico para filtrar a visualização. Também é possível passar o mouse pelo gráfico e checar as possibilidades no canto superior direito do gráfico (zoom, seleção, etc). 

#### Checar instruções de entrada na home page do Oddity!

## Boxplots
Boxplots são diagramas de caixa. Para mais informações a respeito de diagramas de caixa em si, checar o [link](https://pt.wikipedia.org/wiki/Diagrama_de_caixa).

Quanto a utilização de boxplots pelo Oddity, são criadas ***n*** caixas para ***n*** clusters na base de dados (checar instruções de entrada na home page do Oddity).

## Scatterplots
Scatterplots são gráficos de dispersão. Para mais informações a respeito de gráficos de dispersão em si, checar o [link](https://pt.wikipedia.org/wiki/Gr%C3%A1fico_de_dispers%C3%A3o).

Quanto a utilização de scatterplots pelo Oddity, é criado um scatterplot que separa por cores cada cluster contido na base de dados. Os dados que foram rotulados por anomalias também são destacados, em **vermelho**.