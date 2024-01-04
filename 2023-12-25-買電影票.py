age = int( input('請輸入年齡 : ') )
# age = eval( input('請輸入年齡 : ') )
student = input('你是不是學生(Y/N) : ')

money = 0
if age >= 5 and student == "Y" :
    money = 100
elif age >= 5 and student == "N" :
    if  5 <= age <= 18 :
        money = 120
    else :
        money = 150

print( str(money) + '元')


# if age<5 or student == "Y" :
#     if age<5 :
#         print('免費')
#     else :
#         print('100 元')
# else :
#     if 5 <= age <= 18 :
#         print('120 元')
#     else :
#         print('150 元')



# if age < 5 :
#     print('免費')
# elif student == "Y" :
#     print('100 元')
# elif 5 <= age and age <= 18 :
#     print('120 元')
# else :
#     print('150 元')