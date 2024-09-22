import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals["weight"] > 100].sort_values(
        ["weight"], ascending=False
    )[["name"]]