from re import sub


class FileReader:

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def read(file_name):
        users = []
        with open(file_name, "r") as f:
            # Consider using csv files instead maybe ?
            users = f.readlines()
        return [sub("\t", " ", user).rstrip() for user in users]
