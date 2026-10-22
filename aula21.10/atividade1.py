import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

try:
    print('Obtendo dados . . .')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_cvli = df_ocorrencias[['aisp', 'cvli']]
    df_cvli = df_cvli.groupby('aisp', as_index=False)['cvli'].sum()


except Exception as e:
    print(f'Erro ao obter os dados - {e}')

try:
    print('Organizando os dados . . .')
    df_cvli = df_cvli.sort_values(
        by='cvli',
        ascending=False
    )
    print(df_cvli)   
except Exception as e:
    print(f'Erro ao obter os dados - {e}')

try:
    print('Determinando os dados . . .')
    array_cvli = np.array(df_cvli['cvli'])
    media_cvli = np.mean(array_cvli)
    mediana_cvli = np.median(array_cvli)
    distancia = abs (
        media_cvli - mediana_cvli / mediana_cvli * 100
    )

    q1 = np.quantile(array_cvli, .25)
    q2 = np.quantile(array_cvli, .50)
    q3 = np.quantile(array_cvli, .75)

    max = np.max(array_cvli)
    min = np.min(array_cvli)
    amplitude = max - min

    variancia = np.var(array_cvli)
    distancia_variancia = variancia / (media_cvli**2) *100

    desvio_padrao = np.std(array_cvli)
    
    coef_variacao = (desvio_padrao / media_cvli) * 100

    iqr = q3 - q1

    limite_sup = q3 + (1.5*iqr)
    limite_inf = q1 - (1.5*iqr)
except Exception as e:
    print(f'Erro ao obter os dados - {e}')

try:
    print('Exibindo valores . . .')
    print('MOSTRANDO VALORES')
    print()
    print(f'''
Mínimo: {min}
Máximo: {max}

Limite inferior: {limite_inf}

Q1: {q1}
Q2: {q2}
Q3: {q3}

Limite superior: {limite_sup}

MEDIDAS DE TENDÊNCIA CENTRAL

Média: {media_cvli}]
Mediana: {mediana_cvli}

    ''')