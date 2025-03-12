# Visualisierungen
import matplotlib.pyplot as plt
import seaborn as sns

def plot_alter_klasse(df):
    """Zeigt die Verteilung von Alter nach Klasse als Boxplot."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='pclass', y='age', data=df, palette='YlGnBu')
    plt.xlabel('Passagierklasse')
    plt.ylabel('Alter')
    plt.title('Alter vs. Klasse')
    plt.show()

def plot_ueberlebensrate(df):
    """Zeigt die Überlebensrate nach Klasse als Balkendiagramm."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='pclass', y='survived', data=df, palette='YlGnBu')
    plt.xlabel('Passagierklasse')
    plt.ylabel('Überlebensrate')
    plt.title('Überlebensrate nach Klasse')
    plt.show()