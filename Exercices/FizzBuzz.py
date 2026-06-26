def FizzBuzz(n):
    result_list=[]
    for i in range(1, n+1):
        if i %3 == 0 and i %5 == 0:
            result_list.append("FizzBuzz")
        elif i %5 == 0:
            result_list.append("Buzz")
        elif i %3 == 0:
            result_list.append("Fizz")
        else:
            result_list.append(i)
    return result_list

print(FizzBuzz(15))