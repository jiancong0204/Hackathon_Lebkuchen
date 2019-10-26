def load_data():
    import pandas as pd
    filename = '..\csvdata.csv'
    df = pd.read_csv(filename)
    cols = df.columns.tolist()
    cols_asm = [c for c in cols if 'asm_' == c[:4]]
    cols_int = [c for c in cols if 'int_' == c[:4]]
    cols_fin = [c for c in cols if 'fin_' == c[:4]]
    df.dropna(inplace=True)
    return df, cols_asm, cols_int, cols_fin