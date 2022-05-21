from usb import core, util

device = core.find(find_all=True)

for config in device:
    # print('Vendor: {}'.format(config.idVendor))
    # print('Product: {}'.format(config.idProduct))
    print(util.get_string(config, 256, 1))

