def FizzBuzz(n):
    result_list=[]
    for i in range(1, n+1):
        # Multiple of both 3 and 5 -> FizzBuzz
        if i %3 == 0 and i %5 == 0:
            result_list.append("FizzBuzz")
        # Multiple of 5 only -> Buzz
        elif i %5 == 0:
            result_list.append("Buzz")
        # Multiple of 3 only -> Fizz
        elif i %3 == 0:
            result_list.append("Fizz")
        # Not a multiple of 3 or 5 -> keep the number itself
        else:
            result_list.append(i)
    return result_list

print(FizzBuzz(15))