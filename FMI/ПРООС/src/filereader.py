from re import sub


class FileReader:

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def read_users(file_name):
        users = []
        with open(file_name, "r") as f:
            # Consider using csv files instead maybe ?
            users = f.readlines()
        return [sub("\t", " ", user).rstrip() for user in users]

    @staticmethod
    def read_units(file_name):
        units = []
        with open(file_name, "r") as f:
            units = f.readlines()
        return [sub("\_*", "", unit).rstrip() for unit in units]
        
