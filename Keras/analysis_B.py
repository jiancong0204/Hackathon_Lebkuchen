from load_data import load_data
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import matplotlib.pyplot as plt

df, cols_intW, cols_finW, cols_intS, cols_finS = load_data()
X = df[cols_intW+cols_intS+['fin_pressure #CB', 'fin_flow #CC', 'fin_temperature #CD']+['int_Tracking, Zone1, G #BG', 'int_Tracking, Zone2, G #BH', 'int_Tracking, Zone3, G #BI', 'int_Tracking, Zone4, G #BJ']]
y = df[cols_finS+cols_finW+['fin_Tracking, Zone1, G #BW', 'fin_Tracking, Zone2, G #BX', 'fin_Tracking, Zone3, G #BY', 'fin_Tracking, Zone4, G #BZ']]
X = X.values
y = y.values
ratio = 0.2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio, random_state=50)

sgd = optimizers.SGD(lr=0.01, clipnorm=0.5)
model = Sequential()
model.add(Dense(output_dim=20, input_dim=47))
model.compile(loss='mse', optimizer=sgd)

model.add(Dense(output_dim=6, input_dim=20))
model.compile(loss='mse', optimizer=sgd)

print('Training -----------')
for step in range(5001):
    cost = model.train_on_batch(X_train, y_train)
    if step % 100 == 0:
        print('train cost: ', cost)

# pred = model.predict(X_test, batch_size=32, verbose=1)
# mse = np.sqrt(np.mean((pred - y_test)**2))
# print(mse)

print('\nTesting ------------')
cost = model.evaluate(X_test, y_test, batch_size=40)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

print('test before save: ', model.predict(X_test))
model.save('Analysis_A\A_NN.h5')   # HDF5 file, you have to pip3 install h5py if don't have it
del model  # deletes the existing model
