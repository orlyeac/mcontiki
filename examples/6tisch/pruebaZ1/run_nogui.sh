#!/bin/bash

SIMSPERCONFIG=500

declare -a RANDSEED=('952469' '870831' '550884' '341753' '800337' '666782' '562055' '805319' '608058' '712496' '213210' '783231' '972618' '808589' '315497' '224077' '234491' '269176' '117792' '917024' '385675' '373025' '283136' '239308' '775050' '659972' '278470' '581802' '132927' '745505' '591480' '965733' '441230' '326782' '898186' '218042' '222201' '760475' '214452' '356697' '493840' '782792' '833901' '309446' '769481' '348877' '938050' '408864' '297329' '686452' '978105' '726329' '169566' '910703' '771130' '853913' '351954' '577209' '803877' '386269' '100532' '154552' '285051' '471032' '542194' '235617' '317715' '587715' '237384' '903116' '265386' '496187' '511472' '933282' '300769' '185028' '375165' '921727' '129695' '191330' '129036' '750633' '302533' '199923' '830790' '594592' '659623' '287278' '288112' '739005' '793219' '299941' '302681' '232546' '317373' '543494' '501589' '989274' '765270' '635171' '102739' '146991' '616216' '485890' '696699' '194838' '915703' '513547' '159393' '261096' '319984' '360102' '577852' '947704' '494073' '446534' '957572' '951470' '875848' '404631' '483496' '581802' '893682' '938349' '935477' '713922' '785679' '955529' '572765' '313415' '769738' '212565' '411203' '373554' '392638' '810941' '266778' '467007' '473247' '553184' '862392' '359768' '311998' '508002' '684489' '574664' '379617' '299198' '584691' '972778' '799659' '172726' '449811' '199788' '737558' '165796' '453047' '264494' '789970' '157321' '412503' '212268' '485252' '782254' '490192' '646029' '787751' '555523' '479269' '607172' '752020' '156920' '277501' '915104' '322542' '406740' '345001' '237007' '867624' '513768' '786926' '727425' '623416' '880268' '109600' '237840' '338970' '996316' '503473' '517805' '853829' '711289' '100238' '939347' '355421' '884243' '815415' '294450' '171354' '197459' '977601' '730268' '252304' '897487' '354889' '696981' '711589' '990317' '458944' '103170' '968023' '466995' '961426' '900760' '658164' '714245' '339238' '594810' '433528' '444375' '920454' '156371' '172104' '640392' '968222' '195015' '616103' '166111' '743641' '652143' '505685' '810435' '559083' '457124' '253335' '273296' '349222' '560696' '677213' '913399' '723237' '240771' '945508' '136388' '661627' '749282' '643831' '653260' '179238' '302577' '786862' '790732' '786485' '137482' '348662' '996124' '461006' '294034' '395824' '168019' '121011' '210488' '717941' '303390' '143767' '720443' '538458' '568780' '928227' '921192' '107760' '637874' '495662' '828305' '346004' '551155' '757926' '856729' '628442' '460104' '454342' '139861' '687504' '542983' '554004' '209230' '800089' '437633' '902114' '599549' '529314' '607465' '407993' '949234' '565645' '631956' '216083' '994743' '891568' '822146' '698822' '316678' '537428' '303434' '843602' '976667' '444757' '324761' '171826' '888946' '779062' '713034' '504243' '614830' '721684' '180345' '184061' '702460' '156085' '369797' '134882' '318429' '738327' '226198' '634901' '996333' '831286' '850383' '750027' '493040' '567020' '821795' '449263' '909902' '667634' '359625' '669017' '981102' '731640' '651113' '487838' '208580' '972332' '259491' '167905' '148909' '853460' '139422' '275410' '644492' '366920' '859660' '551075' '391575' '696654' '355290' '939937' '967620' '232894' '368181' '388390' '874999' '921030' '408706' '554400' '156997' '105608' '957659' '891672' '701806' '233633' '490359' '153299' '485488' '984631' '865765' '862412' '126645' '354430' '783800' '370408' '406619' '945623' '357600' '208678' '131519' '376447' '372083' '653810' '879137' '975805' '925594' '845277' '636449' '586082' '152966' '403071' '808303' '338708' '406674' '894765' '754143' '726017' '814954' '765096' '468389' '849189' '271985' '265526' '373697' '696600' '443010' '789803' '183528' '622304' '580737' '620041' '775304' '538914' '691871' '453884' '730262' '456109' '582141' '652338' '813082' '406644' '363814' '843752' '548800' '516888' '631188' '709522' '131155' '383260' '369100' '528572' '905331' '454093' '934624' '896219' '859563' '505333' '820371' '732172' '591811' '320771' '182483' '744351' '744833' '833914' '159740' '471550' '206295' '855434' '490305' '748017' '258552' '663613' '160053' '656821' '113856' '797270' '452797' '663968' '761328' '894996' '384700' '286041' '705828' '446618' '488222' '237718' '956229' '477193' '928172' '920584' '683637' '401360' '604890' '841192' '247831' '930611' '902568' '776280' '856908' '965443' '468344' '672058' '162401' '462596' '197328' '298104' '762736' '909365' '914354' '252483' '537688' '905689' '819504');

for ((j=1; j <= $SIMSPERCONFIG; j++))
    do
	randomseed=${RANDSEED[j-1]}
	r=$RANDOM 

	if ((r == 100))
    then
    r=$RANDOM
    fi

	sed -i s/'(cv'/'('$r/ "/home/user/contiki-ng/arch/platform/z1/platform.c"
	sed -i s/generated/$randomseed/ "/home/user/contiki-ng/examples/6tisch/pruebaZ1/z1_rings2.csc"
		cd /home/user/contiki-ng/tools/cooja/
        ant run_nogui -Dargs=/home/user/contiki-ng/examples/6tisch/pruebaZ1/z1_rings2.csc
		for ((a=1; a <= 18; a++))
    		do
        		if [ -s /home/user/contiki-ng/tools/cooja/build/log_$a.txt ]
        		then

        		mv /home/user/contiki-ng/tools/cooja/build/log_$a.txt /home/user/contiki-ng/tools/cooja/build/log_2.txt
			mv /home/user/contiki-ng/tools/cooja/build/COOJA.testlog /home/user/contiki-ng/tools/cooja/build/COOJA_$j.testlog
			cp /home/user/contiki-ng/tools/cooja/build/COOJA_$j.testlog /home/user/contiki-ng/examples/6tisch/pruebaZ1/Testlogs/

        		fi
			done
		cd /home/user/contiki-ng/tools/cooja/build/
		mv log_2.txt log_2_$j.txt
		cp log_2_$j.txt /home/user/contiki-ng/examples/6tisch/pruebaZ1/logs/
	sed -i s/$randomseed/generated/ "/home/user/contiki-ng/examples/6tisch/pruebaZ1/z1_rings2.csc"
	sed -i s/'('$r/'(cv'/ "/home/user/contiki-ng/arch/platform/z1/platform.c"
    done
