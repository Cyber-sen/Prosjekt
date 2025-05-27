Strukturen på prosjektet er lagt opp til: 
-Fra jupyter boka
   
my_project/
│
├── src/ # Kildekode
│ ├── README.md # Dokumentasjon av src-strukturen
│ ├── my_package/ # Hovedpakken med applikasjons‐kode
│ │ ├── init.py # Gjør katalogen om til et Python-pakke
│ │ ├── API.py 
│ │ ├── lesogplottCsv.py
│ │ └── sammenligning.py
│ 
├── data/ # Datakatalog for datasett
│ ├── README.md # Beskrivelse av data‐innhold
│ ├── Vannføring.csv # Eksempel på rådata
│ ├── temperatur.csv # Flere datasett
│ 
├── notebooks/ # Jupyter‐notebooks
│ ├── README.md # Beskrivelse av notebooks‐katalogen
│ ├── Vannføring.ipynb # Analyse‐notat for vannføring
│ ├── temperatur.ipynb # Analyse‐notat for temperatur
│
├── tests/ # Enhetstester
│ ├── README.md # Hvordan kjøre tester og struktur
│ ├── init.py # Gjør katalogen om til et Python-pakke
│ ├── Funksjonstest_sammenligning_plot.py
│ ├── Enhetstest_tidsserieplotter.py
│
├── docs/ # Hoveddokumentasjon
│ ├── README.md # Oversikt over dokumentasjons‐katalogen
│ ├── user_guide.md # Brukerveiledning
│ └── architecture.md # Arkitektur‐oversikt
│
├── venv/ # Virtuelt miljø (ikke versjons­kontroll!)
│
├── .gitignore # Git‐ignore‐regler
├── README.md # Prosjektoversikt
├── requirements.txt # Prosjektavhengigheter
└── setup.py # Installasjons‐script for pakken