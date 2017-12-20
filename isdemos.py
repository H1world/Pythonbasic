# def demo(num1, num2):
#     if num1 < num2:
#         print('too small')
#         return False
#     elif num1 > num2:
#         print('too big')
#         return False
#     else:
#         print('BINGO')
#         return True

# from random import randint
# num = randint(1,100)
# print ('Guess what I think?')
# bingo = False
# while bingo == False:
#     answer = int(input())
#     bingo = (demo(answer, num))
# //
    # if answer < num:
    #     print ('%d is too small'% answer)

    # if answer > num:
    #     print ('too big?')

    # if answer == num:
    #     print ('BINGO')
    #     bingo = True



# a = 0
# b = 1  
# while b < 101:  
#     a = a + b  
#     b += 1  
# print(a)

# for i in range(1, 101):
#     print (i)
# print(1)
# a = input()
# print(2)

# a = 0
# for i in range(1,101):
#     a = a + i
# print (a)
# print (sum(range(1, 101)))
# print("*\n***\n*****\n***\n*")

# num = 'Crossin'
# print('%s.is a good teacher.' % num)

# for i in range(0, 5):
#     for j in range(0, i + 1):
#         print('*',end='')
#     print('')
# print ("%s's score is %d"%('mike',87))
            
# def sayHello():
#     print ('hello')

# sayHello();

# a = [1,'daf',2,3,True]
# a.append('llal');   #添加到数组内
# del a[0];
# print(a)

# //随机从数组中获取一个
# from random import choice
# print ('Choose one side to shoot:')
# print ('left, center, right')
# you = input()
# print ('You kicked ' + you)
# direction = ['left', 'center', 'right']
# com = choice(direction)
# print ('Computer saved ' + com)
# if you != com:
#     print ('Goal!')
# else:
#    print ('Oops...')

# //split() 分割字符串，默认为''切割
# print('aaa'.split('a'))
# //join() 将数组转化连接成字符串
# s = ','
# li = ['apple', 'pear', 'orange']
# fruit = s.join(li)
# print(fruit)

# word = 'helloworld'
# for c in word:
#     print(c)  #word字符串每个字符都会print出来

# // py2版本打开文件：file() py3为open()
#read()函数把文件内所有内容读进一个字符串中
#readline() 读取一行内容
#readlines()  把内容按行读取至一个list中 
#close为关闭文件，释放资源
# f = open('text.txt')
# data = f.read()
# print (data)
# f.close()
# a = input()
# ff = open('text2.txt')
# 'w'就是writing，以这种模式打开文件，原来文件中的内容会被你新写入的内容覆盖掉，如果文件不存在，会自动创建文件。 另外还有一种模式是'a'，appending。它也是一种写入模式，但你写入的内容不会覆盖之前的内容，而是添加到文件中。  write写入
# ff.write(a)


#↓读取数据，操作数据求和
# FILE_OBJECT = open('text2.txt', encoding='UTF-8')  # 修改文件编码格式.默认貌似是GBK 修改为UTF-8
# lines = FILE_OBJECT.readlines()
# FILE_OBJECT.close()
# results = []
# for line in lines:
#     # print(line)
#     data = line.split()
#     # print(data)
#     sum = 0
#     for score in data[1:]:
#         sum += int(score)
#     result = '%s\t: %d\n' % (data[0], sum)
#     results.append(result)          
# print(results)
# output = open('result.txt', 'w', encoding='UTF-8')
# output.writelines(results)
# output.close()

# ↓break 强制终止循环
# while True:
#     a = input()
#     if a == 'EOF':
#         break
# for i in range(10):
#     a = input()
#     if a == 'SOS':
#         break

# ↓continue 终止此次循环继续下面的循环
# i=0
# while i<5:
#     i+=1
#     for j in range(3):
#         print (j)
#         if j==2:
#             break
#     for k in range(3):
#         if k==2:
#             continue
#             print(k)
#     if i > 3:
#         break
#     print(i)

# ↓ try...except-块 用来处理异常语句. 
# try:
#     FILE_OBJECT = open('text2.txt',encoding='UTF-8')  #如果不加encoding='UTF-8' 那么将报错.
#     a = FILE_OBJECT.read()
#     print(a)
# except:
#     print ('File not exists.')
# print('dadaf')

# score = {
#     '萧峰': 95,
#     '段誉': 97,
#     '虚竹': 89
# }
# print (score['段誉'])
# for name in score:
#     print (score[name])

from turtle import *


def curvemove():
    for i in range(200):
        right(1)
        forward(1)

color('red', 'pink')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()


# pensize(1)
# pencolor('red')
# fillcolor('pink')
# speed(5)
# up()
# goto(-30, 100)
# down()
# begin_fill()
# left(90)
# circle(120, 180)
# circle(360, 70)
# left(38)
# circle(360, 70)
# circle(120, 180)
# end_fill()
# up()
# goto(-100, -100)
# down()
