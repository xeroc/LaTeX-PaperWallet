#!/bin/sh

if ! [ -r wallet.csv ]
then
	echo "can not read wallet.csv";
	exit 1
fi

mkdir -p paperwallet-generated-files

pdflatex --shell-escape --halt-on-error --output-dir=paperwallet-generated-files paperWallet.tex || exit $?
mv paperwallet-generated-files/paperWallet.pdf ./
echo "-------------------------"
echo "now print paperWallet.pdf"
echo "don't forget to run"
echo "./safe-clean-up"
