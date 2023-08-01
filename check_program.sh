#!/bin/bash

if ps -ef | grep python3 | grep src/app.py >/dev/null
then
    echo "Programa está em execução."
else
    echo "Programa não está em execução. Iniciando o programa."
    python3 src/app.py &
fi
