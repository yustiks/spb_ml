file = open('yolo_training.txt','r')
los = []
x = []
k = 0
for line in file:
    if line.find('rate')!=-1:
        start = line.find('loss,')+6
        end = line.find('rate')
#        print(line)
        los.append(float(line[start:end]))
        x.append(k)
        k += 1
        print(line[start:end])
file.close()

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(18,6))

plt.plot(x, los, '-')
plt.legend(['learning rate'])
#plt.legend(['validation los'])
#plt.ylim(0,2.1)
plt.xlabel('# step of epochs')
plt.ylabel('loss')
plt.show()