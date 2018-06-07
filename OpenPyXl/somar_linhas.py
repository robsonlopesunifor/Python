"""
#Etapa 1: leia os dados da planilha
import openpyxl, pprint
wb = openpyxl.load_workbook('G:\Meu Drive\DA  Software\Python\OpenPyXl - Execel\Execel\censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}


# TODO: Preencha o countyData com a população e os setores de cada município.
print ('Leitura de linhas ...')

for row in range(2, sheet.max_row + 1):
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value
#Etapa 2: preencher a estrutura de dados
	countyData.setdefault(state, {})
	countyData[state].setdefault(county,{'tracts': 0,'pop': 0})

	countyData[state][county]['tracts'] += 1
	countyData[state][county]['pop'] += int(pop)
#Etapa 3: escreva os resultados em um arquivo
"""
import pprint
print ('Escrevendo resultados ...')
countyData = {'carro':{'moto':88}}
resultFile = open('G:\Meu Drive\DA  Software\Python\OpenPyXl - Execel\Execel\pprint.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')



