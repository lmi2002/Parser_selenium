import csv
import io


class Csv:

    """
    The file for read must have four columns. Name columns : (brand_ex, brand_avtopro, num, index)

    """

    def read_to_csv(self, path_to_directory=None):

        lst_tmp = []
        with open(path_to_directory, 'r', newline='', errors='ignore', encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                lst_tmp.append(row)
            return lst_tmp

    def record_to_csv(self, name_file=None, s_fieldnames=None, data_list=None, path_to_directory=None):

        """
            name_file - name of file
            s_fieldnames - list of column names
            data_list - list of data to record to file
            path_to_directory - the path to the folder
        """
        with open(path_to_directory + '\\' +str(name_file) + '.csv', 'w', newline='', errors='ignore') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=s_fieldnames)
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)



    def create_empty_csv(self, name_file=None, path_to_directory=None):
        with open(path_to_directory + '\\' + str(name_file) + '.csv', 'w', newline='') as csvfile:
            pass

