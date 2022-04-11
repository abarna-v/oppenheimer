import os
import time

file_full_path = ""
for root, dirs, files in os.walk(os.getcwd()):
    for x in files:
        if 'requirements.txt' in x:
            file_full_path = os.path.join(root, x)   
        else:
            pass
    print ("Requirements File Found : ", file_full_path)
    
if file_full_path:
    print ("Changing the Directory  : ", root)
    os.chdir(root)
    pip_cmd = 'pip install -U -r ' + str(file_full_path) 
    print ("Executing the Command   : ", pip_cmd)
    stdout = os.system(pip_cmd)
