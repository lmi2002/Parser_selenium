from properties import prop_txt


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

    t = prop_txt.Txt()

    lst = t.reader_file_txt(r'C:\Users\anokhin\Desktop\side.txt')

    #import ipdb; ipdb.set_trace()
    uniq_list = compare_str(lst)
    out_data = dict(zip(lst, uniq_list))
    print(out_data)


    t.writer_file_txt(r'C:\Users\anokhin\Desktop\side1.txt', out_data)
