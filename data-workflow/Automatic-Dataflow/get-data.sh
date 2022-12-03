#!/bin/bash
url="https://queue-times.com/parks/311/queue_times.json"
date_now=$(date '+%Y%m%d-%H%M%S')
dir_data="data"
filename="data-$date_now.json"
path_data="/home/pi/Automatic-Dataflow/$dir_data/$filename"
touch "$path_data" 2> "/home/pi/Automatic-Dataflow/$dir_data/logfile_erros.txt"
curl $url | jq '.rides' > "$path_data" 2> "/home/pi/Automatic-Dataflow/logfile_errors.txt"
