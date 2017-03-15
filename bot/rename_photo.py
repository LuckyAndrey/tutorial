import os
import time

os.chdir('F:\\DCIM\\100CANON')
path_destination = ''
count = 0
for f in os.listdir():
    count+=1
    f_name, f_ext = os.path.splitext(f)
    t2 = os.path.getctime(f)
    f_year = (time.ctime(t2)).strip()[-4:]
    f_month = (time.ctime(t2)).strip()[4:7]
    f_day = (time.ctime(t2)).strip()[8:10]
    if int(f_day) >= 7:
       if f_month == 'Jul':
            print('\t \t\t\t *****************************************************')

    print('{}{}  {} {} {} '.format(f_name, f_ext, f_day, f_month, f_year))
print(count)
