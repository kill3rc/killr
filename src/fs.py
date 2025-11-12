class FileSystem:
    def delete(self):
        for file in os.listdir():
            if os.path.isfile(file):
                os.remove(file)
            else:
                os.rmdir(file)
