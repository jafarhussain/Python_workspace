import re
with open("Mobile.txt") as f1:
    lst1=f1.readlines()
    print(lst1)
    lst1 = [x.replace("\r\n","") for x in lst1]
    print(lst1)


    for val in lst1:
         
        if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
            print('yes')
        else:
            print('no')