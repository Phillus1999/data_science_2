# Komponenten

- generator_py: Dieser Generator erstellt (dünnbesetzte) NXM Matrizen 
(standartmäßig 100 X 100), und fügt sie (formatiert) in die input.txt.
Das Format lautet: 

"zeilennummer" "spaltennummer" "wert" "matrix A/matrix B"

Zusätzlich wird eine Matrixmultiplikation berechnet, und das Ergebnis in result.txt
gespeichert. Dies dient zum Vergleich mit dem Ergebnis mit MRJob.

- matrixmultilication.py: Dieses Skript führt eine Matrixmultiplikation mit MRJob durch
  (genaue Beschreibungen siehe Kommentare im Code).

# Ausführung

Das Skript benötigt eine input.txt (in diesem Fall haben wir eine input_100x100.txt)
und gibt eine output.txt aus, welche das Ergebnis der Matrixmultiplikation enthält.

Um matrixmultiplication.py aufzurufen, benötigen Sie folgenden Befehl (ohne ""):

"python3 matrixmultiplication.py input_100x100.txt > output.txt"

input_100x100.txt kann abweichen, je nachdem wie das inputfile vom Generator kreiert wird.
