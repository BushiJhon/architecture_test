import threading
import time
import random

quanju = 0
kongzhi =0
tingzhi = 0
target = 0
server_list = [0.1145289,11.7792103290558,0.00233046213785807,2.17243901888529,0.0489664872487386,0.0887525876363118,1.66304032007853,4.32653212547302,14.72377626]
local_list = [0.475302076,11.56842785,0.121201587,9.744031239,0.106026363,0.380011678,3.469889379,3.617563391,21.28003609]
post_list = [0.026,0.031,0.017,0.018,0.022,0.019,0.049,0.029,0.028,0.017]
def getyanchi():
    global  quanju
    while kongzhi == 0:
        ping = random.randint(0,20)
        print("the ping will simulate in "+str(ping))
        time.sleep(ping)
        x = 0
        for i in range(target,len(local_list)):
            x = x + local_list[i]
        for j in range(target,len(server_list)):
            ping = post_list[target]+server_list[j]+post_list[-1]
        if ping>x:
            print("the Daemon thread choose to run in local")
        else:
            quanju = 1
            print("the Daemon thread choose to run in server")
            time.sleep(2)

def function_to_local1():
    global tingzhi
    if quanju == 0:
        print("function in local 1")
        time.sleep(local_list[0])
    else:
        tingzhi = 1
        print("function run server 1")

def function_to_local2():
    global tingzhi
    if quanju == 0:
        print("function in local 2")
        time.sleep(local_list[1])
    else:
        tingzhi = 1
        print("function run server 2")


def function_to_local3():
    global tingzhi
    if quanju == 0:
        print("function in local 3")
        time.sleep(local_list[2])
    else:
        tingzhi = 1
        print("function run server 3")


def function_to_local4():
    global tingzhi
    if quanju == 0:
        print("function in local 4")
        time.sleep(local_list[3])
    else:
        tingzhi = 1
        print("function run server 4")

def function_to_local5():
    global tingzhi
    if quanju == 0:
        print("function in local 5")
        time.sleep(local_list[4])
    else:
        tingzhi = 1
        print("function run server 5")

def function_to_local6():
    global tingzhi
    if quanju == 0:
        print("function in local 6")
        time.sleep(local_list[5])
    else:
        tingzhi = 1
        print("function run server 6")

def function_to_local7():
    global tingzhi
    if quanju == 0:
        print("function in local 7")
        time.sleep(local_list[6])
    else:
        tingzhi = 1
        print("function run server 7")

def function_to_local8():
    global tingzhi
    if quanju == 0:
        print("function in local 8")
        time.sleep(local_list[7])
    else:
        tingzhi = 1
        print("function run server 8")

def function_to_local9():
    global tingzhi
    if quanju == 0:
        print("function in local 9")
        time.sleep(local_list[8])
    else:
        tingzhi = 1
        print("function run server 9")
fun = []
fun.append(function_to_local1)
fun.append(function_to_local2)
fun.append(function_to_local3)
fun.append(function_to_local4)
fun.append(function_to_local5)
fun.append(function_to_local6)
fun.append(function_to_local7)
fun.append(function_to_local8)
fun.append(function_to_local9)
t = threading.Thread(target=getyanchi)
t.setDaemon(True)
for i,func in enumerate(fun):
    if i == 0:
        t.start()
    fun = threading.Thread(target=func)
    target = i+1
    if tingzhi == 1:
        print("all run in server")
        break
    fun.start()
    fun.join()
kongzhi =1
