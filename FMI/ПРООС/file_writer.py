

class FileWriter:
    
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def write(file_name, *args):
        # Write the user information.
        with open(file_name, "a") as f:
            f.write("\t".join("{}".format(arg) for arg in args))
            f.write("\n")
