#!/usr/bin/python

import queue
import threading
import time

exitFlag = 0

class MyThread (threading.Thread):
   def __init__(self, threadid, name, q):
      threading.Thread.__init__(self)
      self.threadid = threadid
      self.name = name
      self.q = q
   def run(self):
      print("Starting " + self.name)
      process_data(self.name, self.q)
      print("Exiting " + self.name)

def process_data(threadname, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         # Extrat data in the queue one by one to be processed synchronously by threads
         data = q.get()
         queueLock.release()
         print( "%s processing %s" % (threadname, data) )
      else:
         queueLock.release()
      time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(len(nameList))
threads = []
threadid = 1

# Create new threads
for tName in threadList:
   thread = MyThread(threadid, tName, workQueue)
   thread.start()  # Thread will run and go to the 'else' statement in the while loop until queue is filled
   threads.append(thread)
   threadid += 1

# Fill the queue
# Feeze threads while computing that operation
queueLock.acquire()
for word in nameList:
   # As we lock the threads while the queue is filled, if length of queue too short then process is frozen
   # Cause no item will be popped from the queue to allow for new entries in the meantime
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
# Only when empty allow flag to switch to end process
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()

print( "Exiting Main Thread" )