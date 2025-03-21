import csv
import os.path
folderPath = "C:/Vic/scheduler/EC/TC5856/SPIP1/5-Master dwidth/"
path = "C:/Vic/scheduler/EC/TC5856/SPIP1/5-Master dwidth/SPI1_MASTER_8bit_HIGH_ALTERNATE_DWDITH_CSHIGH.csv"
ext = '.csv'
prefix = 'SPI1'

csvCnt = 0
csvPath = []
"""
Get the folder all csv path
"""
files_and_dirs = os.listdir(folderPath)
# print(files_and_dirs)
for item in files_and_dirs:
    full_path = os.path.join(folderPath, item)
    # print(item)
    if os.path.isfile(full_path) and item.endswith(ext) and item.startswith(prefix):
        csvCnt = csvCnt + 1
        csvPath.append(item)
        # print(item)
# print(csvCnt)

'''read each csv content'''
cnt = 0
data = ['0', 'Module 0']
for item in csvPath:
    full_path = os.path.join(folderPath, item)
    with open(full_path, mode='r', newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    with open(full_path, mode='w', newline="") as csvfile:
        print(rows[7])
        rows[7] = data
        print(rows[7])

        writer = csv.writer(csvfile)
        writer.writerows(rows)

    cnt = cnt + 1
    if cnt == 1:
        break