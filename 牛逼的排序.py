#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/11/5

sufli=[6,7,2,5,5,6,8,99,2,3,5,3,77,121,52]

# 快排
#     思路:
#         取出一个元素p ,元素p归为
#         右边的比p小 左边的比p大
#     递归完成排序

def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and li[right]>=tmp:
            right -= 1
        li[left]=li[right]
        while left<right and li[left]<=tmp:
            left +=1
        li[right]=li[left]
    li[left]=tmp
    return left
# print(partition(sufli,0,len(sufli)-1))

def suft(li,left,right):
    if left<right:
        mid=partition(li,left,right)
        suft(li,left,mid-1)
        suft(li,mid+1,right)

# suft(sufli,0,len(sufli)-1)
# print(sufli)




def kuai(li,left,right):
    temp=li[left]
    while left<right:
        while left<right and li[right]>=temp:
            right-=1
        li[left]=li[right]
        while left<right and li[left]<=temp:
            left+=1
        li[right]=li[left]
    li[left]=temp
    return left

# print(kuai(sufli,0,len(sufli)-1))
def kaishi(li,left,right):
    if left<right:
        mid=kuai(li,left,right)
        kaishi(li, left, mid - 1)
        kaishi(li,mid+1,right)
# kaishi(sufli,0,len(sufli)-1)

# print(sufli)

def kuaipai2(li):
    if len(li)<=1:
        return li
    temp=li[len(li)//2]
    left=[x for x in li if x < temp]
    middel = [x for x in li if x == temp]
    right = [x for x in li if x > temp]
    return kuaipai2(left) + middel + kuaipai2(right)

# print(kuaipai2(sufli))




# 鸡尾酒排序
#     第一趟找出最小的和最大的
#     然后在一趟趟的找
def cocktail_sort(l):
    size = len(l)
    sign = 1
    for i in range(size // 2):
        if sign:
            sign = 0
            for j in range(i, size - 1 - i):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
            for k in range(size - 2 - i, i, -1):
                if l[k] < l[k - 1]:
                    l[k], l[k - 1] = l[k - 1], l[k]
                    sign = 1
        else:
            break
    print (l)





