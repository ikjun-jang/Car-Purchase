from enum import IntEnum

class Battery(IntEnum):
    KWH_40 = 1
    KWH_60 = 2
    KWH_80 = 3

class Wheel(IntEnum):
    MODEL_1 = 1
    MODEL_2 = 2
    MODEL_3 = 3

class Tire(IntEnum):
    ECO = 1
    PERFORMANCE = 2
    RACING = 3