class Txt:
    def __init__(self):
        self.lst = []

    # Return list string w/o '\n'
    def reader_file_txt(self, path_file):
        with open(path_file, 'r', newline='') as tf:
            data = tf.readlines()
            self.lst = [string[:-1] for string in data]

        return self.lst

    @staticmethod
    def writer_file_txt(path_file, dct):
        with open(path_file, 'a', newline='\n', ) as tf:
            for item in dct:
                tf.write(item + '\n')




