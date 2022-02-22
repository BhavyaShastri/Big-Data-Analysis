import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

youtube_data= pd.read_csv(r'C:\Users\ASUS\Downloads\consumers-price-index-december-2021-index-numbers.csv')

print (youtube_data)
plt.figure()
hist1,edges1=np.histogram(youtube_data.Period)
plt.bar(edges1[:-1],hist1,width=edges1[1:]-edges1[:-1])
