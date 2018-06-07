# importa o arquivo census2010 e conta toda a populacao 

import os
os.chdir('G:\Meu Drive\DA  Software\Python\OpenPyXl - Execel\Execel')
import census2010
census2010.allData['AK']['Anchorage']
    #{'pop': 291826, 'tracts': 55}
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('A população de 2010 de Anchorage foi' + str(anchoragePop))
    #The 2010 population of Anchorage was 291826
