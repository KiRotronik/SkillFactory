from mod_1 import *
def main():
   c = int(input("Enter circle radius"))
   a = int(input("Enter rectangle 1 side"))
   b = int(input("Enter rectangle 2 side"))
   if circ_area(c) > rec_area(a,b):
       print('Circle is larger')
   else:
       print('Rectangle is larger')


if __name__ == '__main__':
     main()