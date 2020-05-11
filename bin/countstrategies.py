# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Classe que contem todas as estrategias
# de contagem de acertos
class EstrategiasDeContagem:
    # Estrategia baseada em condicionais para contagem de acertos
    def todos(self, dataframe, args):
            pts_articulacao = {}
            pts_articulacao['1-Quadril-EN'] = 'Espaco neutro do Quadril'
            pts_articulacao['2-Quadril'] = 'Quadril'
            pts_articulacao['3-Quadril-E'] = 'E Quadril'
            pts_articulacao['4-Quadril-D'] = 'D Quadril'

            pts_articulacao['5-Estomago-EN'] = 'Espaco neutro do Estomago'
            pts_articulacao['6-Estomago'] = 'Estomago'
            pts_articulacao['7-Estomago-E'] = 'E Estomago'
            pts_articulacao['8-Estomago-D'] = 'D Estomago'

            pts_articulacao['9-Peito-EN'] = 'Espaco neutro do Peito'
            pts_articulacao['10-Peito'] = 'Peito'
            pts_articulacao['11-Peito-E'] = 'E Peito'
            pts_articulacao['12-Peito-D'] = 'D Peito'

            pts_articulacao['13-Pescoco-EN'] = 'Espaco neutro do Pescoco'
            pts_articulacao['14-Pescoco'] = 'Pescoco'
            pts_articulacao['15-Ombro-E'] = 'E Ombro'
            pts_articulacao['16-Ombro-D'] = 'D Ombro'

            pts_articulacao['17-Cabeca-EN'] = 'Espaco neutro da Cabeca'
            pts_articulacao['18-Cabeca'] = 'Cabeca'
            pts_articulacao['19-Cabeca-E'] = 'E Cabeca'
            pts_articulacao['20-Cabeca-D'] = 'D da Cabeca'

            pts_articulacao['21-Acima-Cabeca'] = 'Acima da Cabeca'

            pts_articulacao_inverse = {}

            pts_articulacao_inverse['1-Quadril-EN'] = 'Espaco neutro do Quadril'
            pts_articulacao_inverse['2-Quadril'] = 'Quadril'
            pts_articulacao_inverse['3-Quadril-E'] = 'D Quadril'
            pts_articulacao_inverse['4-Quadril-D'] = 'E Quadril'

            pts_articulacao_inverse['5-Estomago-EN'] = 'Espaco neutro do Estomago'
            pts_articulacao_inverse['6-Estomago'] = 'Estomago'
            pts_articulacao_inverse['7-Estomago-E'] = 'D Estomago'
            pts_articulacao_inverse['8-Estomago-D'] = 'E Estomago'

            pts_articulacao_inverse['9-Peito-EN'] = 'Espaco neutro do Peito'
            pts_articulacao_inverse['10-Peito'] = 'Peito'
            pts_articulacao_inverse['11-Peito-E'] = 'D Peito'
            pts_articulacao_inverse['12-Peito-D'] = 'E Peito'

            pts_articulacao_inverse['13-Pescoco-EN'] = 'Espaco neutro do Pescoco'
            pts_articulacao_inverse['14-Pescoco'] = 'Pescoco'
            pts_articulacao_inverse['15-Ombro-E'] = 'D Ombro'
            pts_articulacao_inverse['16-Ombro-D'] = 'E Ombro'

            pts_articulacao_inverse['17-Cabeca-EN'] = 'Espaco neutro da Cabeca'
            pts_articulacao_inverse['18-Cabeca'] = 'Cabeca'
            pts_articulacao_inverse['19-Cabeca-E'] = 'D Cabeca'
            pts_articulacao_inverse['20-Cabeca-D'] = 'E da Cabeca'

            pts_articulacao_inverse['21-Acima-Cabeca'] = 'Acima da Cabeca'

            m_direita = str(args[0])
            m_esquerda = str(args[1])
            ponto_articulacao = str(args[2])
            movimento = str(args[3])
            nome = str(args[4])

            if(movimento == 'Ambas'):
                if((m_direita == pts_articulacao[ponto_articulacao]) and (m_esquerda == pts_articulacao[ponto_articulacao])):
                    return 1
                elif ((m_direita == pts_articulacao_inverse[ponto_articulacao]) and (m_esquerda == pts_articulacao_inverse[ponto_articulacao])):
                    return 1
                elif(m_direita == 'nan' or m_direita == 'FALHOU') or (m_esquerda == 'nan' or m_esquerda == 'FALHOU'):
                    return 3
                else:
                    return 0
            elif(movimento == 'Mao Esquerda'):
                if (m_esquerda == pts_articulacao[ponto_articulacao]):
                    return 1
                elif (m_esquerda == pts_articulacao_inverse[ponto_articulacao]):
                    return 1
                elif(m_esquerda == 'nan' or m_esquerda == 'FALHOU'):
                    return 3
                else:
                    return 0
            elif(movimento == 'Mao Direita'):
                if(m_direita == pts_articulacao[ponto_articulacao]):
                    return 1
                elif (m_direita == pts_articulacao_inverse[ponto_articulacao]):
                    return 1
                
                elif(m_direita == 'nan' or m_direita == 'FALHOU'):
                    return 3
                else:
                    return 0
            else:
                return 4

    def resultado(self, dataframe, args):   
        resultado = args[0]
        return resultado