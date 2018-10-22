# PyLiskShortAddressGen
A Python tool that generates short Lisk Addresses.

This tool generates Lisk addresses. The user is able to specify 1) maximum
length of Lisk Addresses to find, 2) whether the addresses should be
BIP39-compliant(i.e. usable in Lisk Hub), and 3) whether to write generated
addresses to a 'shortAddresses.txt' file.

Addresses shorter than 16 characters in length become increasingly difficult
to find.  

There is some performance advantage to generating non-BIP39-compliant
addresses.


## **Requirements**

[Python 3.6 or higher](https://www.python.org/downloads/)

[PyNaCl library](https://pypi.org/project/PyNaCl/)

[bitarray library](https://pypi.org/project/bitarray)

## Support Nimbus
Please [vote for **nimbus**](lisk://delegates/vote?votes=nimbus) for Lisk
Delegate.  
Also, donations to
[12313256070705265970L](lisk://wallet?recipient=12313256070705265970L) are
greatly appreciated!
