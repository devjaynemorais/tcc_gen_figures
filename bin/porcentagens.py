# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
import matplotlib


matplotlib.rc('font', family='Arial')


class RotinasPorcentagem:
    def __init__(self, dataframe):
        self.df = dataframe.iloc[1:]
        self.df["resultado"] = pd.to_numeric(self.df["resultado"])
        self.colors = ['#27ae60', '#e74c3c', '#3498db', '#3498db']
        self.explode = (0.05, 0.05)
        folders = ['imc_geral', 'movimento_geral', 'pa_geral',
                   'reconhecimento_geral', 'tempo_acertos', 'corpo_geral', 'posicao_geral']
        folderPrefix = 'graficos/'
        if not os.path.exists('csv'):
                os.makedirs('csv')
        if not os.path.exists('graficos'):
                os.makedirs('graficos')
        for folder in folders:
            if not os.path.exists(folderPrefix + folder):
                os.makedirs(folderPrefix + folder)

        self._cortarItervalor()

    def _cortarItervalor(self):
        prefixInicial = '00:00:'
        prefixFinal = '00:05:'

        for i in range(1, 30):
            if (i < 10):
                temp = '0' + str(i)
            else:
                temp = str(i)

            self.df = self.df[self.df.tempo != prefixInicial + temp]

        for i in range(31, 100):
            temp = prefixFinal + str(i)

            self.df = self.df[self.df.tempo != temp]
            
    def movimentoGeral(self):
        listaDeMovimentos = ['Ambas', 'Mao Direita', 'Mao Esquerda']
        movimentos = self.df[['movimento', 'resultado']]
        movimentos = movimentos.iloc[1:]

        movimentos["resultado"] = pd.to_numeric(movimentos["resultado"])

        grupo = pd.DataFrame({})

        for x in listaDeMovimentos:
            movimento = movimentos[(movimentos.movimento == x)]
            movimento_porcentagem = pd.DataFrame({'Acertos': (
                movimento.groupby(('resultado')).size() / len(movimento)) * 100})

            grupo = grupo.append(movimento_porcentagem)

        grupo.fillna(0, inplace=True)
        grupo.reset_index(inplace=True)
        grupo = grupo[(grupo.resultado == 1)]
        grupo = grupo.drop(columns='resultado')

        grafico = grupo.plot(
            kind="bar", colors=self.colors, ylim=(0, 100), rot=0)
        grafico.set_xticklabels(listaDeMovimentos)
        grafico.set_ylabel('Porcentagem')

        for p in grafico.patches:
            grafico.annotate(str(round(p.get_height(), 2)) +
                             '%', (p.get_x() + 0.100, p.get_height() * 1.050))

        plt.title('Movimento')
        plt.tight_layout()
        plt.savefig('graficos/movimento_geral/movimento.png')

    def paGeral(self):
        print self.df

        pa_strings = {}
        pa_strings['1-Quadril-EN'] = 'Espaço neutro do Quadril'
        pa_strings['2-Quadril'] = 'Quadril'
        pa_strings['3-Quadril-E'] = 'Esquerda do Quadril'
        pa_strings['4-Quadril-D'] = 'Direita do Quadril'

        pa_strings['5-Estomago-EN'] = 'Espaço neutro do Estômago'
        pa_strings['6-Estomago'] = 'Estômago'
        pa_strings['7-Estomago-E'] = 'Esquerda do Estômago'
        pa_strings['8-Estomago-D'] = 'Direita do Estômago'

        pa_strings['9-Peito-EN'] = 'Espaço neutro do Peito'
        pa_strings['10-Peito'] = 'Peito'
        pa_strings['11-Peito-E'] = 'Esquerda do Peito'
        pa_strings['12-Peito-D'] = 'Direita do Peito'

        pa_strings['13-Pescoco-EN'] = 'Espaço neutro do Pescoço'
        pa_strings['14-Pescoco'] = 'Pescoco'
        pa_strings['15-Ombro-E'] = 'Esquerda do Ombro'
        pa_strings['16-Ombro-D'] = 'Direita do Ombro'

        pa_strings['17-Cabeca-EN'] = 'Espaço neutro da Cabeça'
        pa_strings['18-Cabeca'] = 'Cabeça'
        pa_strings['19-Cabeca-E'] = 'Equerda da Cabeça'
        pa_strings['20-Cabeca-D'] = 'Direita da Cabeça'

        pa_strings['21-Acima-Cabeca'] = 'Acima da Cabeca'

        listaDePas = ['1-Quadril-EN', '2-Quadril', '3-Quadril-E', '4-Quadril-D', '5-Estomago-EN',
                      '6-Estomago', '7-Estomago-E', '8-Estomago-D', '9-Peito-EN', '10-Peito', '11-Peito-E',
                      '12-Peito-D', '13-Pescoco-EN', '14-Pescoco', '15-Ombro-E', '16-Ombro-D', '17-Cabeca-EN',
                      '18-Cabeca', '19-Cabeca-E', '20-Cabeca-D', '21-Acima-Cabeca']

        pas = self.df[['ponto_articulacao', 'resultado']]
        pas = pas.iloc[1:]
        pas["resultado"] = pd.to_numeric(pas["resultado"])

        novo_pas = pd.DataFrame([])

        for x in listaDePas:
            pa = pas[(pas.ponto_articulacao == x)]
            pa_porcentagem = pd.DataFrame({'PA': pa_strings[x], 'Acertos': (
                pa.groupby(('resultado')).size() / len(pa)) * 100})
            novo_pas = novo_pas.append(pa_porcentagem)

        # novo_pas = novo_pas[(novo_pas.resultado == '1')]
        novo_pas = novo_pas.drop(novo_pas.index[[0]])

        grafico = novo_pas.plot(kind="barh", x='PA', alpha=0.75,
                                color=self.colors[2], rot=0, xlim=(0, 100))

        grafico.legend(loc='lower right')
        grafico.set_xlabel("Porcentagem")
        for i in grafico.patches:
           plt.text(i.get_width()+.1, i.get_y()+.05,
                    str(round((i.get_width()), 2)) + '%', fontsize=10, color='dimgrey')

        plt.tight_layout()
        plt.savefig('graficos/pa_geral/acertos.png', dpi=(150))

    def imcGeral(self):
        imc_strings = {
            'Saudavel': u'Normal',
            'Abaixo do Peso': 'Abaixo do Peso',
            'Sobrepeso': 'Sobrepeso',
            'Obesidade Grau II (severa)': 'Obesidade Grau II (severa)'
        }

        imcs = self.df[['classificacao_imc', 'resultado']]
        imcs = imcs.iloc[1:]
        imcs["resultado"] = pd.to_numeric(imcs["resultado"])

        grupo = pd.DataFrame({})

        for key, value in imc_strings.iteritems():
            imc = imcs[(imcs.classificacao_imc == key)]
            imc_porcentagem = pd.DataFrame({'Acertos': (
                imc.groupby(('resultado')).size() / len(imc)) * 100})
            grupo = grupo.append(imc_porcentagem)

        grupo.fillna(0, inplace=True)
        grupo.reset_index(inplace=True)
        grupo = grupo[(grupo.resultado == 1)]
        grupo = grupo.drop(columns='resultado')

        grafico = grupo.plot(
            kind="barh", colors=self.colors, xlim=(0, 100), rot=0)
        grafico.set_yticklabels(imc_strings.keys())
        grafico.set_xlabel('Porcentagem')

        for i in grafico.patches:
           plt.text(i.get_width()+.1, i.get_y()+.17,
                    str(round((i.get_width()), 2)) + '%', fontsize=10, color='dimgrey')

        plt.title('IMC')
        plt.tight_layout()
        plt.savefig('graficos/imc_geral/imc.png')

    def reconhecimentoGeral(self):

        reconhecimento = self.df.iloc[1:]
        reconhecimento['resultado'] = pd.to_numeric(
            reconhecimento['resultado'])
        reconhecimento['resultado'].value_counts()

        reconhecimento_porcentagem = pd.DataFrame({'Porcentagem': (
            reconhecimento['resultado'].value_counts() / len(reconhecimento['resultado'])) * 100})

        reconhecimento_porcentagem.plot(kind="pie", subplots=True, colors=self.colors, autopct='%1.1f%%', explode=(
            0.05, 0.05), labels=['Acertos', 'Erros'], startangle=90, radius=2)

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        plt.axis('equal')
        plt.title('Reconhecimento')
        plt.tight_layout()
        plt.savefig('graficos/reconhecimento_geral/geral.png')

    def tempoAcertos(self):
        tempoInMs = [
            '500ms', '1000ms', '1500ms', '2000ms', '2500ms', '3000ms', '3500ms', '4000ms',
            '4500ms', '5000ms', '5500ms'
        ]
        listaDeTempos = ['00:00:30', '00:01:00', '00:01:30', '00:02:00', '00:02:30',
                         '00:03:00', '00:03:30', '00:04:00', '00:04:30', '00:05:00', '00:05:30']
        temposAcertos = self.df[['tempo', 'resultado']]
        temposAcertos = temposAcertos.iloc[1:]
        temposAcertos['resultado'] = pd.to_numeric(temposAcertos['resultado'])
        temposAcertos = temposAcertos[(temposAcertos.resultado == 1)]

        grupo = pd.DataFrame([])

        for x in listaDeTempos:
            tempo = temposAcertos[(temposAcertos.tempo == x)]
            grupo = grupo.append(tempo)

        tempo_porcentagem = pd.DataFrame({'Acertos': (
            grupo.groupby(['tempo']).size() / len(grupo)) * 100})

        ax = tempo_porcentagem.plot(kind='line', rot=90)
        ax.set_xticks(range(len(listaDeTempos)))
        ax.set_xticklabels(tempoInMs)
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())

        plt.tight_layout()
        plt.savefig('graficos/tempo_acertos/tempo.png', dpi=(150))

    def posicaoGeral(self):
        secoes = {
            'Espaço Neutro': [
                '1-Quadril-EN',
                '5-Estomago-EN',
                '9-Peito-EN',
                '13-Pescoco-EN',
                '17-Cabeca-EN'
            ],
            'Direita': [
                '4-Quadril-D',
                '8-Estomago-D',
                '12-Peito-D',
                '16-Ombro-D',
                '20-Cabeca-D'
            ],
            'Esquerda': [
                '3-Quadril-E',
                '7-Estomago-E',
                '11-Peito-E',
                '15-Ombro-E',
                '19-Cabeca-E'
            ],
            'Em Contato': [
                '2-Quadril',
                '6-Estomago',
                '10-Peito',
                '14-Pescoco',
                '18-Cabeca'
            ],
            'Acima': ['21-Acima-Cabeca']
        }
        grupos = pd.DataFrame({})
        analisar = self.df[['resultado', 'ponto_articulacao']]

        for key, value in secoes.iteritems():
            analisando = analisar.loc[analisar['ponto_articulacao'].isin(
                value)]
            grupos = grupos.append(pd.DataFrame({'Posição': key, 'Acertos': (
                analisando.groupby(['resultado']).size() / len(analisando)) * 100}))

        grupos.fillna(0, inplace=True)
        grupos.reset_index(inplace=True)
        grupos = grupos[(grupos.resultado == 1)]
        grupos = grupos.drop(columns='resultado')
        grafico = grupos.plot(kind='bar',  rot=0,
                              colors=self.colors, ylim=(0, 100))

        for p in grafico.patches:
            grafico.annotate(str(round(p.get_height(), 2)) +
                             '%', (p.get_x() * 1.005, p.get_height() * 1.005))

        grafico.set_ylabel("Porcentagem")
        grafico.set_xticklabels(secoes.keys())
        plt.savefig('graficos/posicao_geral/posicao.png')

    def corpoGeral(self):
        corpo = {
            'Cabeça': ['17-Cabeca-EN', '18-Cabeca', '19-Cabeca-E', '20-Cabeca-D', '21-Acima-Cabeca'],
            'Quadril': ['1-Quadril-EN', '2-Quadril', '3-Quadril-E', '4-Quadril-D'],
            'Peito': ['9-Peito-EN', '10-Peito', '11-Peito-E', '12-Peito-D'],
            'Estomago': ['5-Estomago-EN', '6-Estomago', '7-Estomago-E', '8-Estomago-D'],
            'Pescoço': ['13-Pescoco-EN', '14-Pescoco'],
            'Ombro': ['15-Ombro-E', '16-Ombro-D']
        }

        corpoDf = self.df[['resultado', 'ponto_articulacao']]
        grupos = pd.DataFrame({})

        for key, value in corpo.iteritems():
            analisando = corpoDf.loc[corpoDf['ponto_articulacao'].isin(value)]
            grupos = grupos.append(pd.DataFrame({'Parte': key, 'Acertos': (
                analisando.groupby(['resultado']).size() / len(analisando)) * 100}))

        grupos.fillna(0, inplace=True)
        grupos.reset_index(inplace=True)
        grupos = grupos[(grupos.resultado == 1)]
        grupos = grupos.drop(columns='resultado')
        grafico = grupos.plot(kind='bar',  rot=0,
                              colors=self.colors, ylim=(0, 100))

        for p in grafico.patches:
            grafico.annotate(str(round(p.get_height(), 2)) +
                             '%', (p.get_x() * 1.005, p.get_height() * 1.005))

        grafico.set_ylabel("Porcentagem")
        grafico.set_xticklabels(corpo.keys())
        plt.savefig('graficos/corpo_geral/corpo.png')

    def paDescibes(self):
        paResultado = self.df[['ponto_articulacao', 'resultado']]

        grupo = paResultado[(paResultado.resultado == 1)]
        grupo = paResultado.groupby(['ponto_articulacao']).count()

        grupo.fillna(0, inplace=True)
        grupo.reset_index(inplace=True)

        std = grupo['resultado'].std()
        freq = grupo.iloc[grupo['resultado'].argmax()]
        count = grupo['resultado'].count()
        media = grupo['resultado'].median()

        grupo = grupo.drop(columns=['resultado'])

        resultado = pd.DataFrame({
            'Desvio Padrão': std,
            'Maior Frequencia': freq,
            'Media': media,
            'Contagem': count
        })

        resultado.to_csv('csv/final.csv')

    def pior(self):
        pessoas = self.df[['nome_individuo', 'classificacao_imc', 'resultado']]
        pessoasErros = pessoas[pessoas.resultado == 0]

        print pessoasErros.groupby(
            ['nome_individuo', 'classificacao_imc']).count()
