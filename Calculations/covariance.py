import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_data

df, cols_asm, cols_int, cols_fin = load_data()
df.dropna(inplace=True)
df_int = df[cols_int]
df_int_fin = df[cols_int+cols_fin]
# corr = df.corr()
# corr_int = df_int.corr()
corr_int_fin = df_int_fin.corr()
# plt.subplots(figsize=(15, 15))
# print(df_int_fin.shape[1])
plt.subplots(figsize=(df_int_fin.shape[1], df_int_fin.shape[1]))
image = sns.heatmap(corr_int_fin, annot=True, vmax=1, vmin=0, xticklabels=True, yticklabels=True, square=True, cmap="Greens")
plt.savefig('pic.png')
plt.show()