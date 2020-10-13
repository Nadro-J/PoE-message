import json, requests
from utils import parsing

class Rpc:
    def __init__(self):
        config = parsing.parse_json(r".\\config.json")["rpc"]
        self.recipients = {}
        self.rpc_host = config["rpc_host"]
        self.rpc_port = config["rpc_port"]
        self.rpc_user = config["rpc_user"]
        self.rpc_pass = config["rpc_pass"]
        self.serverURL = 'http://' + self.rpc_host + ':' + self.rpc_port
        self.headers = {'content-type': 'application/json'}

    # OP_RETURN message project
    # listunspent on specified address where input is between 1 and 20000 confirmations
    def listunspent(self, address):
        payload = json.dumps({"method": "listunspent", "params": [1, 20000, [address]], "jsonrpc": "2.0"})
        response = requests.post(self.serverURL, headers=self.headers, data=payload,
                                 auth=(self.rpc_user, self.rpc_pass))
        return response.json()['result']

    def createrawtransaction(self, txid, vout, address, amount, data):
        payload = json.dumps({"method": "createrawtransaction", "params": [[{"txid": txid, "vout": vout}], [{address: amount}, {"data": data}]], "jsonrpc": "2.0"})
        response = requests.post(self.serverURL, headers=self.headers, data=payload,
                                 auth=(self.rpc_user, self.rpc_pass))
        return response.json()['result']

    def signrawtransactionwithkey(self, txhex, private_key, txid, vout, scriptPubKey, amount):
        payload = json.dumps({"method": "signrawtransactionwithkey", "params": [txhex, [private_key], [{"txid": txid, "vout": vout, "scriptPubKey": scriptPubKey, "amount": amount}]], "jsonrpc": "2.0"})
        response = requests.post(self.serverURL, headers=self.headers, data=payload,
                                 auth=(self.rpc_user, self.rpc_pass))
        return response.json()['result']

    def sendrawtransaction(self, hexstring):
        payload = json.dumps({"method": "sendrawtransaction", "params": [hexstring], "jsonrpc": "2.0"})
        response = requests.post(self.serverURL, headers=self.headers, data=payload,
                                 auth=(self.rpc_user, self.rpc_pass))
        return response.json()['result']

    def fundrawtransaction(self, hexstring):
        payload = json.dumps({"method": "fundrawtransaction", "params": [hexstring], "jsonrpc": "2.0"})
        response = requests.post(self.serverURL, headers=self.headers, data=payload,
                                 auth=(self.rpc_user, self.rpc_pass))
        return response.json()['result']