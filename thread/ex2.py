import os
from threading import Thread
from time import sleep

class myclass():
    def help(self):
        a = [1,2,3,4,5,6,7,8,9]
        for i in a:
            os.system('echo \"asfasdflj sadjfdfd '+str(i)+'\"')
            sleep(2)

    def nope(self):
        a = [1,2,3,4,5,6,7,8,9]
        for i in a:
            print(i)
            sleep(1)

if __name__ == "__main__":
    abc = myclass()
    thread1 = Thread(target = abc.help)
    thread2 = Thread(target = abc.nope)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Finished")