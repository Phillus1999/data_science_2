from mrjob.job import MRJob
import ast
import numpy as np

class PageRankMR(MRJob):
    def mapper(self, _, line):
        data = line.strip().split('\t')

        # Extrahiere die Kategorien aus den Daten
        cat1, cat2 = ast.literal_eval(data[0])

        # Übergebe die Kategorien an den Reducer und zähle die Verbindung
        yield cat1, (1, 1)  # Zähle eine Verbindung zu cat1, der zweite 1 repräsentiert den verteilten Rang
        yield cat2, (1, 1)  # Zähle eine Verbindung zu cat2, der zweite 1 repräsentiert den verteilten Rang

    def reducer(self, category, values):
        weight_matrix = []

        for value in values:
            weight_matrix.append(value)

        # Konvertiere die Liste der Gewichte in eine Numpy-Array (Gewichtsmatrix)
        weight_matrix = np.array(weight_matrix)

        # Spektrale Methode: Berechne den Rang auf Basis der Eigenwerte und Eigenvektoren
        eigvalues, eigvectors = np.linalg.eig(weight_matrix)
        dominant_eigvector = eigvectors[:, np.argmax(eigvalues)]

        # Konvergenzüberprüfung
        epsilon = 0.003
        max_iter = 100  # Setzen Sie hier die gewünschte maximale Anzahl von Iterationen
        rangliste = dominant_eigvector
        for i in range(max_iter):
            # Aktualisiere die Rangliste
            neuer_rangliste = np.dot(weight_matrix, rangliste)

            # Überprüfe die Konvergenz
            if np.linalg.norm(neuer_rangliste - rangliste, 1) < epsilon:
                break

            rangliste = neuer_rangliste

        yield category, float(rangliste)


if __name__ == '__main__':
    PageRankMR.run()