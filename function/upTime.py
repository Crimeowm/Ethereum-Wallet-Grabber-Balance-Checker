from datetime import timedelta
from time import time


class upTime:
    def __init__(self) -> None:
        self.start = time()

    def upTime(self) -> timedelta:
        upTime = self.chop_microseconds(timedelta(seconds=time() - self.start))
        return upTime

    def per_seconds(self, wallets) -> dict:
        Time = self.upTime().total_seconds()
        if wallets and int(Time):
            data = []
            wallets_seconds = wallets/int(self.upTime().total_seconds())
            data.extend([self.upTime(), int(wallets_seconds), 0])
            if self.upTime().total_seconds() > 60:
                wallets_min = wallets / int((self.upTime().total_seconds())/60)
                data[2] = int(wallets_min)

            return data
        else:
            return [self.upTime(), 0, 0]

    def chop_microseconds(self, delta):
        return delta - timedelta(microseconds=delta.microseconds)
