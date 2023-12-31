# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis2mdl import lis2mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis2mdl.LIS2MDL(i2c)

lis.operation_mode = lis2mdl.ONE_SHOT

while True:
    for operation_mode in lis2mdl.operation_mode_values:
        print("Current Operation mode setting: ", lis.operation_mode)
        for _ in range(10):
            mag_x, mag_y, mag_z = lis.magnetic
            print(f"X:{mag_x:.2f}, Y:{mag_y:.2f}, Z:{mag_z:.2f} uT")
            print()
            time.sleep(0.5)
        lis.operation_mode = operation_mode
