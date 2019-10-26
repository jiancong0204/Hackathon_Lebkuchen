from load_data import load_data
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns


df, cols_asm, cols_int, cols_fin = load_data()

## for initial inspection ##
for c in cols_int:
    if c == 'int_Shape #BK':
        continue
    else:
        plt.figure()
        sns.distplot(df[c], rug=False, hist_kws={'color': 'green', 'label': 'Histogram'}, kde_kws={'color': 'green', 'label': 'KDE'})
        plt.savefig('Hist_int\hist_' + c)
        plt.close()

## for final inspection ##
# for c in cols_fin:
#     if c == 'fin_Shape #CA':
#         continue
#     else:
#         plt.figure()
#         sns.distplot(df[c], rug=False, hist_kws={'color': 'green', 'label': 'Histogram'}, kde_kws={'color': 'green', 'label': 'KDE'})
#         plt.savefig('Hist_fin\hist_' + c)
#         plt.close()

## for asm ##
# for c in cols_asm:
#     plt.figure()
#     sns.distplot(df[c], rug=False, hist_kws={'color': 'green', 'label': 'Histogram'}, kde_kws={'color': 'green', 'label': 'KDE'})
#     plt.savefig('Hist_asm\hist_' + c)
#     plt.close()