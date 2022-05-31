#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{:c}".format(i), end='')
