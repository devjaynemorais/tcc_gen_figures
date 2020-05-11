# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
import numpy as np
import csv
import math
# import matplotlib.pyplot as plt

# Classe de testes


class ProcessoDeDados:
	def __init__(self, dataframe):
		self.dataframe = dataframe

	# Aplica o callback determinado em setCountStrategy
	# para calcular os acertos do dataFrame.
	def calcular(self, columns):
		self.dataframe['resultado'] = self.dataframe[columns].apply(
		    self._calculateCb, axis=1)
		self.dataframe = self.dataframe[self.dataframe.resultado != 3]

	# Exibe o resultado do processamento do
	# dataframe
	def mostrarResultado(self, numberOfRows):
		""" Show the result of dataframe processing """

		print self.dataframe.head(numberOfRows)
		print self.dataframe.resultado.value_counts()

	# Salva o dataframe processado em um arquivo
	def salvarResultado(self, nomeArquivoDeSaida):
		""" Salva o resultado em um arquivo

			Argumentos:
				nomeArquivoDeSaida -- Nome para o arquivo de saida.
		 """

		self.dataframe.to_csv(nomeArquivoDeSaida,
		                      encoding='utf-8', index=True, sep=';')

	# Define a estrategia para contagem
	def configurarEstrategia(self, strategy):
		self.strategy = strategy

	# --------------------------------------------
	# Private Methods
	# --------------------------------------------
	def _calculateCb(self, args):
		""" Retorna 0 ou 1 baseado nas colunas e estrategia configuradas"""

		result = self.strategy(self.dataframe, args)

		return result


if __name__ == '__main__':
	print 'Tester'
