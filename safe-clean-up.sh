#!/bin/bash

echo "Shreding files"
shred -u -z wallet.csv paperWallet.pdf paperWallet-pics.pdf paperwallet-generated-files/*

echo "Deleting files"
rm -Rf wallet.csv paperWallet.pdf paperWallet-pics.pdf paperwallet-generated-files
