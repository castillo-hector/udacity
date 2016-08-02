import time
import webbrowser

total_breaks = 3
break_count = 0

print("Start Counter")
while break_count < total_breaks:
    time.sleep(2*60*60)
    webbrowser.open("https://youtu.be/bi4tPIVL7RQ?t=5s")
    break_count = break_count + 1
    print"Launch break num: ", break_count
    
