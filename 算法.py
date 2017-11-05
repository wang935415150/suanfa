#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/11/4

def func(x):
    if x>0:
        print('抱着',end='')
        func(x-1)
        print('得我',end='')
    else:
        print('我的小鲤鱼', end='')
# func(3)

# 结果:抱着抱着抱着我的小鲤鱼得我得我得我

li = [1,2,3,4,5,6,7,8,9,10]


def func(li,x):
    for i in range(len(li)) :
        if li[i] ==x:
            print(i)

# func(li,5)

# 下角标是4

def bin_search(li,x):
    low=0
    high=len(li)-1
    while low<=high:
        mid=(low+high)//2
        if li[mid] == x:
            print(mid)
            break
        elif li[mid]>x:
            high = mid - 1
        else:
            low = mid + 1

# bin_search(li,8)
# 返回的索引是7


# 冒泡排序
    # 特点是循环几趟:然后有一个有序区和一个无序区
sufli=[2,6,7,2,3,6,7,12,4,5,7,11]

def bulle_seach(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li

# print(bulle_seach(sufli))

# 选择排序
#     思路 :无序区和有序区,最小位置在哪里

def select_search(li):
    for i in range(len(li)-1):
        min_loc=i
        for j in range(i+1 , len(li)):
            if li[j]<li[min_loc]:
                min_loc=j
                li[j],li[min_loc]=li[min_loc],li[j]
        if min_loc != i:
            li[i],li[min_loc]=li[min_loc],li[i]
    return li


def xuanze(li):
    for i in range(len(li)-1):
        moc=i
        for j in range(i+1,len(li)):
            if li[moc]>li[j]:
                li[moc],li[j]=li[j],li[moc]
    return li
# print(select_search(sufli))


# 插入排序
    # 特点: 摸到的牌和手里的牌

def inster_search(li):
    for i in range(1,len(li)):
        temp=li[i]
        j=i-1
        while j>=0 and temp<li[j]:
            li[j+1]=li[j]
            j=j-1
        li[j+1]=temp
    return li

def inster(li):
    for i in range(1,len(li)-1):
        one=li[i]
        j=i-1
        while j>=0 and one<li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1]=one

    return li

def inster2(li):
    for i in range(1,len(li)):
        temp=li[i]
        j=i-1
        while j>=0 and temp<li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
    return li

