import time
def countdown(t):
    while t > 0:
        print(t)
        t -=1
        time.sleep(1)
    print("BLAST OFF")
print("How many seconds to countdown? Enter number: ")
seconds=input()
while not seconds.isdigit():
    print("That wasnt an interger,Enter an interger:")
    seconds=input()
seconds=int(seconds)
countdown(seconds)