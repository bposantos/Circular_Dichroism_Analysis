import os
import argparse
import sys
import pandas as pd
import parameters

#Creating data frames
#Create as many dataframes as CD curves (csv files) that you have and will share the same spectra in the final figure
#In this example, three curves in one spectra
df = pd.read_csv("300821_1.csv", header=0)
df1 = pd.read_csv("300821_2.csv", header=0)
df2 = pd.read_csv("300821_3.csv", header=0)

#Creating the final dataframe that will contain all CD curves. No need to modifications here.
data = {}
final_df = pd.DataFrame(data)

#Joining the curves. If you have more than three curves, add then here just like the examples below.
final_df['wavelength'] = df["wavelength"]
final_df['y0'] = df["ellipticity"]
final_df['y1'] = df1["ellipticity"]
final_df['y2'] = df2["ellipticity"]

#exporting the csv file with all curves
final_df.to_csv('spectra.csv')
