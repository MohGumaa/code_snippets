# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


# Here using Generator
def square_numbers(nums):
    for i in nums:
        yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

# Generator don't hold result in memory it yield which give location
# print(my_nums)

# Here using next we can print number by asking till stop iteration
# print(next(my_nums))
# print(next(my_nums))

my_nums = (x*x for x in [1,2,3,4,5])
# print(my_nums)
# print(list(my_nums))


# Will get generate memory
my_nums = [x*x for x in [1,2,3,4,5]]
# print(my_nums)


# Here use loop to print and know to stop
# for num in my_nums:
    # print(num)

