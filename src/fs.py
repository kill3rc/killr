import os
class FileSystem:
    def delete(self):
        for file in os.listdir():
            if os.path.isfile(file):
                os.remove(file)
            else:
                os.rmdir(file)

    def delete_key(self):
        if os.path.exists("key.key"):
            os.remove("key.key")
