#!/usr/bin/python

import csv
import bip38
import json
import sys
import getpass

print "Give the Passphrase to encrypt the addresses:"
pw1 = 0
pw2 = 1
while not pw1 == pw2 :
 pw1 = getpass.getpass('Passphraase: ')
 pw2 = getpass.getpass('Retype passphrase: ')
 if not pw1 == pw2 :
  print "Given Passphrases do not match!"

with open('wallet.csv') as csvfile :
 reader = csv.DictReader(csvfile, delimiter=';')
 jsondump = [ row for row in reader ];
 #print json.dumps( jsondump, indent=2 )

fid=open('wallet.csv', 'w+')
fid.write("Coin;Unit;Address;PrivKey;Balance;\n")

for c in jsondump :
 if c['Unit'] == 'BTC' :
  try :
   c['PrivKey'] = bip38.bip38_encrypt(c['PrivKey'],pw1)
  except :
   print "[Warning] Error encoding the privkey for address %s. Already encrypted?" % c['Address']
 else :
  print "[Warning] Only encrypting Bitcoin Private Keys! Not encrypting %s Addresses" % c['Coin']
 fid.write("%s;%s;%s;%s;%s\n" %(c['Coin'],c['Unit'],c['Address'],c['PrivKey'],c['Balance']))

print "Encrytion finished. The unencrypted privkey was overwritten."
