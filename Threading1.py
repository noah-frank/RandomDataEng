# Used to perform multiple tasks concurrently
# Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time # Just to simulate each function taking time 

def walk_dog(first, last):
    # print("Started walking the dog")
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    # print("Started taking out trash")
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    # print("Started getting mail")
    time.sleep(4)
    print("You get the mail")

# start_time = time.time()
# # Running on the same thread 
# walk_dog() # Do this, then
# take_out_trash() # Do this, then
# get_mail() # Do this
# print("Single Thread ExecutionTime :", time.time() - start_time)

start_time = time.time()
# Running on separate threads
chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo")) # If only 1 arg, do "args=("Scooby",)" (end with comma)
chore1.start() # Do this, and

chore2 = threading.Thread(target=take_out_trash)
chore2.start() # Do this, and

chore3 = threading.Thread(target=get_mail)
chore3.start() # Do this, and

chore1.join()
chore2.join()
chore3.join()

print("Multi Thread ExecutionTime :", time.time() - start_time)