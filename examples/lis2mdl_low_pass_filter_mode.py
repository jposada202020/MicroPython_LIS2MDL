# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis2mdl import lis2mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis2mdl.LIS2MDL(i2c)

lis.low_pass_filter_mode = lis2mdl.LPF_ENABLED

while True:
    for low_pass_filter_mode in lis2mdl.low_pass_filter_mode_values:
        print("Current Low pass filter mode setting: ", lis.low_pass_filter_mode)
        for _ in range(10):
            mag_x, mag_y, mag_z = lis.magnetic
            print(f"X:{mag_x:.2f}, Y:{mag_y:.2f}, Z:{mag_z:.2f} uT")
            print()
            time.sleep(0.5)
        lis.low_pass_filter_mode = low_pass_filter_mode
