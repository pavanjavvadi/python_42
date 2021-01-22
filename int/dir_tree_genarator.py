import os

for path,dirs,files in os.walk('/home/pavan/python projects/'):
    print("Current Directory: "+path)
    for dir in dirs:
        print("----SubFolder presents: "+path+"/"+dir)
    for file in files:
        print("--------Files: "+file)    
    

