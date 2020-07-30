
import re

def find():
    f = open("找三位数.txt","r",encoding="utf-8") 
    s = re.findall(r'(?<=\D)[0-9]{3}(?=\D)',f.read())
    print(s)
    f.close()
if __name__ == "__main__":
    find()
    
