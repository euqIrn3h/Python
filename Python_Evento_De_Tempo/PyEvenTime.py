import time
import asyncio
from threading import Thread as th
from datetime import datetime as dt


async def event_second() -> None:
    timetosecond = 100-int(str(dt.now().time())[9:11])
    while True:
        if not timetosecond:
            return True
        timetosecond -= 1
        await asyncio.sleep(0.01)

async def event_minute() -> None:
    timetominute = 60-int(str(dt.now().time())[6:8])
    while True: 
        if not timetominute:
            return True
        timetominute -= 1
        await asyncio.sleep(1)

async def event_hour() -> None:
    timetohour = 60-int(str(dt.now().time())[3:10])
    while True:
        if not timetohour:
            return True
        timetohour -= 1
        await asyncio.sleep(60)
      
def second() -> None:
    while True:
        if asyncio.run(event_second()):
            print("Your code per second")         

def minute() -> None:
    while True:
        if asyncio.run(event_minute()):
            print("Your code per minute")
            
def hour() -> None:
    while True:
        if asyncio.run(event_hour()):
            print("Your code per hour")

def main():
    thread0 = th(target=second)
    thread1 = th(target=minute)
    thread2 = th(target=hour)

    thread0.start()
    thread1.start()
    thread2.start()

#inserido o print nas funções apenas para demosntração
if __name__ == "__main__":
    main()

#Exemplo detalhado de Thread
#https://pt.stackoverflow.com/questions/143552/entendendo-o-conceito-de-threads-na-pr%C3%A1tica-em-python
#Documentação
#https://docs.python.org/3/library/threading.html



