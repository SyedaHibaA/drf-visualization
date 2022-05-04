from csv_to_df import gender_violence_df
import seaborn as sns
import matplotlib.pyplot as plt


def victims_by_gender():
    """
    Bar graph of gender distribution of victims.

    When multiple victims, count as separate, regardless of crime committed

    x-axis: male, female, transgender
    y-axis: number of cases
    """
    plt.figure(figsize=(15, 10))
    gender_only_df = gender_violence_df[['Gender of Victim', 'Gender of Victim(s)', 'Gender of Victim(s).1', 'Gender of Victim(s).2', 'Gender of Victim(s).3']].copy()
    gender_only_df[['Gender of Victim', 'Gender of Victim.1']] = gender_only_df['Gender of Victim'].str.split(', ', expand=True)
    gender_divided_series = gender_only_df.unstack().reset_index(drop=True).dropna()
    gender_divided_df = gender_divided_series.to_frame()
    gender_divided_df.rename(columns={0: "Gender of Victim"}, inplace=True)
    plot = sns.countplot(x="Gender of Victim", data=gender_divided_df, order=gender_divided_df['Gender of Victim'].value_counts().index)
    for p in plot.patches:
        plot.annotate('{:1d}'.format(p.get_height()), (p.get_x() + 0.375, p.get_height() + 1))

    plt.show()


victims_by_gender()
