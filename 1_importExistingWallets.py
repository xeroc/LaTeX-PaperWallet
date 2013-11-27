import bitcoinrpc
import json
import subprocess
import pprint

# RPC Connection Info
altcoins = [
          {
           'name'            : 'Protoshares',    # Name of the coin
           'unit'            : 'PTS'             # Unit name of that coin
           'rpcuser'         : 'protosharesrpc', # connections settings -- daemon must be running
           'rpcpassword'     : 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxg',
           'rpchost'         : 'localhost',
           'rpcport'         : 3838,
           'daemonName'      : 'protoshared',    # daemon name to dump privkeys
           'passphrase'      : '',               # optional passphrase
           'numberAddresses' : 1,                # number of adresses to generate (are stored in deamon)
           'coinsPerAddress' : 1,                # coins to transfer to each new address
           'fromWallet'      : '',               # send from wallet X
           'walletName'      : 'PaperWallet',    # create new addreses in a new wallet
          },
          { ########### You can add multiple daemons (altcoins) here
           'name'            : 'Litecoins',      # Name of the coin
           'unit'            : 'LTC'             # Unit name of that coin
           'rpcuser'         : 'litecoinrpc',    # connections settings -- daemon must be running
           'rpcpassword'     : 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxg',
           'rpchost'         : 'localhost',
           'rpcport'         : 9332,
           'daemonName'      : 'litecoind',      # daemon name to dump privkeys
           'passphrase'      : '',               # optional passphrase
           'numberAddresses' : 1,                # number of adresses to generate (are stored in deamon)
           'coinsPerAddress' : 1,                # coins to transfer to each new address
           'fromWallet'      : '',               # send from wallet X
           'walletName'      : 'PaperWallet',    # create new addreses in a new wallet
          },
]

###########################################################
fid=open('wallet.csv', 'w')
fid.write("Coin;Unit;Address;PrivKey;Balance;\n")

for altcoin in altcoins : 
 # Variables
 numberAddresses = altcoin['numberAddresses']
 coinsPerAddress = altcoin['coinsPerAddress']
 fromWallet      = altcoin['fromWallet']
 walletName      = altcoin['walletName']

 ## Connect
 c = bitcoinrpc.connect_to_remote(altcoin['rpcuser'],
                                  altcoin['rpcpassword'],
                                  altcoin['rpchost'], 
                                  port=altcoin['rpcport'])
 ## Test Connection
 try :
  info = c.getinfo()
 except :
  print('No Connection!')
  continue

 # Lock & unlock wallet
 if not altcoin['passphrase'] == "" :
  c.walletlock()
  c.walletpassphrase(altcoin['passphrase'], 999, 0)

 # Read all addresses in 'walletName' and create wallet.csv
 adds = c.getaddressesbyaccount( walletName )

 try :
		altWalletCmd = '%s listaddressgroupings' % (altcoin['daemonName'])
		CmdOutput = subprocess.check_output(altWalletCmd, shell=True)
		adds = json.loads(CmdOutput)
 except :
  print('Something went wrong getting addresses!')
  continue

 for add in adds:
		x = str(add[0][0])
		balance = (add[0][1])
		privkey = subprocess.check_output('%s dumpprivkey %s' % (altcoin['daemonName'],x), shell=True)
		fid.write("%s;%s;%s;%s;%.8f\n" %( altcoin['name'],altcoin['unit'],x.strip(),privkey.strip(),balance))

 if not altcoin['passphrase'] == "" :
  c. walletlock()

fid.close()
