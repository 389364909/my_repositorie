
import re
import os
def find():
    os.chdir('/home/jimi/Documents/github/test2')
    f = open("find.txt","r",encoding="utf-8") 
    r = re.compile(r'(?<=\D)[0-9]{3}(?=\D)')
    s = re.findall(r,f.read())
    print(s)
    f.close()
if __name__ == "__main__":
    find()
    
