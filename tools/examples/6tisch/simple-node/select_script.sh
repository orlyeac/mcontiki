#!/bin/bash

for ((a=1; a <= 18; a++))
    do
        if [ -s /home/mmmorfa/contiki-ng/examples/6tisch/simple-node/logs/log_$a.txt ]
        then

        mv /home/mmmorfa/contiki-ng/examples/6tisch/simple-node/logs/log_$a.txt /home/mmmorfa/contiki-ng/examples/6tisch/simple-node/logs/log_2.txt

        fi
done