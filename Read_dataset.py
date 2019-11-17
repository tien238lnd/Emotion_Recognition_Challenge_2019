# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:01:31 2019

@author: trung
"""


import numpy as np
import scipy.io.wavfile as wav
import csv

# Mỗi file đọc ra được 1 mảng numpy 1D size khoảng 30000~50000.
# Vì các row có size khác nhau nên ko đưa vô mảng numpy2D được, trước mắt anh để chung trong 1 list đặt tên data như này đã
data = []   
label = []

data_dir = "Handout/Train/"

with open('Handout/train_label.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)    # bỏ qua dòng đầu tiên của file csv
    for row in csv_reader:
        rate, signal = wav.read(data_dir + row[0])
        data.append(signal)
        label.append(int(row[1]))
    
        
# Feature engineering
