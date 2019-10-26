# import pandas as pd
# import numpy
# from statsmodels.formula.api import ols
# import statsmodels.api as sm
# df = pd.read_csv('..\csvdata.csv', skipinitialspace=True)
# df = df.dropna(how='any')
# data = df.rename(columns={"fin_pressure #CB":"fin_pressure_CB","fin_flow #CC":"fin_flow_CC","fin_temperature #CD":"fin_temperature_CD","fin_weight #BO":"fin_weight_BO"})
# ana = ols('fin_weight_BO ~ C(fin_pressure_CB) + C(fin_flow_CC) +C(fin_temperature_CD)', data=data).fit()
# # list = data.columns.values.tolist()
# # print(list)
# print(sm.stats.anova_lm(ana))



from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
df = pd.read_csv('..\\test.csv', skipinitialspace=True)
df = df.dropna(how='any')
data_AV = df['AV'].values
data_AVT = df['AV_T'].values
a=0
for i in data_AV:
    if i == 'IN TOLA':
        data_AV[a] = 1
    else:
        data_AV[a] = 0
    a = a + 1
a = 0
for i in data_AVT:
    if i == 'TOLA':
        data_AVT[a] = 1
    else:
        data_AVT[a] = 0
    a = a + 1

gnb = GaussianNB()
#data_AV = data_AV.reshape(1,-1)


X_train = df['fin_flow'].values.reshape(-1,1)
y_train = data_AV.astype('int')
X_test = df['fin_flow_T'].values.reshape(-1,1)
y_test = data_AVT.astype('int')

model = gnb.fit(X_train, y_train)
y_prd = gnb.predict(X_test)
error = np.sqrt(np.mean((y_test - y_prd)**2))
print(y_prd)
print(error)

