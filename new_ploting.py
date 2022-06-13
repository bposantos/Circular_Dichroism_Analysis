#-*-coding:utf-8 -*-
# General code for plotting Circular Dichroism data

#############################################################################################################################################
#Identifying how many data files will be used
#############################################################################################################################################

import pandas as pd

#Number of spectra per image
#var1 = int(input("How many text files will be used to plot the data: "))
var1=4


#############################################################################################################################################
#Peptide Information
#############################################################################################################################################

molecular_weight = 1957.21
aa = 17
path_length = 1
dic_nomes = {1:'s2_popc_31_01.txt', 2:'s2_popc_62_01.txt', 3:'s2_popc_125_01.txt', 4:'s2_popc_250_01.txt'}
dic_media_concentration = {1:31.25, 2:62.5, 3:125, 4:250}
csv_name = "teste2021"

#############################################################################################################################################
#CD files that will be analyzed
#############################################################################################################################################

list_var1 = []
dic_var1 = {}
dic_var2 = {}
dic_var3 = {}

#############################################################################################################################################
#Deconvolution
#############################################################################################################################################
for i in range(1,var1+1):
	list_var1.append(i)

for i in list_var1:
	var2 = dic_nomes[i]
	dic_var1[i] = {}
	dic_var1[i]['file_name'] = var2
	dic_var2[i] = {}
	dic_var2[i]['file_name'] = var2	
	abrir_txt = ''
	#le_linhas = ''
	lista_txt = []
	dic_var1[i]['abrir_txt'] = open(dic_var1[i]['file_name'], "r")
	dic_var1[i]['le_linhas'] = dic_var1[i]['abrir_txt'].readlines()
	dic_var1[i]['lista_txt'] = []
	for j in dic_var1[i]['le_linhas']: #para cada elemento das linhas
		dic_var1[i]['lista_txt'].append(j) #os elementos são adicionados à lista
	dic_var1[i]['lista_split'] = [dado.split('\t') for dado in dic_var1[i]['lista_txt']]
	for element in list_var1:
		dic_var2[i]['x'] , dic_var2[i]['y'] = zip(*dic_var1[i]['lista_split'])
		dic_var2[i]['x'] , dic_var2[i]['y'] = list(dic_var2[i]['x']), list(dic_var2[i]['y'])
		for elemento in range(len(dic_var2[i]['x'])):
			dic_var2[i]['x'][elemento] = dic_var2[i]['x'][elemento].replace(',', '.')
		for elemento in range(len(dic_var2[i]['y'])):
			dic_var2[i]['y'][elemento] = dic_var2[i]['y'][elemento].replace(',', '.')
		dic_var2[i]['x'] = [float(valor) for valor in dic_var2[i]['x']]
		#print(x)  # [59.99167, 60.0]
		dic_var2[i]['y'] = [float(valor) for valor in dic_var2[i]['y']]
		#print(y)  # [-3180.0, -3181.0]	

for i in list_var1:
	dic_var3[i] = {}
	dic_var3[i]['file_name'] = dic_var2[i]['file_name']
	var3 = dic_media_concentration[i]
	dic_var2[i]['Ellipticity'] = ((molecular_weight/aa-1)/(path_length*(molecular_weight*var3*0.000001))) 
	#Ellipticity, [θ], in deg. · cm2/dmol = (millidegrees times mean residue weight) / (path length in mm times concentration in mg/ml)Norma J. Greenfield Nat Protoc. 2006
	dic_var2[i]['y'] = [round(z*dic_var2[i]['Ellipticity'],2) for z in dic_var2[i]['y']]


#############################################################################################################################################
# Converting dictionaries in CSV files
#############################################################################################################################################

df = pd.DataFrame.from_dict(dic_var2, orient="index")
print(df.head())
print(df.info())
df1 = pd.DataFrame(df.loc[1,'x'], columns=['x'])
df1['Y1'] = list(df.loc[1,'y'])
df1['Y2'] = list(df.loc[2,'y'])
df1['Y3'] = list(df.loc[3,'y'])
df1['Y4'] = list(df.loc[4,'y'])
print(df1.info())
df1.to_csv(csv_name+".csv")