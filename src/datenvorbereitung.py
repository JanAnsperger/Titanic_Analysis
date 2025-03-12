# Datenvorbereitung
import pandas as pd
import seaborn as sns

def lade_titanic_daten():
    """Lädt den Titanic-Datensatz von Seaborn und gibt ihn als Pandas DataFrame zurück."""
    df = sns.load_dataset("titanic")
    return df.copy()

def bereinige_daten(df):
    """Bereinigt den Titanic-Datensatz (fehlende Werte auffüllen, unnötige Spalten entfernen)."""
    df = df.copy()
    df.drop(columns=['deck', 'embark_town', 'alive', 'who', 'class', 'adult_male'], inplace=True, errors='ignore')
    df['age'].fillna(df['age'].median(), inplace=True)
    df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
    df['fare'].fillna(df['fare'].median(), inplace=True)
    return df
