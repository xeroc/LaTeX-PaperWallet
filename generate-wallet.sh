#!/bin/sh

# all args are passed to vanity
# call:
# ./generate-wallet.sh 1Pat

if ! [ -f wallet.csv ]
then
	echo "Address;PrivKey;Balance;" > wallet.csv
	chmod 600 wallet.csv
fi

ad=
vanitygen "$@" | while read a b
do
	if [ "$a" == "Address:" ]
	then
		ad=$b;
	elif [ "$a" == "Privkey:" ]
	then
		echo "$ad;$b;\\_\\_\\_\\_;" >> wallet.csv
		echo "$ad added to wallet.csv"
		ad=
	else
		echo "$a $b"
	fi
done
