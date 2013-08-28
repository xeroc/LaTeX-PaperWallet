import bitcoinrpc
import json
import subprocess

# RPC Connection Info
rpcuser         = 'primecoinrpc'
rpcpassword     = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
rpchost         = 'localhost'
rpcport         = 9912
daemonName      = 'primecoind'

# Wallet passphrase
passphrase='5ecre7'

# Coin Settings
numberAddresses = 2             # number of adresses to generate (are stored in deamon)
coinsPerAddress = 10            # coins to transfer to each new address
fromWallet      = ''            # send from wallet X
walletName      = 'PaperWallet' # store addresses in wallet 'walletName'

###########################################################

## Connect
c = bitcoinrpc.connect_to_remote(rpcuser, rpcpassword , rpchost, port=rpcport)

## Lock & unlock wallet
#c.walletlock()
#c.walletpassphrase(passphrase, 999, 0)

## create 'many'-transaction
target = {}
for s in range(0,numberAddresses) :
 addr = c.getnewaddress(walletName)
 target[addr] = coinsPerAddress

## Create&Broadcast transaction
c.sendmany(fromWallet, target)

CmdOutput = subprocess.check_output('%s listaddressgroupings' % (daemonName), shell=True)
balancesJson = json.loads(CmdOutput)

balances = {}
for b1 in balancesJson :
 for b in b1 :
  addr = b[0]
  balances[addr] = b[1]

# Read all addresses in 'walletName' and create wallet.csv
print "Address;PrivKey;Balance;"
adds = c.getaddressesbyaccount( walletName )
for add in adds:
 x          = str(add) 
 if add in balances :
  balance    = balances[add]
 else :
  balance = 0.0
 privkey    = subprocess.check_output('%s dumpprivkey "%s"' % (daemonName,x), shell=True)
 print "%s;%s;%s" %( x.strip(),privkey.strip(),balance )

#c. walletlock()
