import pandas as pd
from .utils import Utils


class PlayerStats:
    def __init__(self, df: pd.DataFrame):
        self.df = df

