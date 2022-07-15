#!/usr/bin/python

import threading
import time

# # Define a function for the thread
# def print_time(threadname, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print("%s: %s" % ( threadname, time.ctime(time.time()) ))

# # Create two threads as follows
# try:
#    thread1 = threading.Thread(target=print_time, args=("Thread-1",2))
#    thread2 = threading.Thread(target=print_time, args=("Thread-2",4))
#    thread1.start()
#    thread2.start()
# except Exception as e:
#    print("Error: unable to start thread")
#    print(e)


exitFlag = False

class MyThread(threading.Thread):
   def __init__(self, threadid, name, delay):
      threading.Thread.__init__(self)
      self.threadid = threadid
      self.name = name
      self.delay = delay
   def run(self):
      print("Starting " + self.name)
      # Get lock to synchronize threads
      threadlock.acquire()
      print_time(self.name, 5, self.delay)
      # Free lock to release next thread
      threadlock.release()

def print_time(threadname, counter, delay):
   while counter:
      if exitFlag:
         threadname.exit()
      time.sleep(delay)
      print( "%s: %s" % (threadname, time.ctime(time.time())) )
      counter -= 1

threadlock = threading.Lock()
threads = []

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()

print( "Exiting Main Thread" )