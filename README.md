![alt text](https://i.imgur.com/uYr1lbS.png)
> Transaction containing OP_RETURN data: https://bitg.polispay.com/tx/39d808d9f9c03986dab4fde64eac6d4ff67088a875e5e86cbee909ed0ef78fc2

![alt text](https://i.imgur.com/8kuddeD.png)
****

#### Install Python3
> https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe

#### Setting up PoE-message
1. Modify config.json to match your wallet configuration in bitgreen.conf

inside broadcast_OP_RETURN.py modify the following lines
```python
line 29: UTXO = json.loads(txid_vout(""))
line 32: privateKey = ""
```
To get the private key of the address you want to use, open up the console **(Tools > Console)** and type `dumpprivkey <address>`

#### Run broadcast_OP_RETURN.py
1. Open PowerShell and navigate to the working directory and type: `py .\broadcast_OP_RETURN.py`
2. Write message (limited to 40 characters) that you want to store on the blockchain
