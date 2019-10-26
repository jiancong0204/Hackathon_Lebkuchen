import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = 'csvdata.csv'
df = pd.read_csv(filename)
cols = df.columns.tolist()
cols_asm = [c for c in cols if 'asm_' == c[:4]]
cols_int = [c for c in cols if 'int_' == c[:4]]
cols_fin = [c for c in cols if 'fin_' == c[:4]]
df.dropna(inplace=True)
df_int = df[cols_int]
df_int_fin = df[cols_int+cols_fin]
# corr = df.corr()
# corr_int = df_int.corr()
corr_int_fin = df_int_fin.corr()
# plt.subplots(figsize=(15, 15))
print(df_int_fin.shape[1])
plt.subplots(figsize=(df_int_fin.shape[1], df_int_fin.shape[1]))
image = sns.heatmap(corr_int_fin, annot=True, vmax=1, vmin=0, xticklabels=True, yticklabels=True, square=True, cmap="Greens")
plt.savefig('pic.png')
plt.show()