import pandas as pd


def import_all(filename, seperator):
    return pd.read_csv(filename, sep=seperator)


gender_violence_csv = "../data/gender_violence_stats.csv"
gender_violence_df = import_all(gender_violence_csv, "|")

disinformation_csv = "../data/indian_disinformation_tweets.csv"
disinformation_df = import_all(disinformation_csv, "|")

pak_gov_csv = "../data/pak_gov_apps.csv"
pak_gov_df = import_all(pak_gov_csv, "|")
