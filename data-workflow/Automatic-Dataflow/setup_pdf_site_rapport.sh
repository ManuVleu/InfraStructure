#!/bin/bash

sudo md2pdf rapport.md rapport.pdf

mkdocs new rapport_site

cp rapport.md ./rapport_site/docs/index.md
cp -R graphs ./rapport_site/docs/graphs

cd ./rapport_site || exit; mkdocs serve
