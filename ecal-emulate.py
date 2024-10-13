#!/usr/bin/env python3

from facedancer         import main
from facedancer         import *

@use_inner_classes_automatically
class ECalDevice(USBDevice):

    vendor_id                : int  = 0x0957
    product_id               : int  = 0x0001

    manufacturer_string      : str  = "Agilent Technologies"
    product_string           : str  = "USB ECal Module"
    serial_number_string     : str  = "S/N 12346"
    device_speed             : DeviceSpeed = DeviceSpeed.FULL

    class ECalConfiguration(USBConfiguration):

        class ECalInterface(USBInterface):

            class ECalInEndpoint(USBEndpoint):
                number               : int                    = 1
                direction            : USBDirection           = USBDirection.IN
                transfer_type        : USBTransferType        = USBTransferType.BULK
                max_packet_size      : int = 64
                
                def handle_data_requested(self):
                    self.send(b"Hello!")

            class ECalOutEndpoint(USBEndpoint):
                number               : int                    = 1
                direction            : USBDirection           = USBDirection.OUT

                def handle_data_received(self, data):
                    print(f"Received data: {data}")

    @vendor_request_handler(number=2, direction=USBDirection.OUT)
    @to_device
    def handle_control_request_2(self, request):
        print(request)
        request.ack()


    @vendor_request_handler(number=4, direction=USBDirection.OUT)
    @to_device
    def handle_control_request_4(self, request):
        print(request)
        request.ack()


main(ECalDevice)
