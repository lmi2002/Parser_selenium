from properties import prop_txt
from helper import base_func
from properties.prop_csv import Csv

def compare_str(lst):

    uniq_list = []
    for item in lst:
        if ',' in item.lower():
            lower_item = item.lower()
            string = lower_item.split(', ')
            uniq = set(string)
            uniq_list.append(uniq)
        else:
            uniq_list.append(item)

    return uniq_list






if __name__ =='__main__':

    csv_obj = Csv()
    csv_obj.read_to_csv(r'C:\Users\anokhin\Desktop\tec_doc_2017_2_cross\tec_doc_2017_2_cross.csv')





