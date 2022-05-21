import usb
from usb import core, util

busses = usb.busses()

for bus in busses:
    device = bus.device

    for dev in device:
        print(repr(dev))
        print("Device: ", dev.filename)
        print("   Vendor ID:  ", dev.idVendor)
        print("   Product ID: ", dev.idProduct)
        print("Manufacturer: ", dev.iManufacturer)
        print("Serial: ", dev.iSerialNumber)
        print("Product: ", dev.iProduct)
        
