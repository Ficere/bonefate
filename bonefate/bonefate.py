from lunar_python import Lunar, Solar
from .utils import *


class BoneFates:
    def __init__(self, year: int, month: int, day: int, hour: str, lunar: bool = False):
        if lunar:
            self.lunar = Lunar.fromYmd(year, month, day)
            self.solar = self.lunar.getSolar()
        else:
            self.solar = Solar.fromYmd(year, month, day)
            self.lunar = self.solar.getLunar()
        self.hour = hour
        self.time_24_hour = get_24_hour_time(DIZHI_REVERSE[hour])
    
    @property
    def bone_weight(self):
        return get_weight(self.lunar.getYear(), self.lunar.getMonth(), self.lunar.getDay(), self.hour)
    
    @property
    def poem(self):
        return WEIGHTS_POEMS[self.bone_weight]
