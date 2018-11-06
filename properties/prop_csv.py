import csv
import io

class Csv:

    def record_to_csv(self, name_file=None, s_fieldnames=None, data_list=None, path_to_directory=None):

        """
            name_file - name of file
            sfieldnames - list of column names
            data_list - list of data to record to file
            path_to_directory - the path to the folder
        """
        with open(path_to_directory + '\\' +str(name_file) + '.csv', 'w', newline='', encoding='Cp1252') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=s_fieldnames)
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)





