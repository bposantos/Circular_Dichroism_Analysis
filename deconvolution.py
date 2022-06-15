import os
import argparse
import sys
import pandas as pd
import parameters

#############################################################################################################################################
#Input arguments to call during code execution
#############################################################################################################################################

parser = argparse.ArgumentParser(description='CD deconvolution')
parser.add_argument("-f", '--file', help="data in txt format", action="store")
parser.add_argument("-p", '--parameters', help="file with parameters", action="store")
args = parser.parse_args()

#############################################################################################################################################
#Transforming txt file into a pandas matrix
#############################################################################################################################################

#read the txt file
df = pd.read_csv(args.file,sep='	', header=None)
#change commas for dots
df = df.stack().str.replace(',','.').unstack()
#remove voltage column. If absent, insert # in the line below
df.drop(1,inplace=True, axis=1)
#rename the columns names. If there was no voltage column, change the number 2 below to the number 1
df.rename(columns={0:'wavelength',2:'absorbance'},inplace=True)
#convert string to float
df['absorbance'] = df['absorbance'].astype(float)


#############################################################################################################################################
#Deconvolution
#############################################################################################################################################

#The mean residue weight of a peptide is the molecular weight divided by the number of backbone amides (number of amino acids -1 if the protein is not acetylated). It is ~ 115 for most proteins if the molecular weight of the sample is not known.
mean_residue_weight = (parameters.molecular_weight/parameters.aa-1)

#concentration in mg/ml is molarity (M) x Molecular Weight (Da)
concentration = round(parameters.molarity*parameters.molecular_weight*0.000001,3)

#Ellipticity, [θ], in deg. · cm2/dmol = (millidegrees times mean residue weight) / (path length in mm times concentration in mg/ml)Norma J. Greenfield Nat Protoc. 2006
ellipticity=round(mean_residue_weight/(parameters.path_length*concentration),2)

#applying the ellipticity function
def multiply(x,y):
	return round(x*y,3)

df['absorbance'] = df.apply(lambda row : multiply(row['absorbance'],ellipticity), axis=1)

#############################################################################################################################################
#Export table
#############################################################################################################################################

#rename the absorbance column name to ellipticity
df.rename(columns={'absorbance':'ellipticity'},inplace=True)

#export as csv
df.to_csv(os.path.splitext(args.file)[0]+'.csv')
