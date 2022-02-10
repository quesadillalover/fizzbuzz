for x in range(1,101):
    if x % 3 is 0 and x % 5 is 0:
        print('fizzbuzz')
    elif x % 3 is 0:
        print('fizz')
    elif x % 5 is 0:
        print('buzz')
    else:
        print(x)