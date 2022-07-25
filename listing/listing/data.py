import pdb
import pandas as pd
def get_df(path):
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".xlsx"):
        df = pd.read_excel(path)
    elif path.endswith(".json"):
        df = read_json(path)
    else:
        raise Exception("The file is not an .csv,.xlsx or .json file")
    return df
pdb.set_trace()