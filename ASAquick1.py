import os
filename = "example.fasta"
command="/home/biomine/programs/ASAquick/bin/ASAquick "+filename
os.system(command)

outfile = open('ASA.txt','w')

fileaddress = r"asaq.example.fasta/rasaq.pred"
f = open(fileaddress)
res_list = list()
line = f.readline()
while line:
    line = line.rstrip('\n')
    line_cols = line.split()
    res_list.append(str(round((float(line_cols[2])/2)+0.5,2)))
    line = f.readline()
f.close()
res_list = res_list[:-1]
entry_res_string = ",".join(res_list)
outfile.writelines(entry_res_string+'\n')
outfile.close()

import numpy as np
import pandas as pd
import csv
ASA= []
f = open(r'ASA.txt')
for line in f:
    data_line = line.rstrip().split(',')
    ASA.append(data_line)
ASA = np.concatenate(ASA)
ASA_Score = list(ASA)