
import os

def isConnected():
    ping = os.system('ping www.baidu.com')
    if ping:
        print('Not connected to the Internet')
        return False
    else:
        print('Already connected to the Internet')
        return True
if __name__ == '__main__':
    isConnected()
