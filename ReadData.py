
#đang suy nghĩ việc tách mfcc ra vì đọc quá lâu

data = pd.DataFrame(columns=['label', 'feature'])
data_dir = "/content/gdrive/My Drive/Handout (1)/Train/Train/"
i = 0
input_duration = 3
with open('/content/gdrive/My Drive/Handout (1)/train_label.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)    # bỏ qua dòng đầu tiên của file csv
    for row in csv_reader:
      i += 1
      X, sample_rate = librosa.load(data_dir + row[0], res_type='kaiser_fast',duration=input_duration,sr=22050*2,offset=0.5)
      #sample_rate, X = wav.read(data_dir + row[0])
      sample_rate = np.array(sample_rate)
      mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)
      feature = mfccs
      data.loc[i, 'feature'] = [feature]
      data.loc[i, 'label'] = int(row[1])
      

    
