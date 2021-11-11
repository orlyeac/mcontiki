#!/bin/bash

SIMSPERCONFIG=2

for ((j=1; j <= $SIMSPERCONFIG; j++))
    do
		cd /home/user/contiki-ng/tools/cooja/
        ant run_nogui -Dargs=/home/user/contiki-ng/examples/6tisch/simple-node/rpl-tsch-cooja1.csc
		for ((a=1; a <= 18; a++))
    		do
        		if [ -s /home/user/contiki-ng/tools/cooja/build/log_$a.txt ]
        		then

        		mv /home/user/contiki-ng/tools/cooja/build/log_$a.txt /home/user/contiki-ng/tools/cooja/build/log_2.txt

        		fi
			done
		cd /home/user/contiki-ng/tools/cooja/build/
		mv log_2.txt log_2_$j.txt
		cp log_2_$j.txt /home/user/contiki-ng/examples/6tisch/simple-node/logs/
    done