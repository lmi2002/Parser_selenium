import xml.etree.ElementTree as ET
import csv

tree = ET.parse(r'C:\Users\anokhin\Desktop\cat.xml')
root = tree.getroot()

f = open(r'C:\Users\anokhin\Desktop\test.csv', 'w', newline='', errors='ignore')

csvwriter = csv.writer(f,  delimiter=';')

head = ['Title', 'Shortname', 'Category', 'Description', 'Img', 'Price']

csvwriter.writerow(head)

for item in root.findall('item'):
    row = []
    title = item.find('title').text.replace('\n', '')
    row.append(str(title))
    shortname = item.find('shortname').text.replace('\n', '')
    row.append(str(shortname))
    category = item.find('category').text.replace('\n', '')
    row.append(str(category))
    description = item.find('description').text.replace('\n', '')
    row.append(str(description))
    img = item.find('img').text.replace('\n', '')
    row.append(str(img))
    price = item.find('price').text.replace('\n', '')
    row.append(str(price))
    csvwriter.writerow(row)

f.close()

