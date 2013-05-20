Generate PDF paperwallet with QR-codes

# Disclaimer #
Use at your own risk!

# Requirements: #
import-wallet.py:
* bitcoind or bitcoin-qt
* Python
* import bitcoinrpc
* import requests
* import json
* import subprocess

generate-wallet.sh:
* vanitygen

LaTeX:
* \usepackage{tikz}
* \usepackage{pst-barcode}
* \usepackage{auto-pst-pdf}
* \usepackage{csvtools}

# Create PaperWallet #
1. Store address and privkey in csv file
	* using import-wallet.py to get the keys from bitcoind or bitcoin-qy
		$ python2 import-wallet.py > wallet.csv
	* using generate-wallet.sh to generate keys with have an address matching a pattern (e.g. start with 1Fuu)
		$ ./generate-wallet.sh -k 1Pattern
		press Ctrl + C when You have enough
		View/edit your wallet.csv
2. Generate the PDF
	$ ./generate.sh
3. Print
4. Shred wallet.csv, pdfs and all generated files
5. Donate to xeroc, vanitygen, charity ...
