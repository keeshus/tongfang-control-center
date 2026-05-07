"""
Copyright (c) 2019, Rodrigo Gomes.
Distributed under the terms of the MIT License.
The full license is in the file LICENSE, distributed with this software.
Created on May 27, 2019
@author: @rodgomesc
"""
import sys
from typing import Optional, Union

import usb.core
import usb.util


class Device:
    def __init__(self, vendor_id: int, product_id: int) -> None:
        self._device = self._get_device(vendor_id, product_id)
        self.interface_id = self._get_interface()
        cfg = self._device.get_active_configuration()

        self.in_ep = self._get_endpoint(cfg[(1, 0)], usb.util.ENDPOINT_IN)
        self.out_ep = self._get_endpoint(cfg[(1, 0)], usb.util.ENDPOINT_OUT)

    def _get_device(self, vendor: int, product: int) -> usb.core.Device:
        device = usb.core.find(idVendor=vendor, idProduct=product)
        if device is None:
            raise ValueError("Device not found")

        # in linux interface is 1, in windows 0
        if not sys.platform.startswith("win"):
            if device.is_kernel_driver_active(1):
                device.detach_kernel_driver(1)

        return device

    def _get_interface(self) -> None:
        return None

    def _get_endpoint(self, intf, ep_type: int) -> Optional[usb.core.Endpoint]:
        return usb.util.find_descriptor(
            intf,
            custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress)
            == ep_type,
        )


class DeviceHandler(Device):
    def __init__(self, vendor_id: int, product_id: int) -> None:
        super().__init__(vendor_id, product_id)
        self.bmRequestType = 0x21
        self.bRequest = 0x09
        self.wValue = 0x300
        self.wIndex = 1

    def ctrl_write(self, *payload: Union[int, bytes]) -> None:
        self._device.ctrl_transfer(
            self.bmRequestType, self.bRequest, self.wValue, self.wIndex, payload
        )

    def bulk_write(self, times: int = 1, payload: Optional[bytes] = None) -> None:
        if payload is None:
            return
        for _ in range(times):
            self._device.write(self.out_ep, payload)
