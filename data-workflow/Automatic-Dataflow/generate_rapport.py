import os
import lorem
from datetime import datetime


def main():
    with open('./rapport.md','w') as rapport:
        rapport.write(f'# <p align=\"center\">**Rapport Data Analyse Infrastructure Automation**<p><br/>')
        rapport.write(f'Aangemaakt op {datetime.now().day}/{datetime.now().month}/{datetime.now().year} {datetime.now().hour}:{datetime.now().minute}\n')
        rapport.write('## **Inleiding**\n\n')
        rapport.write(f'{lorem.text()}\n\n')

        rapport.write('## **Basisstatistieken**\n\n')
        stats = open('./statistieken.txt','r')
        [rapport.write(f'{line}\n') for line in stats.readlines()]
        rapport.write('\n')
        rapport.write('## **Graphieken**\n\n')
        rapport.write('### *De wachttijden van elke attractie doorheen de tijd*\n')
        [rapport.write(f'#### {graph}\n![{graph}](./graphs/{graph})\n') for graph in os.listdir('graphs') if not 'wt_count' in graph]
        rapport.write('### Aantal keer elke wachttijd voorkomt per attractie\n')
        [rapport.write(f'#### {graph}\n![{graph}](./graphs/{graph})\n') for graph in os.listdir('graphs') if 'wt_count' in graph]

        rapport.write('## **Conclusie**\n')
        rapport.write(f'{lorem.text()}')

main()
