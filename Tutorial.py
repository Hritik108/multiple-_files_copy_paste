# import os
# path="D:\\create_directories"

# for i in range(1,10):
#     os.chdir(path)
#     newfolder='Tutorial-'+str(i)
#     os.makedirs(newfolder)

import shutil
import os
#shutil.copy
#shutil.move
path="D:\\create_directories"
src = r"D:\capcha_images\capcha\capcha"
# dest = r"C:\Users\Moondra\Desktop\FOLDER B"
files = os.listdir(src)
print(len(files))
for i in range(0,len(files),10):
    os.chdir(path)
    newfolder='Tutorial-'+str(i)
    os.makedirs(newfolder)
    for j in range(i,i+10):
        dest = r'D:\\create_directories\\'+newfolder
        full_file_name = os.path.join(src,files[j])
        shutil.copy(full_file_name, dest)
        # print(files[i])
