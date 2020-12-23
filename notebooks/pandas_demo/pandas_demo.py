import seaborn as sns


def load_data():
    return sns.load_dataset("penguins")


def pairs_plot(df):
    return sns.pairplot(df, hue="species")


def group_count(df, col_name):
    return df.groupby(col_name).count()
