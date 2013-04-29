import bitcoinrpc
import requests
import json
import subprocess

# Wallet passphrase
passphrase='5ecre7'

# Establish connection to bitcoind
conn = bitcoinrpc.connect_to_local()
conn.walletlock()
conn.walletpassphrase(passphrase, 999, 0)
accs = conn.listaccounts()

print "Address;PrivKey;Balance;"

# all accounts
for acc in accs:
	adds = conn.getaddressesbyaccount( acc )
	# all addresses
	for add in adds:
		x          = str(add)	
		# get privkey from daemon
		privkey    = subprocess.check_output('bitcoind dumpprivkey "%s"' % (x), shell=True)
		# get balance using blockchain.info
		balanceURL = "http://blockchain.info/address/%s?format=json" % (x)
		balance    = requests.get(balanceURL).json['final_balance']/100000000.0
		print "%s;%s;%3.10f" %( x.strip(),privkey.strip(),balance )

conn. walletlock()
