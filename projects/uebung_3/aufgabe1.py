import os
import pandas as pd


def make_subset(size=10, remove_old=False):
    """
    Erstellt einen Teildatensatz mit 10 Instanzen und speichert ihn als subset.txt datei ab.
    :param size: Größe des Teildatensatzes
    :param remove_old: True, wenn die alte Datei gelöscht werden soll
    :return: None
    """

    # entferne die alten Daten, wenn remove_old=True (default=False)
    if remove_old:
        os.remove('subset.txt')

    # lese die Daten ein und erstelle ein Sample der Größe size (default=10) mit zufälligen Einträgen.
    column_names = ['Text String 1', 'Text String 2', 'Metadata 1', 'Metadata 2']
    df = pd.read_csv('sts2016-english-with-gs-v1.0/STS2016.input.answer-answer.txt', sep='\t', header=None,
                     names=column_names)
    df.drop(['Metadata 1', 'Metadata 2'], axis=1, inplace=True)
    sample = df.sample(n=size)

    # speichere die Daten als txt Datei ab. (separator ist ein Leerzeichen)
    sample.to_csv('subset.txt', sep=' ', index=False, header=False)


def get_k_shingles(filepath, k=3):
    """
    Erstellt Shingles der Länge k (default=3) aus einem Text.
    :param filepath: Pfad zur Datei
    :param k: Länge der Shingles
    :return: Generator der Shingles
    """
    # das ist ein Generator (yield statt return) er gibt die Shingles des Textes zurück

    # lese den Text ein
    with open(filepath, 'r') as file:
        text = file.read()

    # entferne alle Zeilenumbrüche
    lines = text.split('\n')
    for line in lines:
        # erstelle die Shingles
        for i in range(len(line) - k + 1):
            yield line[i:i + k]


if __name__ == '__main__':
    shingles = get_k_shingles('subset.txt', k=3)
    for shingle in shingles:
        print(shingle)
