# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:01:31 2019

@author: trung
"""


import numpy as np
import scipy.io.wavfile as wav

# Mỗi file đọc ra được 1 mảng numpy 1D size khoảng 30000~50000.
# Vì các row có size khác nhau nên ko đưa vô mảng numpy2D được, trước mắt anh để chung trong 1 list đặt tên data như này đã
data = []   

data_dir = "Handout/Train/PAEP-"
for i in range(1, 5230):
    (rate, signal) = wav.read(data_dir + str(i).zfill(6) + ".wav")
    data.append(signal)
