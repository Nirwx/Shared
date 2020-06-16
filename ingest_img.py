import os
import time, datetime
from openpyxl import load_workbook
import shutil
import sys

# wb = load_workbook(filename = file_path)
# sheet_ranges = wb['banners'] #name of sheet itself
# print(sheet_ranges['E1102'].value)
def user_input(value_type, x):
    loop_param = True
    while loop_param:
        value_to_return = input('Enter {} value {} or type "Done" to proceed').format(value_type, x)
        if value_to_return == 'Done' or 'done':
            loop_param = False
        else:
            return value_to_return

def determine_working_directory():

    now = datetime.datetime.now()
    #weeknb = (now.isocalendar()[1])
    weeknb = '29'# Testing purpose
    year = now.year
    working_dir = 'O:\some_dir\some_dir\some_dir\{}\Week {}\\'.format(year, weeknb)
    return working_dir


def create_lab_directory():

    today_date = time.strftime('%Y%m%d')
    dir_path = 'C:\edit\\{}\\'.format(today_date) #temp_path
    if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            os.makedirs(dir_path + 'Radio\\Images')
            os.makedirs(dir_path + 'TV Guide\\Images')
            os.makedirs(dir_path + 'TV Search\\Images')
    return dir_path


def process_data(image_dir, lab_dir, asset_dict, title, crid):
    bmp_dir = image_dir + 'Images\\' + '239x53\\'
    jpg_dir = image_dir + 'Images\\' + '300x58\\'
    bmp_files = os.listdir(bmp_dir)
    jpg_files = os.listdir(jpg_dir)
    i = 0
    y = 0
    next_xml = [1, 2, 0]

    try:
        for file in bmp_files:
            bmp_path = bmp_dir + file
            bmp_dest_path = '{}TV Guide\\Images\\NL_TVOD_0{}.bmp'.format(lab_dir, i)
            shutil.copyfile(bmp_path, bmp_dest_path)
            build_xml(lab_dir + "TV Guide", i, title[i], crid[i], next_xml[i])
            i += 1
        for file in jpg_files:
            jpg_path = jpg_dir + file
            jpg_dest_path1 = '{}Radio\\Images\\NL_TVOD_0{}.jpg'.format(lab_dir, y)
            jpg_dest_path2 = '{}TV Search\\Images\\NL_TVOD_0{}.jpg'.format(lab_dir, y)
            shutil.copyfile(jpg_path, jpg_dest_path1)
            build_xml(lab_dir + "Radio", y, title[y], crid[y], next_xml[y])
            shutil.copyfile(jpg_path, jpg_dest_path2)
            build_xml(lab_dir + "TV Search", y, title[y], crid[y], next_xml[y])
            y += 1
    except Exception as e:
        print("Exception: {}".format(e))


def build_xml(path, img_nb, title, crid, next_xml):
    xml_format = '<advert>\n' \
                 '<image href="http://some_ip/some_dir/some_dir/some_dir/some_dir/Images/img_file{}.jpg"/>\n' \
                 '<label value="{}"/>\n' \
                 '<duration value="6000"/>\n' \
                 '<action name="launchHyperlink">\n' \
                 '<parameter name="ondemand" value="itv://some_dir/some_dir/some_dir/some_dir?id={}&amp;content=none&amp;theme=Default"/>\n' \
                 '</action>\n' \
                 '<next href="http://some_ip/some_dir/some_dir/some_dir/xml{}"/>\n' \
                 '</advert>'.format(img_nb, title, crid, next_xml)
    print(path)
    with open(path, 'a') as f:
        f.write(xml_format)
        f.close()


def user_input():
    i = 0
    x = 1
    asset_dict = {}
    while True:
        title = input('Enter Title value {} or type "Done" to proceed: '.format(x))
        if title != 'Done':
            print(title)
            crid = input('Enter Crid value {} or type "Done" to proceed: '.format(x))
            if crid != "Done":
                asset_dict.update({title: crid})
                print(asset_dict[title]) 
                i +=1
                x += 1
                continue
            else:
                break
        else:
            break
    return asset_dict

asset_dict = user_input()
working_dir = determine_working_directory()
lab_dir = create_lab_directory()
for key, value in asset_dict.items():
    process_data(working_dir, lab_dir, asset_dict, key, value)

