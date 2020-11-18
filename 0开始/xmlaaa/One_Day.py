from multiprocessing import Process

import os

import time

def run_proc(name, age, **kwargs):

       for i in range(10):

              print("姓名是: %s, 年龄是: %s"% (name, age))

              print(kwargs)

              time.sleep(0.3)

if __name__ == "__main__":

       p = Process(target=run_proc,args=("王多鱼", 20))

       p.start()