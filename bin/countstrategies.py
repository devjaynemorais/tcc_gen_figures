# -*- coding: utf-8 -*-
import sys
import pandas as pd
from importlib import reload

reload(sys)

# Classe que contem todas as estrategias
# de contagem de acertos
class EstrategiasDeContagem:

    def __init__(self):
        self.pond_df = pd.read_csv(
            'data/medidas_ponderadas.csv', encoding='utf-8', sep=',')
        self.pond_df = self.pond_df.set_index('PA')

        self.pts_articulacao = {}
        self.pts_articulacao['1-Quadril-EN'] = 'Espaco neutro do Quadril'
        self.pts_articulacao['2-Quadril'] = 'Quadril'
        self.pts_articulacao['3-Quadril-E'] = 'E Quadril'
        self.pts_articulacao['4-Quadril-D'] = 'D Quadril'

        self.pts_articulacao['5-Estomago-EN'] = 'Espaco neutro do Estomago'
        self.pts_articulacao['6-Estomago'] = 'Estomago'
        self.pts_articulacao['7-Estomago-E'] = 'E Estomago'
        self.pts_articulacao['8-Estomago-D'] = 'D Estomago'

        self.pts_articulacao['9-Peito-EN'] = 'Espaco neutro do Peito'
        self.pts_articulacao['10-Peito'] = 'Peito'
        self.pts_articulacao['11-Peito-E'] = 'E Peito'
        self.pts_articulacao['12-Peito-D'] = 'D Peito'

        self.pts_articulacao['13-Pescoco-EN'] = 'Espaco neutro do Pescoco'
        self.pts_articulacao['14-Pescoco'] = 'Pescoco'
        self.pts_articulacao['15-Ombro-E'] = 'E Ombro'
        self.pts_articulacao['16-Ombro-D'] = 'D Ombro'

        self.pts_articulacao['17-Cabeca-EN'] = 'Espaco neutro da Cabeca'
        self.pts_articulacao['18-Cabeca'] = 'Cabeca'
        self.pts_articulacao['19-Cabeca-E'] = 'E Cabeca'
        self.pts_articulacao['20-Cabeca-D'] = 'D da Cabeca'

        self.pts_articulacao['21-Acima-Cabeca'] = 'Acima da Cabeca'

        self.pts_articulacao_inverse = {}

        self.pts_articulacao_inverse['1-Quadril-EN'] = 'Espaco neutro do Quadril'
        self.pts_articulacao_inverse['2-Quadril'] = 'Quadril'
        self.pts_articulacao_inverse['3-Quadril-E'] = 'D Quadril'
        self.pts_articulacao_inverse['4-Quadril-D'] = 'E Quadril'

        self.pts_articulacao_inverse['5-Estomago-EN'] = 'Espaco neutro do Estomago'
        self.pts_articulacao_inverse['6-Estomago'] = 'Estomago'
        self.pts_articulacao_inverse['7-Estomago-E'] = 'D Estomago'
        self.pts_articulacao_inverse['8-Estomago-D'] = 'E Estomago'

        self.pts_articulacao_inverse['9-Peito-EN'] = 'Espaco neutro do Peito'
        self.pts_articulacao_inverse['10-Peito'] = 'Peito'
        self.pts_articulacao_inverse['11-Peito-E'] = 'D Peito'
        self.pts_articulacao_inverse['12-Peito-D'] = 'E Peito'

        self.pts_articulacao_inverse['13-Pescoco-EN'] = 'Espaco neutro do Pescoco'
        self.pts_articulacao_inverse['14-Pescoco'] = 'Pescoco'
        self.pts_articulacao_inverse['15-Ombro-E'] = 'D Ombro'
        self.pts_articulacao_inverse['16-Ombro-D'] = 'E Ombro'

        self.pts_articulacao_inverse['17-Cabeca-EN'] = 'Espaco neutro da Cabeca'
        self.pts_articulacao_inverse['18-Cabeca'] = 'Cabeca'
        self.pts_articulacao_inverse['19-Cabeca-E'] = 'D Cabeca'
        self.pts_articulacao_inverse['20-Cabeca-D'] = 'E da Cabeca'

        self.pts_articulacao_inverse['21-Acima-Cabeca'] = 'Acima da Cabeca'

    # Estrategia baseada em condicionais para contagem de acertos
    def todos(self, dataframe, args):
            m_direita = str(args[0])
            m_esquerda = str(args[1])
            ponto_articulacao = str(args[2])
            movimento = str(args[3])
            nome = str(args[4])

            if(movimento == 'Ambas'):
                if((m_direita == self.pts_articulacao[ponto_articulacao]) and (m_esquerda == self.pts_articulacao[ponto_articulacao])):
                    return 1
                elif ((m_direita == self.pts_articulacao_inverse[ponto_articulacao]) and (m_esquerda == self.pts_articulacao_inverse[ponto_articulacao])):
                    return 1
                elif(m_direita == 'nan' or m_direita == 'FALHOU') or (m_esquerda == 'nan' or m_esquerda == 'FALHOU'):
                    return 3
                else:
                    return 0
            elif(movimento == 'Mao Esquerda'):
                if (m_esquerda == self.pts_articulacao[ponto_articulacao]):
                    return 1
                elif (m_esquerda == self.pts_articulacao_inverse[ponto_articulacao]):
                    return 1
                elif(m_esquerda == 'nan' or m_esquerda == 'FALHOU'):
                    return 3
                else:
                    return 0
            elif(movimento == 'Mao Direita'):
                if(m_direita == self.pts_articulacao[ponto_articulacao]):
                    return 1
                elif (m_direita == self.pts_articulacao_inverse[ponto_articulacao]):
                    return 1

                elif(m_direita == 'nan' or m_direita == 'FALHOU'):
                    return 3
                else:
                    return 0
            else:
                return 4

    def ponderado(self, dataframe, args):
        m_direita = str(args[0])
        m_esquerda = str(args[1])
        ponto_articulacao = str(args[2])
        movimento = str(args[3])
        nome = str(args[4])

        if (movimento == 'Mao Esquerda'):
            if (m_esquerda != 'FALHOU'):
                return self.pond_df.loc[ponto_articulacao][m_esquerda]


        if (movimento == 'Mao Direita'):
            if (m_direita != 'FALHOU'):
                return self.pond_df.loc[ponto_articulacao][m_direita] 
            

        if (movimento == 'Ambas'):
            if (m_direita != 'FALHOU' and m_esquerda != 'FALHOU'):
                resultado_soma =  (self.pond_df.loc[ponto_articulacao][m_esquerda] + self.pond_df.loc[ponto_articulacao][m_direita])
                if (resultado_soma != 0): return resultado_soma / 2
                return 0

            