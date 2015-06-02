from application import Application

class Initializer:

    def __init__(self, *args, **kwargs):
        pass
    
    @staticmethod
    def start_up():
        # Create a new window for the application
        app = Application()
        
        # Draw the window and start the application
        app.mainloop()



if __name__ == "__main__":
    Initializer.start_up()
        
