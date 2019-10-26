def ANNmodel(hid_layers=[], in_dim=1, out_dim=1):
    model = Sequential()
    if len(hid_layers) == 0:
        model.add(Dense(out_dim, input_dim=in_dim, activation='relu', kernel_initializer='normal'))
    else:
        model.add(Dense(hid_layers[0], input_dim=in_dim, activation='relu', kernel_initializer='normal'))
        for layer in hid_layers:
            model.add(Dense(layer, activation='relu'))
        model.add(Dense(out_dim))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

def get_hid_layers(min_layers=0, max_layers=5, min_neurons=1, max_neurons=10, n_iter=1):
    hid_layers = []
    for _ in range(n_iter):
        layers = np.random.randint(min_layers, max_layers)
        hid_layers.append(np.random.randint(low=min_neurons, high=max_neurons, size=layers).tolist())
    return hid_layers
#train
runANN = False
np.random.seed(99)
n_iter = 100
param_dist = {'hid_layers': get_hid_layers(max_layers=10, min_neurons=1, max_neurons=20, n_iter=n_iter)}

if runANN:
    ann = KerasRegressor(build_fn=ANNmodel, in_dim=X_train.shape[1], epochs=50, batch_size=256, verbose=0)
    random_search_ann = GridSearchCV(estimator=ann, param_grid=param_dist, scoring='neg_mean_squared_error')
    start = time.time()
    random_search_ann.fit(X_train, y_train)
    elapsed_ann = (time.time() - start)
    print("RandomizedSearchCV took %.2f seconds for %d candidates"
          " parameter settings." % (elapsed_ann, n_iter))
    report(random_search_ann.cv_results_)
# test
if runANN:
    best_ann = random_search_ann.best_estimator_
else:
    best_ann_param =  {'hid_layers': [4]} 
    best_ann = KerasRegressor(build_fn=ANNmodel, in_dim=X_train.shape[1], epochs=50, batch_size=256, verbose=0, **best_ann_param)
start = time.time()
best_ann.fit(X_train, y_train)
elapsed_ann_test = (time.time() - start)
print('r2_score for training set:', r2_score(y_train, best_ann.predict(X_train)))
print("ANN took %.2f seconds for test." % (elapsed_ann_test))