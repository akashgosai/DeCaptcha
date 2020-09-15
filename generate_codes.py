import os

count = 1
for image in os.listdir('.'):
    os.system('cp '+image+' image'+str(count)+'.png')
    count += 1
    print(image)
