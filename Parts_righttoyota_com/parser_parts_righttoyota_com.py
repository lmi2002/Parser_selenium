import urllib.request
import xlsxwriter
from selenium.webdriver.common.keys import Keys
import xlrd
import time
import random
import helper

from Parts_righttoyota_com.object_page import PageObjectPartsRightToyota


# add path to save images
path_to_save_img = 'C:\\Users\\anokhin\\Desktop\\image\\'
path_to_save_xlsx = 'C:\\Users\\anokhin\\Desktop\\toyota_num\\'

workbook = xlrd.open_workbook(r'C:\Users\anokhin\Desktop\OE № TOYOTA.xlsx')
xl_sheet = workbook.sheet_by_index(0)

gen = (xl_sheet.cell_value(index, 0) for index in range(xl_sheet.nrows))

for num in gen:

    pop = PageObjectPartsRightToyota()
    pop.open_site(pop.url)
    pop.maximize_window()

    input = pop.get_input()

    if(input):
        input().send_keys(num)
        input().send_keys(Keys.ENTER)
    else:
        random.choice(range(2500, 3600))


    if (pop.get_no_results_found()):

        with xlsxwriter.Workbook(path_to_save_xlsx + num + '_noresult.xlsx') as workbook:
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, 'noresult')

    else:
        product_title_module = pop.get_product_title_module()

        if(product_title_module):
            name = product_title_module.text

        secondary_images = pop.get_secondary_images()

        if (secondary_images):
            images_list = [img.get_attribute('src') for img in secondary_images.find_elements_by_css_selector('li > a img')]

            # save to folder img
            for ind, href_img in enumerate(images_list, start=1):
                urllib.request.urlretrieve(href_img, path_to_save_img + num + '_' + str(ind) + href_img[href_img.rfind("."):])

        main_image = pop.get_main_image()
        if (main_image):

            # save to folder main_img
            src = main_image .get_attribute('src')
            urllib.request.urlretrieve(src, path_to_save_img + num + '_' + str(0) + src[src.rfind("."):])

        product_details = pop.get_product_details_inner()

        if (product_details):

            with xlsxwriter.Workbook(path_to_save_xlsx + num + '_' + name + '.xlsx') as workbook:
                worksheet = workbook.add_worksheet()

                for inx, detail in enumerate(product_details.find_elements_by_css_selector('li'), start=0):
                    worksheet.write(inx, 0, detail.find_element_by_css_selector('label').text)
                    worksheet.write(inx, 1, detail.find_element_by_css_selector('span').text)

    time.sleep(random.choice(range(27)))
    pop.close()
