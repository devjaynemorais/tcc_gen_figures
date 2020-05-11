# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import math
import argparse
from dataprocess import ProcessoDeDados
from countstrategies import EstrategiasDeContagem
from porcentagens import RotinasPorcentagem

# configura um dataframe e retorna
def construirDataFrame(csvPath, colunas):
	# Configuração das colunas e dataFrame
	# ------------------------------------------------------
	dataFrame = pd.read_csv(csvPath, encoding='utf-8', sep=';', names=colunas)
	return dataFrame

def analisePrimaria():
	estrategias = EstrategiasDeContagem()
	dataFrame = construirDataFrame('data/teste_geral.csv', colunas=['tempo', 'm_direita', 'm_esquerda', 'movimento', 'ponto_articulacao', 'classificacao_imc',
                                               'nome_individuo', 'predominancia', 'altura', 'peso', 'data_criacao', 'nao_sei'])

	data = ProcessoDeDados(dataFrame)
	data.configurarEstrategia(estrategias.todos)

	data.calcular(['m_direita', 'm_esquerda', 'ponto_articulacao', 'movimento', 'nome_individuo'])
	data.mostrarResultado(numberOfRows=50000)

	data.salvarResultado('logs/output.csv')


def analiseSecundaria():
	estrategias = EstrategiasDeContagem()
	dataFrame = construirDataFrame('logs/output.csv', colunas=['tempo', 'm_direita', 'm_esquerda', 'movimento', 'ponto_articulacao', 'classificacao_imc',
                                               'nome_individuo', 'predominancia', 'altura', 'peso', 'data_criacao', 'nao_sei', 'resultado'])

	porcentagem = RotinasPorcentagem(dataFrame)


	# porcentagem.pior()
	porcentagem.movimentoGeral()
	porcentagem.paGeral()
	porcentagem.imcGeral()
	porcentagem.reconhecimentoGeral()
	porcentagem.tempoAcertos()
	porcentagem.posicaoGeral()
	porcentagem.corpoGeral()
	porcentagem.paDescibes()


# Encapsula a inicialização do script
# Utilização do Script:
#
# teste_oficial2.py -i || --input path/to/csv
#
if __name__ == "__main__":
	mainFunc = analisePrimaria
	funcMap = {
		'primaria': analisePrimaria,
		'secundaria': analiseSecundaria
	}

	# Configura os argumentos do script
	parser = argparse.ArgumentParser(description='Analise de dados.')
	parser.add_argument(
		"-t", "--tipo", help="Tipo de dado a ser analisado, com o sem resultado")

	args = parser.parse_args()

	# Verifica se foi passado um argumento
	# referente ao caminho do arquivo e referente
	# a qual função utilizar
	# ------------------------------------------------------
	if (args.tipo):
		mainFunc = funcMap[args.tipo]
	# -------------------------------------------------------

	print "\033"
	print "############## Inicializando os Testes ##############"
	print "\n"

	mainFunc()

	# print dataFrame.resultado.describe()


# tipo de movimento | IMC |  PA |  MAO DIR | mao  esq | Qt acerto | Qt erro | porcentagem de acerto
# agrupado por tipo de movimento, imc e PA
