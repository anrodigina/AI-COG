import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

pd.options.display.max_rows = 72
pd.options.display.max_columns = 72
file1 = 'psy_20151221.csv'
file2 = 'NEW.csv'
data = pd.read_csv(file1, na_values='?', sep=';', encoding='cp1251')
data2 = pd.read_csv(file2, na_values='?', sep=';', encoding='cp1251')
f1 = open('pearson.txt', 'w')
f2 = open('kendall.txt', 'w')
f3 = open('spearman.txt', 'w')
print(data.corr(method='pearson'), file=f1)
print(data.corr(method='kendall'), file=f2)
print(data.corr(method='spearman'), file=f3)
data.corr(method='pearson').to_csv('pearson.csv', encoding='cp1251')
data.corr(method='kendall').to_csv('kendall.csv', encoding='cp1251')
data.corr(method='spearman').to_csv('spearman.csv', encoding='cp1251')
data2.corr(method='pearson').to_csv('pearson1.csv', encoding='cp1251')
data2.corr(method='kendall').to_csv('kendall1.csv', encoding='cp1251')
data2.corr(method='spearman').to_csv('spearman1.csv', encoding='cp1251')
