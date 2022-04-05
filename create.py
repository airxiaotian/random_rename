import os
for i in range(10):
    file = os.open(os.getcwd()+'/files/'+str(i)+'.mp3', os.O_CREAT)
