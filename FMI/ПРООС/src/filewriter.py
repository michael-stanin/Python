

class FileWriter:
    
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def write(file_name, *args):
        # Write the user information.
        with open(file_name, "a") as f:
            # Consider using csv files instead maybe ?
            f.write("\t".join("{0:10}".format(arg) for arg in args))
            f.write("\n")
