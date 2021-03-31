#import cs50
#from cs50 import get_int

def main():
    while True:
        print("Height: ", end="")
        height, height = int(input()), input()  
        if height >= 1 and height <= 8:
            break
            
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end = "")
        for k in range(i + 1):
            print("#", end = "")
        print("")
main()    

#if _name_ == "_main_":
    #m ain()