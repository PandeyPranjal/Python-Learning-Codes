#10. Exponential Backoff
#Problem: Implement an exponential backoff strategy that doubles the  wait time between retries, starting from 1 second, but stops after 5 retries. 

import time
max_retries=5
attmepts=0
wait_time=1

while attmepts<max_retries:
    print("Attempt", attmepts+1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attmepts+=1