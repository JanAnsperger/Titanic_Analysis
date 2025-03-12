## Projekt: Titanic Analyse

### Beschreibung
Dieses Projekt führt eine **explorative Analyse der Passagierdaten der Titanic** durch.  
Der Fokus liegt auf der **Untersuchung der Überlebenswahrscheinlichkeiten** basierend auf verschiedenen demografischen Faktoren.  

Unsere Schwerpunkte sind:
- **Datenanalyse**: Untersuchung der Datenqualität und relevanter Merkmale  
- **Aggregation**: Zusammenführung und Berechnung relevanter Statistiken  
- **Visualisierung**: Darstellung der Ergebnisse durch Diagramme  

---

### **Ordnerstruktur**

```
Titanic_Analysis/
├── README.md                               # Projektbeschreibung mit einer Übersicht über das Projekt
│
├── main.ipynb                              # Main-Ausgabe der bereinigten Daten
│                                 
├── data/                                   # Enthält alle Daten für die Analyse  
│    ├── processed/                         # Vorverarbeitete Daten nach Bereinigung und Transformation  
│        ├──  
│
├── notebooks/                              # Jupyter Notebooks oder Python-Skripte für Analysen und Exploration  
│    ├── titanic_analysis.ipnyb                # Hauptskript für die Datenanalyse  
│
├── results/                                # Ergebnisse der Analysen, z. B. Diagramme und Berichte  
│    ├── (....png)  
│
├── src/                                    # Enthält den eigentlichen Code des Projekts, z. B. Funktionen und Modelle  
│   ├── datenvorbereitung.py                # Laden & Bereinigen der Hauptdaten von Seaborn Datensatz ("titanic")
│   ├── visualisierungen.py                 # Plots & Analysen
│   ├── utils.py                            # Hilfsfunktionen
│
├── tests/                                  # Tests für den Code, um sicherzustellen, dass alles korrekt funktioniert  
│    ├──  
│
└── requirements.txt                        # Liste der benötigten Python-Bibliotheken für das Projekt 
```

### Hinweise für Nutzer
```
Die Anwendung wird durch titanic_analysis.py gestartet.
Alle Module befinden sich im src/-Verzeichnis.
Tests befinden sich im tests/-Verzeichnis und können mit pytest ausgeführt werden.
Installiere Abhängigkeiten mit pip install -r requirements.txt.
```
### **Autor**

#### [Titanic Busters]