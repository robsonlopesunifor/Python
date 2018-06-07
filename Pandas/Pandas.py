import unittest
import pandas as pd
import numpy as np
import matplotlib as plt
import xlrd

class Pandas(unittest.TestCase):

    def test_o_que_e_a_biblioteca_pandas(self):
        print 'O que é a biblioteca pandas ?'
        print 'E uma bilbioteca de analise de dados, baseado no Numpy. '
        print 'Permite trabalhar com vario tipos de estrutura de dados.'
        print '     Serie:      '
        print '     DataFrame:  '
    
    def test_series(self):
        print '---------- Series----------'
        s = pd.Series([7,'texto',3.14,np.nan,-1234])
        print s

    def test_series_index(self):
        print '---------- Series com index ----------'
        s = pd.Series([7,'texto',3.14,np.nan,-1234], index=['A','B','C','D','E'])
        print s
        

    def test_series_dicionario(self):
        print '---------- Series com dicionario ----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print cidades['Recife']
        print cidades[cidades < 1300]

    def test_series_boolean_indexing(self):
        print '---------- Series com boolean indexing ----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print cidades[cidades < 1300]

    def test_series_boolean_indexing_2(self):
        print '---------- Series com boolean indexing 2----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        menor_que_1300 = cidades < 1300
        print menor_que_1300
        print '\n'
        print cidades[menor_que_1300]

    def test_series_mudando_valor(self):
        print '---------- Series mudando valor ----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print 'Valor antigo', cidades['Brasilia']
        cidades['Brasilia'] = 1300
        print 'Valor novo', cidades['Brasilia']
        print '------------------'
        cidades[cidades < 1200] = 1200
        print cidades

    def test_series_saber_se_existe(self):
        print '---------- Series saber se uma valor existe ----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print 'Recife' in cidades
        print 'Sao Paulo' in cidades

    def test_series_operacao_metematica(self):
        print '---------- Series divisao ----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print cidades / 3
        print '---------- Series quadrado ----------'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print np.square(cidades)
        print '---------- Series quadrado ----------'

    def test_series_soma(self):
        print '---------- Series soma de series ----------'
        print 'soma indices iguais'
        print 'retorna null/NaN para indeces diferentes'
        d = {'Recife':1000,'Brasilia':1200,'Maceio':1300,'Salvador':1400}
        cidades = pd.Series(d)
        print ''
        print cidades[['Recife','Brasilia']] + cidades[['Maceio','Brasilia']]

    def test_series_isnull(self):
        print '---------- Series isnull ----------'
        d = {'Recife':1000,'Brasilia':np.nan,'Maceio':np.nan,'Salvador':1400}
        cidades = pd.Series(d)
        print cidades[cidades.isnull()]

    def test_dataframe(self):
        dataframe = pd.DataFrame()

    def test_dataframe(self):
        data = {'ano':[2010,2011,2012,2013],
                'time':['Flamengo','Flamengo','Vasco','Vasco'],
                'vitorias':[11,8,10,15],
                'derrota':[5,5,2,3]}

        football = pd.DataFrame(data, columns=['ano','time','vitorias','derrota'])
        print football

    def test_adicionar_linha(self):
        print '--------------- adicionar linha ---------------'
        df = pd.DataFrame(columns=['A', 'B', 'C'])
        for i in range(5):
            df.loc[i] = [2, 3, 4]   # o loque adiciona a linha no indece definido
        df.loc[1] = [0, 0, 0]       # subistitue o que esta na linha 1
        df.loc[10] = [0, 0, 0]      # adiciona no indece 10
        df.loc[8] = {'A':2, 'B':2, 'C':2}      # asicionar com dicionario
        df = df.sort_index()
        #df2 = pd.DataFrame({'A':[8], 'B':[8],'C':[8]})
        #df.append(df2, ignore_index=True)
        print df
        df.loc[11] = np.nan         # preenche a linha com valores nulos  
        print df.loc[11]
        df.loc[11] = {'A':9,'B':9}
        print df.loc[11]
        df2 = pd.DataFrame({'A':[7],'B':[7],'C':[7]},columns=['A','B','C'])
        print df2
        df = df.append(df2,ignore_index=True) # alem de adicionar no final
                                              # ele ordena os index 
        print df
        


    def test_adicionar_colunas(self):
        print '-------------------adicionar colunas----------------'
        df = pd.DataFrame(columns=['A', 'B'])
        df2 = df
        df2['C'] = np.nan       # adicionar coluna nova
                                # depois de adicionar uma nova coluna
                                # a melhor forma de adicionar dicionario
                                # e essa de baixo 
        for i in range(5):
            novo = {'B':22,'C':22}  
            df.loc[i] = np.nan
            for chave in novo:
                df.loc[i,(chave)] = novo[chave]      
            
        print df
        df['D'] = np.nan
        print df
        df['E'] = df['F'] = np.nan
        print df
        df.loc[0,('G')] = np.nan
        print df
        

    def test_selecionar_valores(self):
        print '--------------- selecionar valor ---------------'
        #set_value
        data = {'ano':[2010,2011,2012,2013,2015,2017],
                'time':['Flamengo','Flamengo','Vasco','Vasco','Ceara','Fortaleza'],
                'vitorias':[11,8,10,15,9,0],
                'derrota':[5,5,2,3,8,10]}

        df = pd.DataFrame(data, columns=['ano','time','vitorias','derrota'])
        print df[df['vitorias'] > 12]           #mostra somente o valores com vitorias > 12
        print df[df['vitorias'] > 12]['time']
        print df[(df['time'] == 'Flamengo') | (df['time'] == 'Vasco')]
        print '----- fatia -----'
        print df.iloc[0:2]        # fatia de 0 a 2
        print df.iloc[0:2, : ]    # o : depois fa virgula define as colunas
        print '----- fatia -----'
        print df.iloc[[0,1,2]]      # linha 0,1 e 2
        print '----- fatias linha e coluna -----'
        print df.iloc[[0,2],0:3]      # linha 0 e 3, colunas de 0 a 3
        print '---- ultimo valor -----'
        print '----iloc----'
        print df.iloc[-1]       # retorna um vetor
                                # ano          2013
                                # time        Vasco
                                # vitorias       15
                                # derrota         3
        print '----iloc----'
        print df.iloc[[-1]]['ano'] # valor especifico 
        print df.iloc[[-1]]     # retorna a ultima linha
                                #    ano   time  vitorias  derrota 
                                #3  2013  Vasco        15        3
        print '----condicionais----'
        print df[(df.index == df.index[-1])] # retorna a ultima linha
                                #    ano   time  vitorias  derrota 
                                #3  2013  Vasco        15        3

    def test_setar_valor(self):
        print '--------------- setar valor ---------------'
        #set_value
        print '--------------- adicionar linha ---------------'
        df = pd.DataFrame(columns=['A', 'B', 'C'])
        for i in range(5):
            df.loc[i] = [2*i,2*i,2*i] 
        
        print '----setando linha loc nao aceita -1 ----'
        print df.loc[1]
        df.loc[1] = {'A':22, 'B':22, 'C':22}
        print df.loc[1]
        print '----setando celula loc ----'
        print df.loc[1][1]
        df.loc[1][1] = 33
        print df.loc[1][1]
        print '----setando faicha de celulas loc ----'
        print df.loc[:, ('A')]
        df.loc[:, ('A')] = 66
        print df.loc[:, ('A')]
        print '---- iloc ----'
        print df.iloc[[-1]]
        df.iloc[[-1], :] = 99
        print df.iloc[[-1]]
        print '---- iloc ----'
          

    def test_csv(self):
        print '-------------- csv_link --------------'
        df = pd.DataFrame(columns=['A', 'B', 'C'])
        for i in range(5):
            df.loc[i] = [2*i,2*i,2*i] 
        print '------- salvar csv ---------'
        file_name = 'G:\Meu Drive\DA  Software\Python\Pandas\exemplo.csv'
        df.to_csv(file_name, sep=';', encoding='utf-8')
        print '------- carregar csv ---------'
        from_csv = pd.read_csv(file_name,sep=';')
        print from_csv

    def test_csv_link_coluns(self):
        print '-------------- csv_link selecao de colunas --------------'
        cols = ['GRUPOSERVICO_CODIGO','GRUPOSERVICO_DESCRICAO']
        from_csv = pd.read_csv('156diario.csv',sep=';',header=None,names=cols)
        #print from_csv.head()

    def test_execel(self):
        print '-------------- execel --------------'
        #df = pd.Series([7,'texto',3.14,np.nan,-1234], index=['A','B','C','D','E'])
        #df.to_excel('execel.xlsx', sheet_name='Sheet1')

        print pd.read_excel('execel.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    
        
    
    
if __name__ == "__main__":
    print('____Teste da classe Pandas')
    unittest.main()
      
