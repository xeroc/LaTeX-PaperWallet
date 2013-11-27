#!/bin/sh
## Prefix of choise #########################
     Prefix=1Foo
CoinVersion=0
   CoinName='Bitcoin'
   CoinUnit='BTC'
## Coin Versions ############################
# ['bitcoin']     = 0
# ['primecoin']   = 23
# ['ppcoin']      = 55
# ['litecoin']    = 48
# ['protoshares'] = 56
# ['namecoin']    = 52
# ['feathercoin'] = 14
# ['megacoin']    = 50
# ['novacoin']    = 8
# ['worldcoin']   = 73
# ['freicoin']    = 73
# ['infinitecoin']= 102
#############################################

if ! [ -f wallet.csv ]
then
	echo "Coin;Unit;Address;PrivKey;Balance;" > wallet.csv
	chmod 600 wallet.csv
fi

echo "[WARNING] Do check your private key before depositing"

ad=
vanitygen -k -X $CoinVersion $Prefix | while read a b
do
	if [ "$a" == "Address:" ]
	then
		ad=$b;
	elif [ "$a" == "Privkey:" ]
	then
		echo "$CoinName;$CoinUnit;$ad;$b;\\_\\_\\_\\_;" >> wallet.csv
		echo "$ad added to wallet.csv"
		ad=
	else
		echo "$a $b"
	fi
done
