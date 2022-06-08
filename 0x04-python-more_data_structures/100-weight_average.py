#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    totalWeight = 0
    totalScore = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        totalWeight += weight
        totalScore += score * weight
    return totalScore / totalWeight
