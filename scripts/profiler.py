import numpy as np
import sys
import matplotlib.pyplot as plt


a = sys.argv

f = open('result.txt')
beta_range_min = 0
beta_range_max = 200
contrast_range_min = 120
contrast_range_max = 201
contrast_number = int((contrast_range_max - contrast_range_min)/5 + 1)
lines = f.readlines()

beta = []
contrast = []
AAE = []
EPE = []


for b in range(len(lines)):
    line = lines[b]
    words = line.split()
    if b % 2 == 0:
        beta.append(int(words[2]))
        contrast.append(int(words[3]))
    else:
        AAE.append(float(words[1]))
        EPE.append(float(words[4]))

for b in range(len(lines)):
    line = lines[b]
    words = line.split()
    beta.append(int(words[1]))
    contrast.append(int(words[3]))
    EPE.append(float(words[5]))


# Show AAE error according to beta value
xt = range(0, 195, 5)
plt.figure()
x = []
y = []
value = []
for c in range(17):
    x = []
    y = []
    for b in range(195/5 + 1):
        x.append(beta[b * 17 + c])
        y.append(AAE[b * 17 + c])
        value.append(contrast[b * 17 + c])
    plt.plot(x, y, label='haze = ' + str(value[c * (195/5+1)]))

print x
print y
print value
plt.xticks(xt)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=-2)

# Show EPE error according to beta value
# Show error according to beta value
xt = range(0, 195, 5)
plt.figure()
x = []
y = []
value = []
for c in range(17):
    x = []
    y = []
    for b in range(195/5 + 1):
        x.append(beta[b * 17 + c])
        y.append(EPE[b * 17 + c])
        value.append(contrast[b * 17 + c])
    plt.plot(x, y, label='haze = ' + str(value[c * (195/5+1)]))

print x
print y
print value
plt.xticks(xt)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=-2)

# Show EPE error according to beta value
# Show error according to beta value
xt = range(120, 201, 5)
plt.figure()
x = []
y = []
value = []
for b in range(beta_range_min, beta_range_max, 5):
    x = []
    y = []
    for c in range((contrast_range_max-contrast_range_min)/5 + 1):
        x.append(contrast[b/5 * contrast_number + c])
        y.append(EPE[b/5 * contrast_number + c])
        value.append(beta[b/5 * contrast_number + c])
    plt.plot(x, y, label='beta = ' + str(value[b/5 * contrast_number]))

print x
print y
print value
plt.xticks(xt)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=-2)

plt.show()