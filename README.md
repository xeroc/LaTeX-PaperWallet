This tool lets your generate PDF paperwallet for arbitrary altcoins
using QR-Codes for fast access to the address and the private key.

# Disclaimer #
***Use at your own risk!***

# Requirements: #
* LaTeX distribution such as TexLive or MikTex
* LaTeX Packages
    * tikz
    * pst-barcode
    * auto-pst-pdf
    * csvtools
    * coolstr
* 1_createEmptyPaperWallets:
    * vanitygen
* 1_createNewWalletsAndMoveCoins **and** 1_importExistingWallets:
    * Python libraries:
        * bitcoinrpc
        * json
        * subprocess
        * pprint

# Howto Create PaperWallet #
1. Store address and privkey in csv file
   You may select one of three options to generate you wallet.csv file with
   private keys in it. Read the header of the files to adjust the settings to
   your needs.
    * **1_createEmptyPaperWallets**:
        to create new empty wallets using vanitygen
        press ***Ctrl+C*** when You have enough
    * **1_createNewWalletsAndMoveCoins**:
        to create new wallets using the bitcoin daemons and move coins accoring to the settings in that file
    * **1_importExistingWallets**:
        load existing wallets from deamons using 'listaddressgroupings'
3. Uncomment _ONE_ note layout input line in 'paperWallet.tex' (line 41-48)
2. Generate the PDF
	$ ./2_generatePDF.sh*
3. Print
4. Cleanup:
 %./3_shredAndCleanup.sh*
5. Donate to xeroc, vanitygen, charity ...

# Donations are welcome #
Thank you for every donation.
BTC: `1XeRocJ6PRUX419QQo9crW5nbsjetJLUn` 
XPM: `AXeRocF9m3VX3P5TAfGiDq6hSSqWG5r6nd`
LTC: `LXeRoc6FVG3eswpuA4CJxjqMWc7Aq5sNnp`
PPC: `PXeRocjAG8W2bBPxZPRPBn5yErg3mRx8Gx`
PTS: `PkXeRocDnRSkHzuTbQdqYWRQ8QqmjwrdyY`
NMC; `MxerocLbhWEKELr2DAjXzUwAWRop2nsSZJ`
