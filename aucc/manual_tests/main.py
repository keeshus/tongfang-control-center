"""
Manual test script for checking HID device communication.
Requires: pip install hidapi
"""

import sys
from typing import List

import hid

# Using same IDs as main application
VENDOR_ID = 0x048D
PRODUCT_ID = 0x6004


def run_manual_test() -> None:
    print(f"Opening the device: {VENDOR_ID:04X}:{PRODUCT_ID:04X}")

    try:
        h = hid.device()
        h.open(VENDOR_ID, PRODUCT_ID)

        print(f"Manufacturer: {h.get_manufacturer_string()}")
        print(f"Product: {h.get_product_string()}")
        print(f"Serial No: {h.get_serial_number_string()}")

        # enable non-blocking mode
        h.set_nonblocking(1)

        # Reset a color scheme
        h.send_feature_report([0x08, 0x02, 0x33, 0x00, 0x24, 0x00, 0x00, 0x00])
        # Setup mono_color
        h.send_feature_report([0x12, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00])

        green: List[int] = [0x00, 0x00, 0x00, 0xFF] * 16 + [0x00]

        for _ in range(8):
            h.write(green)

        print("Test sequence sent successfully.")
        h.close()

    except Exception as e:
        print(f"Error communicating with device: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_manual_test()
