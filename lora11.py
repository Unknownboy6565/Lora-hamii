
import os, sys, time
import os
os.system("clear")
P = '\x1b[91m'
H = '\x1b[95m'
G = '\x1b[97m'
K = '\x1b[92m'
logo = """

  _    _                 _ _                
 | |  | |               (_|_)               
 | |__| | __ _ _ __ ___  _ _                
 |  __  |/ _` | '_ ` _ \| | |               
 | |  | | (_| | | | | | | | |               
 |_|  |_|\__,_|_| |_| |_|_|_|               
  _____  ______ _____   ____  _____ _______ 
 |  __ \|  ____|  __ \ / __ \|  __ \__   __|
 | |__) | |__  | |__) | |  | | |__) | | |   
 |  _  /|  __| |  ___/| |  | |  _  /  | |   
 | | \ \| |____| |    | |__| | | \ \  | |   
 |_|  \_\______|_|     \____/|_|  \_\ |_|   
                                            
                                            
 """
def Loads():
    for i in range(101):
        time.sleep(0.3)
        sys.stdout.write(G + '\r[+] ' + P + 'PLZZ WAIT : %d%%' % i)
        sys.stdout.flush()


def Report():
    for d in range(101):
        time.sleep(0.2)
        sys.stdout.write(G + '\r[*] ' + P + 'REPORT PROCESSING ... [%d%%] ' % d)
        sys.stdout.flush()

print '-' * 49 + H
os.system('figlet "HAMII"')

print P + '=' * 49
B = raw_input(G + '[+]' + K + ' PUT REPORT ID LINK   : ')
print '=' * 49
if not B.startswith('1000'):
    print '[!] LINK INVILED'
    sys.exit()
    print '=' * 49
Loads()
time.sleep(3)
print ''
print '=' * 49
a = 1
while True:
    print ('{}[-] {}REPORTING PROCESS DONE [{}] => {}{}').format(G, P, a, H, B)
    print ('{} | {}[+]{} SUCCESS').format(Report(), K, G)
    print '=' * 49
    a += 1

