# Automatic Dataflow opdracht
We verzamelen data van een publieke API en gieten die in de juiste vorm om geanalyseerd te worden en een rapport erover te schrijven.

## Data

De publieke API die ik gebruik is een API over de wachttijden van attracties in pretparken in JSON-formaat. We nemen Bobbejaanland als pretpark naar keuze. We gebruiken de URL https://queue-times.com/nl/parks/311/queue_times.json om de wachttijden te verkrijgen. Bobbejaanland heeft als ID 311 om de JSON-data op te halen.

![Ruwe JSON data](./imgs/json_data.png "Ruwe JSON data")

Dit geeft een lijst met verschillende attracties in het pretpark. Elke attractie heeft:

- ID :  `int`
- name : `string` 
- is_open : `boolean`
- wait_time : `int`
- last_updated : `datetime`

Het `wait_time` attribuut is de wachttijd in minuten.

Ik heb dit script laten lopen van **22/10/2022 14:00:01** tot **06/11/2022 18:00:01**. Het heeft 1 dag gecrasht maar ik heb 2036 json-files met ruwe data verzameld tijdens deze periode.

## Scripts

### *get-data.sh*

Dit script scrapt de JSON-data van de API en slaat het op in de [*data*](./Automatic-Dataflow/data) folder. De JSON-file heeft als naam het tijdstip dat het gescrapt is. Er wordt ook een logfile aangemaakt voor errorberichten.
