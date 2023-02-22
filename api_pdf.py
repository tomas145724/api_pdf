# Libs necessarias
import os

# Pacotes analise de dados
import pandas_datareader.data as web
import pandas as pd
import numpy as np

# Analises gráficos
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Função para data
from datetime import datetime

# YFiance
import yfinance as yf
yf.pdr_override()

# Avisos
import warnings
warnings.filterwarnings('ignore')

# Coletando os dados
Dados = web.get_data_yahoo( 'AMER3.SA', period='1y' )

# Shape
Dados.shape


# Verificando
    #Dados.head()
# Ultimos registros
    #Dados.tail()
# Estatistica descritiva
    #Dados.describe()
# Informações
    #Dados.info()


def preco_fechamento():
    # Plot
    plt.plot(Dados['Close'])
    plt.title('Preço Fechamento');
    plt.show()


#Função rolling
"""A função rolling() é uma função do pandas que permite calcular estatísticas em janelas deslizantes de dados.
Ela é muito útil para calcular médias móveis, desvios padrão, somatórios, mínimos e máximos, entre outras estatísticas.
"""
def rolling():
    from pandas.core import window
    Periodo = 5
    Dados['Close'].rolling(window=Periodo).mean()

    # Tamanho da imagem
    plt.figure(figsize=(12, 6))

    plt.plot(Dados['Close'])
    plt.plot(Dados['Close'].rolling(window=Periodo).mean())
    plt.plot(Dados['Close'].rolling(window=Periodo + 20).mean())
    plt.title('Preço Fechamento')
    plt.legend(['Close', 'Media 5 dias', 'Media 25 dias'])
    plt.ylabel('Valor de Fechamento')
    plt.xlabel('Periodo');
    plt.show()


#PLOTLY
"""O PLOTLY é uma biblioteca Python de plotagem interativa e de código aberto que oferece suporte a mais de 40 tipos de gráficos exclusivos, 
abrangendo uma ampla variedade de casos de uso estatísticos, financeiros, geográficos, científicos e tridimensionais.
plotly.express (px) é uma maneira rápida e fácil de criar visualizações dinâmicas de dados.
plotly.graph_objects (go) é a API de nível inferior que concede mais controle sobre suas visualizações, mas é mais intensiva em código.
"""
def fechamento():
    Periodo = 5
    Dados['Media_Movel'] = Dados['Close'].rolling(window=Periodo).mean()

    Figure = px.line(
        Dados,
        y='Close',
        title='Fechamento'
    )

    #Figure.show()
def analise_fechamento():
    Figure_02 = go.Figure(
        data=go.Scatter(
            x=Dados.index,
            y=Dados['Close'],
            line=(dict(color='firebrick', width=3))
        )
    )

    Figure_02.update_layout(
        title='Análise de Fechamento',
        xaxis_title='Periodo',
        yaxis_title='Preço de fechamento'
    )

    Figure_02.show()


#Candlestick Charts
""" É um estilo de gráfico financeiro que descreve abertura, alta, baixa e fechamento para uma determinada xcoordenada (tempo mais provável). As caixas representam 
 a dispersão entre os valores opene closee as linhas representam a dispersão entre os valores lowe high. Pontos de amostragem onde o valor de fechamento é maior (inferior) do que o valor de
 abertura são chamados de crescentes (decrescentes). Por padrão, as velas crescentes são desenhadas em verde, enquanto as decrescentes são desenhadas em vermelho.
"""
def candlestick():

    # Grafico clandestik
    Grafico_Candlestick = go.Figure(
        data=[
            go.Candlestick(
                x=Dados.index,
                open=Dados['Open'],
                high=Dados['High'],
                low=Dados['Low'],
                close=Dados['Close']
                #mudar a cor das velas
                #increasing_line_color='cyan',
                #decreasing_line_color='gray'
            )
        ]
    )

    Grafico_Candlestick.update_layout(
        xaxis_rangeslider_visible=False,
        title='Análise Fechamento',
        xaxis_title='Periodo',
        yaxis_title='Preço de Fechamento'
    )

    Grafico_Candlestick.show()



fechamento()
#Criação do Relatorio
def relatorio():
    # Criar a Figura
    Figura = make_subplots(
        rows=2,
        cols=1,
        specs=[
            [{'type': 'scatter'}],
            [{'type': 'scatter'}]
        ],
        vertical_spacing=0.075,
        shared_xaxes=True,
        subplot_titles=('Cotação', 'Fechamento')
    )

    # Layout e Dimensão
    Figura.update_layout(
        width=1000,
        height=800,
        title_text='<b>Analise Avançada</b> <br>Follow-up Americanas'
    )

    # Adicionado um gráfico na 1º Posição
    Figura.add_trace(
        go.Candlestick(
            x=Dados.index,
            open=Dados['Open'],
            high=Dados['High'],
            low=Dados['Low'],
            close=Dados['Close']
        ),
        row=1, col=1
    )

    Figura.add_trace(
        go.Scatter(
            x=Dados.index,
            y=Dados['Media_Movel'],
            mode='lines',
            name='Média Móvel',
            line=dict(color='yellow')
        ),
        row=1, col=1
    )

    Figura.update_layout(
        xaxis_rangeslider_visible=False
    )

    # Adicionado um gráfico na 2º Posição
    Figura.add_trace(
        go.Scatter(
            x=Dados.index,
            y=Dados['Close'],
            mode='lines',
            name='Fechamento',
            line=dict(color='green')
        ),
        row=2, col=1
    )

    Figura.add_trace(
        go.Scatter(
            x=Dados.index,
            y=Dados['Media_Movel'],
            mode='lines',
            name='Média Móvel',
            line=dict(color='red')
        ),
        row=2, col=1
    )

    Figura.update_layout(
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            font=dict(size=10)
        )
    )

    Figura.add_annotation(
        showarrow=False,
        text='Análise feita no evento de Python',
        font=dict(size=14),
        xref='x domain',
        x=1,
        yref='y domain',
        y=-1.4
    )

    Figura.add_annotation(
        showarrow=False,
        text='By: Thomaz Lima',
        font=dict(size=14),
        xref='x domain',
        x=0,
        yref='y domain',
        y=-1.4
    )

    Figura.show()

    # Kaleido
    """Kaleido é uma biblioteca de plataforma cruzada para geração de imagens estáticas (por exemplo, png, svg, pdf,
    etc.) para bibliotecas de visualização baseadas na web, com foco particular na eliminação de dependências
    externas. O foco inicial do projeto é a exportação de imagens plotly.js do Python para uso por plotly.py,
    mas ele foi projetado para ser relativamente direto para estender a outras bibliotecas de visualização
    baseadas na web e outras linguagens de programação. O foco principal do Kaleido (pelo menos inicialmente)
    é servir como uma dependência de bibliotecas de visualização baseadas na web, como plotly.py. Como tal, o
    foco está em fornecer uma API programática, em vez de amigável ao usuário."""

    Figura.write_image('Report_Fiananceiro.pdf')
relatorio()






