from application import Application

class Initializer:

    def __init__(self, *args, **kwargs):
        pass

    def start_up(self):
        # Create a new window for the application
        self.app = Application()

        # Draw the window and start the application
        self.app.mainloop()




if __name__ == "__main__":
    init = Initializer()
    init.start_up()
        
