class Information:
    def __init__(self, info_type):
        self.info_type = info_type

    def print_information(self, info_name):
        print(self.info_type.INFO_MAP[info_name])

