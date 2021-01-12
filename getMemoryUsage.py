import os
import pandas as pd
import numpy as np
import time


def getMemoryUsage(serviceName):
    # Get current time and workpath
    currentPath = os.getcwd().replace('\\', '/')
    global currentTime
    # Store the begin time
    currentTime = time.strftime("%m%d%H%M")
    # Store the servicename
    global servicename
    servicename = serviceName

    # Create the Logman counter
    os.system('logman.exe create counter ' + serviceName + ' -f csv -si 5 -v mmddhhmm -o "' + currentPath + '\\Log_' + serviceName + '" -c "\Process('+serviceName+')\*"')

    # Create the csv file and start recording
    os.system('Logman start ' + serviceName)
    print('Start monitoring the memory Usage of ' + serviceName)
    print('The Log file is Log_' + serviceName)
    return 'Log_' + serviceName + '_' + currentTime + '.csv'


    """
    2.Start the script to auto change the profile for 1 minute
    """

def  checkTheResult(filename, condition=0):
    # return the memory usage and delete the file of not
    os.system('Logman stop ' + servicename)
    print('Stop monitoring the memory Usage of ' + servicename)

    # Read the latest data of memory usage
    targetDataArray = np.array(pd.read_csv(filename, usecols=[11]).tail(1))

    # Compare the data with the limit
    print('The Memory Usage of ' + servicename + ' is %s' % targetDataArray[0][0] + 'bytes')
    if (condition):
        # If the condition is qualified, save the csv file for check
        print("ALERT!")
        return True
    else:
        # If the condition is not qualified, delete the csv file
        os.remove('Log_' + servicename + '_' +currentTime + '.csv')
        return False


if __name__ == '__main__':


    filename = getMemoryUsage('DolbyAccess')
    checkTheResult(filename)
