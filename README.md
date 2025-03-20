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
├── README.md                                               # Projektbeschreibung mit einer Übersicht über das Projekt
│
├── main.ipynb                                              # Haupt-Notebook mit der finalen Analyse und Ergebnissen  
│                                 
├── data/                                                   # Enthält alle Roh- und verarbeiteten Daten  
│    ├── processed/                                         # Bereinigte & transformierte Daten  
│    ├── titanic_kaggle/                                    # Original-Kaggle-Datensätze  
│         ├── gender_submission.csv                         # Beispiel-Submission für Kaggle-Wettbewerb  
│         ├── test.csv                                      # Test-Daten ohne Überlebenslabel  
│         ├── train.csv                                     # Trainingsdaten mit Überlebenslabel  
│
├── notebooks/                                              # Explorative Datenanalysen & Experimente  
│    ├── korrelation_datenpunkte.ipynb                      # Untersuchung der Korrelationen zwischen Features  
│    ├── ticket.ipynb                                       # Analyse von Ticket-Daten  
│    ├── titanic_analysis.ipynb                             # Hauptskript für die gesamte Datenanalyse  
│
├── results/                                                # Visualisierungen und Analyseergebnisse  
│    ├── age_pclass.png                                     # Altersverteilung pro Passagierklasse  
│    ├── confusion_matrix_ml.png                            # ML-Modell: Konfusionsmatrix  
│    ├── correlation_heatmap.png                            # Heatmap der Merkmalskorrelationen  
│    ├── family_alone.png                                   # Überlebensraten von Alleinreisenden  
│    ├── family_sibsp.png                                   # Überlebensraten nach Anzahl der Geschwister/Ehepartner  
│    ├── survival_by_embark_town.png                        # Überlebensrate nach Einschiffungshafen  
│    ├── survival_by_embarked_age_group.png                 # Überlebensrate nach Alter und Einschiffungshafen  
│    ├── survival_passenger_with_family.png                 # Überlebensrate von Passagieren mit Familie  
│    ├── survival_rate_by_age.png                           # Überlebensrate nach Altersgruppen  
│    ├── survival_rate_by_class.png                         # Überlebensrate pro Ticketklasse  
│    ├── survival_rate_by_gender.png                        # Überlebensrate nach Geschlecht  
│    ├── ticket_summary_filtered.csv                        # Gefilterte Ticketanalyse  
│    ├── ticket_summary.csv                                 # Gesamt-Ticketanalyse  
│    ├── Ueberlebende_nach_Passagierklassen_1_Anzahl.png    # Überlebende pro Klasse (absolute Zahlen)  
│    ├── Ueberlebende_nach_Passagierklassen_2-Anteil.png    # Überlebende pro Klasse (prozentual)  
│
├── src/                                                    # Quellcode für Datenverarbeitung & Modellierung  
│   ├── __pycache__/                                        # Zwischengespeicherte kompilierte Python-Dateien  
│   ├── datenvorbereitung.py                                # Vorverarbeitung: Laden & Bereinigen der Daten  
│   ├── visualisierungen.py                                 # Funktionen zur Generierung von Diagrammen  
│   ├── utils.py                                            # Hilfsfunktionen für das Projekt  
│
├── tests/                                                  # Test-Skripte zur Validierung der Analysen  
│    ├── machine_learning_fully_commented.ipynb             # Dokumentierte ML-Analyse  
│    ├── konfusionsmatrix_auswertung.txt                    # Bewertung der Konfusionsmatrix  
│
└── requirements.txt                                        # Liste aller benötigten Python-Bibliotheken  
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