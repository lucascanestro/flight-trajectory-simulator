#lee el CSV
import pandas as pd

def data_loader(path):
    df = pd.read_csv(path)
    return df