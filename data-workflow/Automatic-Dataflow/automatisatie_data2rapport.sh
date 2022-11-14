#!/bin/bash

echo "Transformeren van data naar data.csv"
./transform-data.sh

echo "Installeer packages voor analyse en rapport"
sudo pip install lorem
sudo pip install pandas
sudo pip install matplotlib
sudo apt-get install libpangocairo-1.0-0
sudo pip install md2pdf
sudo pip install mkdocs
echo "Analyse maken van de data"
python data_analyse.py

echo "Genereer rapport.md"
python generate_rapport.py

echo "Genereer rapport.pdf en host static site op localhost:8000"
./setup_pdf_site_rapport.sh
