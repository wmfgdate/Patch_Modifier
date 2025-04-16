import csv
import os.path

# FolderPath Configuration 
basePath = "C:/Vic/scheduler/EC/"
chipName = "TC5856"
moduleName = "SPIP1"
testItemName = "27-Slave single dual LSB"
folderPath = os.path.join(basePath, chipName, moduleName, testItemName)

# Configure files prefix & extension
prefix = 'SPI1' # for check each files's prefix.
ext = '.csv'    # for check each files's extension.

testMode = True # only process 1 item when enable

def getCsvPath(folderPath) -> list:
    '''Get matched csv path'''
    csvCnt = 0 # how much csv file match in the folderPath
    csvPath = [] # store all match file's path

    files_and_dirs = os.listdir(folderPath)
    # print(files_and_dirs) # type(files_and_dirs) = list
    for item in files_and_dirs:
        fullPath = os.path.join(folderPath, item)
        # print(item)
        if os.path.isfile(fullPath) and item.endswith(ext) and item.startswith(prefix):
            csvCnt = csvCnt + 1
            csvPath.append(item)
            # print(item)
    print("{} file matched".format(len(csvPath)))
    return csvPath


"""
read each csv content
"""
def modifyCsvContent(csvPath:list, index:int, replaceData:list[list[str]]):
    '''
    modify the content
    Args:
        csvPath(list): input
    
    '''
    cnt = 0
    for item in csvPath:
        fullPath = os.path.join(folderPath, item)
        with open(fullPath, mode='r', newline="") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        with open(fullPath, mode='w', newline="") as csvfile:
            print("{} row[{}] from {} ==> {}"
                  .format(item, index, rows[index], replaceData))
            rows[index] = replaceData

            #do write operation
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        cnt = cnt + 1
        if (testMode):
            break
    print("Process {} items. ".format(cnt))

if __name__ == '__main__':
    os.system('cls')
    print("In process path: ", folderPath)
    csvPath = getCsvPath(folderPath)

    index = 0 # which row would be modify
    replaceData = ['Interval_Time', '250'] # update the content to this content
    modifyCsvContent(csvPath, index, replaceData)