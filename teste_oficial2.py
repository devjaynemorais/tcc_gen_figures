# -*- coding: utf-8 -*-
import os 
import pandas as pd 
import numpy as np
import csv
# import matplotlib.pyplot as plt	


print "############## Iniciando Testes ##############"
folder = "~/Documentos/TCC/Testes/"

colunas = ['tempo', 'm_direita', 'm_esquerda', 'movimento', 'ponto_articulacao', 'classificacao_imc', 'nome_individuo', 'altura', 'peso', 'data_criacao', 'nao_sei']
dataFrame = pd.read_csv(folder+"teste_geral.csv", encoding = 'utf-8', sep = ';', names=colunas) #, header=0


pts_articulacao = {}
pts_articulacao['1-Quadril-EN']		= 'Espaco neutro do Quadril'
pts_articulacao['2-Quadril']		= 'Quadril'
pts_articulacao['3-Quadril-E']		= 'E Quadril'
pts_articulacao['4-Quadril-D']		= 'D Quadril'

pts_articulacao['5-Estomago-EN'] 	= 'Espaco neutro do Estomago'
pts_articulacao['6-Estomago']	 	= 'Estomago'
pts_articulacao['7-Estomago-E']	 	= 'E Estomago'
pts_articulacao['8-Estomago-D']	 	= 'D Estomago'

pts_articulacao['9-Peito-EN']	    = 'Espaco neutro do Peito'
pts_articulacao['10-Peito']	        = 'Peito'
pts_articulacao['11-Peito-E']	    = 'E Peito'
pts_articulacao['12-Peito-D']	    = 'D Peito'

pts_articulacao['13-Pescoco-EN']	= 'Espaco neutro do Pescoco'
pts_articulacao['14-Pescoco']	    = 'Pescoco'
pts_articulacao['15-Ombro-E']	    = 'E Ombro'
pts_articulacao['16-Ombro-D']	    = 'D Ombro'

pts_articulacao['17-Cabeca-EN']	    = 'Espaco neutro da Cabeca'
pts_articulacao['18-Cabeca']	    = 'Cabeca'
pts_articulacao['19-Cabeca-E']	    = 'E Cabeca'
pts_articulacao['20-Cabeca-D']	    = 'D Cabeca'

pts_articulacao['21-Acima-Cabeca']	= 'Acima da Cabeca'


def calcular_acerto(a):
	m_direita = str(a[0])
	m_esquerda = str(a[1])
	ponto_articulacao = str(a[2])
	movimento = str(a[3])

	# print str(m_direita) + ' X ' + str(pts_articulacao[ponto_articulacao])

	if(movimento == 'Ambas'):
		if(((m_direita) and (m_direita == pts_articulacao[ponto_articulacao])) and ((m_esquerda) and ( m_esquerda == pts_articulacao[ponto_articulacao]) )):
			return 1
		elif ( (m_direita) and  (m_direita != pts_articulacao[ponto_articulacao]) or ((m_esquerda) and (m_esquerda != pts_articulacao[ponto_articulacao]) )):
			return 0
		elif((m_direita is None) and (m_esquerda is None)):
			return 3
	elif(movimento == 'Mao Esquerda'):
		if ((m_esquerda) and ( m_esquerda == pts_articulacao[ponto_articulacao])):
			return 1
		elif (m_esquerda) and ( m_esquerda != pts_articulacao[ponto_articulacao]):
			return 0
		elif(m_esquerda is None):
			return 3
	elif(movimento == 'Mao Direita'):
		if((m_direita) and (m_direita == pts_articulacao[ponto_articulacao])):
			return 1
		elif ((m_direita) and (m_direita != pts_articulacao[ponto_articulacao])):
			return 0
		elif(m_direita is None):
			return 3
	else:
		return 4

	




dataFrame['resultado'] = dataFrame[['m_direita', 'm_esquerda', 'ponto_articulacao', 'movimento']].apply(calcular_acerto, axis=1)

# print dataFrame.head(2000)
# print acerto, erro


print(dataFrame.resultado.value_counts())

# print dataFrame.resultado.describe()
# .apply(lambda x: 100 * x / float(x.sum())
data_agrupado  = dataFrame.pivot_table( index=["movimento","ponto_articulacao"], aggfunc=np.sum)
print(data_agrupado['resultado'])
data_agrupado.to_csv('vamos_analisar.csv', encoding='utf-8', index=True, sep=';')