import numpy as np

SQRT_YEAR = np.sqrt(245)


def _for_TE(h, l, last_close, adf, sqrt_year=SQRT_YEAR):
    return np.max((np.abs(np.log(h / last_close)),
                   np.abs(np.log(l / last_close)))) * sqrt_year * adf


def get_TE(l, h, c, adf, t, sqrt_year=SQRT_YEAR):
    lhc = np.c_[l[1:], h[1:], c[:-1]]
    TE = np.apply_along_axis(lambda x: _for_TE(*x, 0.9, SQRT_YEAR), 1, lhc)
    for i in range(1, len(TE)):
        TE[i] =  TE[i] * 2 / t + TE[i - 1] * (1 - 2 / t)
    TE[:t + 1] = np.nan
    return np.r_[np.array([np.nan]), TE]


def get_TE_from_df(ohlc, adf, t, sqrt_year=SQRT_YEAR):
    import pandas as pd
    l, h, c = ohlc.iloc[:, 2], ohlc.iloc[:, 1], ohlc.iloc[:, 3]
    TE = get_TE(l, h, c, adf, t, sqrt_year=SQRT_YEAR)
    TE = pd.Series(TE, index=ohlc.index)
    return TE