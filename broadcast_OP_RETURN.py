import json
import codecs
from utils import rpc_module, parsing

RPC = rpc_module.Rpc()

# pick the last UTXO visible on listunspend
def txid_vout(address: str=''):
    unspentTx = RPC.listunspent(address)
    tUTXO = len(unspentTx)
    return parsing.parse2json(unspentTx[tUTXO - 1])

def hexify_message(msg):
    return codecs.encode(msg.encode(), 'hex')

if __name__ == '__main__':
    print("""
 ____  ____   ___   ___  _____       ___  _____        ___ __ __ ____ ___________  ____ ____     __   ___ 
|    \|    \ /   \ /   \|     |     /   \|     |      /  _|  T  l    / ___|      T/    |    \   /  ] /  _]
|  o  |  D  Y     Y     |   __j    Y     |   __j     /  [_|  |  ||  (   \_|      Y  o  |  _  Y /  / /  [_ 
|   _/|    /|  O  |  O  |  l_      |  O  |  l_      Y    _l_   _j|  |\__  l_j  l_|     |  |  |/  / Y    _]
|  |  |    \|     |     |   _]     |     |   _]     |   [_|     ||  |/  \ | |  | |  _  |  |  /   \_|   [_ 
|  |  |  .  l     l     |  T       l     |  T       |     |  |  |j  l\    | |  | |  |  |  |  \     |     T
l__j  l__j\_j\___/ \___/l__j        \___/l__j       l_____|__j__|____j\___j l__j l__j__l__j__j\____l_____j
PoE is a utility built into most blockchains that allow anyone to store records in an immutable fashion.
    """)
    write2block = input('OP_Return Message: ')

    UTXO = json.loads(txid_vout(""))
    MESSAGE = hexify_message(write2block)
    transact = 0.0001
    privateKey = ""

    # Output the UTXO that's been selected
    print(f""" 
    ----- [ selected vout / hex message ] ---------
    txid: {UTXO['txid']}
    vout: {UTXO['vout']}
    address: {UTXO['address']}
    scriptPubKey: {UTXO['scriptPubKey']}
    ----- [ ascii / hex message ] -----------------
    ASCII: {write2block}
    hex-data: {MESSAGE.decode()}
    -----------------------------------------------
    """)

    # Create -> Fund -> Sign -> Send
    cRawTx = RPC.createrawtransaction(UTXO['txid'], UTXO['vout'], UTXO['address'], transact, MESSAGE.decode())
    fundTx = RPC.fundrawtransaction(cRawTx)['hex']
    signTx = RPC.signrawtransactionwithkey(fundTx, privateKey, UTXO['txid'], UTXO['vout'], UTXO['scriptPubKey'], transact)['hex']
    sendTx = RPC.sendrawtransaction(signTx)
    print(f'Transaction ID: {sendTx}')