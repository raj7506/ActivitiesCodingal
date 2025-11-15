import os
def shutdown(answer):
    
    if answer == "yes":
        print("Shutting down...")
    elif answer == "no":
        print("Okay! The computer will not shut down")
    else:
        print("Sorry, I didn't understand")
#    os.system("shutdown /s /t 0")
ans = input("Do you want to shut down your computer? (yes/no): ")
shutdown(ans)