'''
Created on Oct 6, 2019

Things to do:

    1) get a list of the files that are valid for log processing
        Name with:
            - FR1 or FR2
                and
            - n41 or n260
                and
            - Test or Bad or Medium
        
    2) Open the file in pandas
    3) Save output file using pandas


@author: CEVDEA
'''

'''
    Main program
'''

import datetime
import os
import pandas as pd

#Variables
filePath = r'C:\Users\cevdea\Desktop\PCTEL\pctel_scaner_export_csv_2'
combinedPath = r'C:\Users\cevdea\Desktop\PCTEL\combined'
combinedFile = 'combinedFile.csv'
frList = ['FR1', 'FR2']
bandList = ['n41', 'n260']
testList = ['Test', 'Bad', 'Medium', 'Mobility']
csvFile = 'csv'
flagFr = False
flagBand = False
FlagTest = False
testFileList_df = []

current_dt = datetime.datetime.now()
print ("**** Begin ****" + str(current_dt))

#Change path
os.chdir(filePath)

#Get the files on directory
baseFiles = os.listdir()
for item in baseFiles:
    if csvFile in item:
        for fr in frList:
            if fr in item:
                flagFr = True
                break
        for band in bandList:
            if band in item:
                flagBand = True
                break
        for test in testList:
            if test in item:
                FlagTest = True
                break
        if (flagFr and flagBand and FlagTest):
            flagFr = False
            flagBand = False
            FlagTest = False
            os.chdir(filePath)
            test_df = pd.read_csv(item)
            if 'MIB' in test_df.columns:
                test_df = test_df.drop(['MIB'], axis = 1)
            test_df['FR'] = fr
            test_df['Band'] = band
            test_df['Test'] = test
            newName = fr + '_' + band + '_' + test + '.csv'
            os.chdir(combinedPath)
            test_df.to_csv(newName, index = False)
            print(newName)
            testFileList_df.append(test_df)

combined_df = pd.concat(testFileList_df, ignore_index = True)
os.chdir(combinedPath)
combined_df.to_csv(combinedFile, index = False)
current_dt = datetime.datetime.now()

print ("**** End ****" + str(current_dt))
