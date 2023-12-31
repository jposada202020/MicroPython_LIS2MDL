# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis2mdl import lis2mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis2mdl.LIS2MDL(i2c)

lis.low_power_mode = lis2mdl.LP_ENABLED

while True:
    for low_power_mode in lis2mdl.low_power_mode_values:
        print("Current Low power mode setting: ", lis.low_power_mode)
        for _ in range(10):
            magx, magy, magz = lis.magnetic
            print(f"X:{magx:.2f}, Y:{magy:.2f}, Z:{magz:.2f} uT")
            print()
            time.sleep(0.5)
        lis.low_power_mode = low_power_mode
