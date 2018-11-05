import csv


class Csv:

    def record_to_csv(self, name_file=None, s_fieldnames=None):

        """
            name_file - name of file
            sfieldnames - list of column names
            data_list - list of data to record to file
        """
        with open(str(name_file) + '.csv', 'w', newline='', ) as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=s_fieldnames)
            writer.writeheader()
            writer.writerow()






c = Csv()
c.record_to_csv('12345_febi', ['K', 'l'])