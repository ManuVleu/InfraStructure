#!/bin/bash

PATH_CSV='./data.csv';

first_file=(/home/pi/Automatic-Dataflow/data/*)
names=$(jq '.[].name' ${first_file})
names=$(echo ${names},"time" | sed 's/ /,/g')


echo ${names} > ${PATH_CSV}

for f in /home/pi/Automatic-Dataflow/data/data*;
do
  echo ${f}
  waits=$(jq '.[].wait_time' ${f})
  waits=$(echo ${waits} | sed 's/ /,/g')
  time=$(basename ${f} | tr -d 'data.json' | tr '-' ' ' | cut -c2-)
  echo ${waits}','${time} >> ${PATH_CSV}
done
