Generate PDF paperwallet with QR-codes

Requirements:
----------------------
Python2:
	import bitcoinrpc
	import requests
	import json
	import subprocess

LaTeX:
	\usepackage{tikz}
	\usepackage{pst-barcode}
	\usepackage{auto-pst-pdf}
	\usepackage{csvtools}

Create PaperWallet
----------------------
1.) Store address and privkey in csv file using python
	$ python2 wallet.py > wallet.csv
2.) Execute LaTeX
	$ pdflatex --shell-escape paperWallet.tex
3.) Print
4.) Shred pdfs and wallet.csv file
