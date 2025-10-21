from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39SeedGenerator,
    Bip44,
    Bip44Coins,
    Bip44Changes,
    Bip39WordsNum,
)

class Bip44Gen:
    def __init__(self) -> None:
        pass
    
    def __bip(self):
        return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
    
    def __bip44_wallet_seed(self):
        seed = self.__bip()
        seed_bytes = Bip39SeedGenerator(seed).Generate()

        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    

        bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        return {
            "address": bip44_acc_ctx.PublicKey().ToAddress(),
            "seed": seed.ToStr(),
            "private": bip44_acc_ctx.PrivateKey().Raw().ToHex()
        }
    
    def bip44_generate(self, length=None) -> list:
        if length:
            data = {}
            for __ in range(length):
                wallet = self.__bip44_wallet_seed()
                data.update([(wallet["address"],
                    {"seed": wallet['seed'],
                    "private": wallet['private']
                })])

            return data
        else:
            return self.__bip44_wallet_seed()