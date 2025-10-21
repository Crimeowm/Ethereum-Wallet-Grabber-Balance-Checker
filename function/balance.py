from web3 import Web3
from time import sleep
from function import logger


class Balance:
    def __init__(self, apiKey=None, apiURL="ethereum-rpc.publicnode.com", apiType="https://") -> None:
        self.apiURL = apiURL
        self.apiKey = apiKey
        self.apiType = apiType
        self.w3 = self.__init_w3__()
        self.logger = logger.Logger()

    def __init_w3__(self):
        apiURL = f'{self.apiType}{self.apiURL}' if not self.apiKey else f'{self.apiType}{self.apiURL}/{self.apiKey}'
        if self.apiType == "wss://":
            return Web3(Web3.WebsocketProvider(apiURL))
        elif self.apiType == "http://" or self.apiType == "https://":
            return Web3(Web3.HTTPProvider(apiURL))

    # def trigger_timeout(self):
    #     sleep(300)
    #     if self.w3 is None:
    #         self.w3 = self.__init_w3__
        
    def w3_balance(self, address, mnemonic):
        # if not self.w3.is_connected():
        #     if self.w3 is not None:
        #         self.w3 = None
        #         self.trigger_timeout()
        try:
            return self.w3.eth.get_balance(address)
        except Exception as e:
            self.logger.error(f'Failed to acquire balance: {repr(e)}')
            self.logger.info(f'Faild Wallet Scan {address} || {mnemonic}')
            raise Exception("FAIL", "BALANCE FAIL")
