def load_data():
    import pandas as pd
    filename = '..\csvdata.csv'
    df = pd.read_csv(filename)
    cols = df.columns.tolist()
    cols_intW = [c for c in cols if 'int_W' == c[:5]]
    cols_finW = [c for c in cols if 'fin_W' == c[:5]]
    cols_intS = [c for c in cols if 'int_S' == c[:4]]
    cols_finS = [c for c in cols if 'fin_S' == c[:4]]
    df.dropna(inplace=True)
    return df, cols_intW, cols_finW, cols_intS, cols_finS