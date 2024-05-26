import numpy as np
def input_next_day(df,lookback,col='High'):
    arr = np.array(df[col])
    return arr[-1*lookback:]
    