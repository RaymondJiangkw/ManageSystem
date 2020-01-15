# Get required information and send to connect.py
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup as bs
parent_directory = "C:\\WWW\\ManageSystem\\search\\function\\resources"
def get_data():
    data = [[],[],[],[],[],[],[],[],[],[],[]]
    file_list = [f for f in listdir(parent_directory) if isfile(join(parent_directory,f))]
    for file_name in file_list:
        with open(join(parent_directory,file_name),encoding = 'utf-8') as f:
            soup = bs(f.read(),'html.parser')
            parent_info = []
            for tr in soup.find_all("tr")[1:]:
                text = tr.text.replace(' ','')
                info = [ele for ele in text.split('\n') if ele != '']
                if (len(info) == 3):
                    parent_info[-3] = info[0]
                    parent_info[-2] = info[1]
                    parent_info[-1] = info[2]
                else:
                    parent_info = info
                # print(parent_info)
                data[0].append(parent_info[3])
                data[1].append(",".join(parent_info[4:-6]))
                data[2].append(int(parent_info[-4]))
                data[3].append(parent_info[-1])
                data[4].append("")
                data[5].append(parent_info[1])
                data[6].append("BJTU")
                data[7].append(parent_info[2])
                data[8].append(parent_info[-6])
                data[9].append(parent_info[-2])
                data[10].append(parent_info[-3])
    return data
