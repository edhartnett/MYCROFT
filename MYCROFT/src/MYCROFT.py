import os

class MYCROFT:
    def __init__(self):
        self.name = "MYCROFT"
        self.version = "1.0"
        self.author
        self.description = "A simple AI assistant"
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = self.path + "/config"
        self.data = self.path + "/data"
        self.logs = self.path + "/logs"

    def main():
        print("Hello, I am MYCROFT, your personal assistant")
    
if __name__ == "__main__":
    MYCROFT.main()
