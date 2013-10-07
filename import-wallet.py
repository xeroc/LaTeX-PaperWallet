import bitcoinrpc
import json
import subprocess

# RPC Connection Info
rpcuser         = 'ppcoinrpc'
rpcpassword     = '7Mmmyw7PKJJxJhEETkC72LJP4QESR6dVRQX99otVsGDw'
rpchost         = 'localhost'
rpcport         = 9902
daemonName      = 'ppcoind'

# Wallet passphrase
passphrase='5ecre7'

## Connect
c = bitcoinrpc.connect_to_remote(rpcuser, rpcpassword , rpchost, port=rpcport)

## Lock & unlock wallet
#c.walletlock()
#c.walletpassphrase(passphrase, 999, 0)

# Establish connection to bitcoind
accs = c.listaccounts()

print "Address;PrivKey;Balance;"

# all accounts
for acc in accs:
	adds = c.getaddressesbyaccount( acc )
	# all addresses
	for add in adds:
		x          = str(add)	
		# get privkey from daemon
		privkey    = subprocess.check_output('ppcoind dumpprivkey "%s"' % (x), shell=True)
		# get balance using blockchain.info
		# balanceURL = "http://blockchain.info/address/%s?format=json" % (x)
		# balance    = requests.get(balanceURL).json['final_balance']/100000000.0
		print "%s;%s;--" %( x.strip(),privkey.strip() )

#c.walletlock()
