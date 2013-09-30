Generate PDF paperwallet with QR-codes

# Disclaimer #
Use at your own risk!

# Requirements: #
import-wallet.py:
* ppcoind
Latex distrubition such as TexLive or MikTex

generate-wallet.sh:
* vanitygen

Python libraries:
* import bitcoinrpc
* import requests
* import json
* import subprocess

LaTeX:
* \usepackage{tikz}
* \usepackage{pst-barcode}
* \usepackage{auto-pst-pdf}
* \usepackage{csvtools}
* \usepackage{coolstr}

# Howto Create PaperWallet #
1. Store address and privkey in csv file
	* using import-wallet.py to get the keys from primecoind
		$ python2 import-wallet.py > wallet.csv
	* using generate-wallet.sh to generate keys with have an address matching a pattern (e.g. start with 1Fuu)
		$ ./generate-wallet.sh -k 1Pattern
		press Ctrl + C when You have enough
		View/edit your wallet.csv
3. Uncomment _ONE_ note layout input line in 'paperWallet.tex' (line 41-48)
2. Generate the PDF
	$ ./generate.sh
3. Print
4. Shred wallet.csv, pdfs and all generated files
5. Donate to xeroc, vanitygen, charity ...

# Donations are welcome #
Thank you for every donation.
BTC: `1XeRocJ6PRUX419QQo9crW5nbsjetJLUn` 
XPM: `AXeRocF9m3VX3P5TAfGiDq6hSSqWG5r6nd`
