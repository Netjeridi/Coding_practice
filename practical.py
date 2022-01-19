# functional programming: map, filter, zip and reduce
# inbuilt functions that allow us to keep code simple
# the functions we define for them don't need lots of complexity
# means we can use pure functions

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


# provided with a function and an iterable,
# map applies the function to each element of
# the iterable and returns the new values
print(list(map(multiply_by2, my_list)))

# provided with a function and an iterable,
# filter applies the function and returns
# only values that evaluate to TRUE
print(list(filter(only_odd, my_list)))

# zip combines elements of iterables ('zips' them together)
# 1st element of each, 2nd element of each and so on
# can be as many iterables as required
# creates tuples of elements
print(list(zip(my_list, your_list)))

# reduce has to be imported separately
from functools import reduce


def accumulator(acc, item):
    return acc + item


# reduce takes a function, a sequence and an
# initial value (defaults to zero if not provided)
# for each pass of the function, reduce uses the
# previously returned value as the new 'initial value'
print(reduce(accumulator, my_list, 0))

# lambda expressions - one off anonymous (unnamed) functions
# use with caution as can make code less readable
# so instead of defining 'multiply_by2', we can use
# lambda param: action(param)
print(list(map(lambda item: item * 2, my_list)))

# or instead of 'accumulator' function we can use lambda
print(reduce(lambda acc, item: acc + item, my_list))

# list/set/dictionary comprehensions
# again, can reduce code readability
# my_list = [param for param in iterable]

# return each character of 'hello'
my_list = [char for char in 'hello']
print(my_list)

# return values from 0 to 100
print([num for num in range(0, 100)])

# return squared values from 0 to 100 only if they are even
print([num**2 for num in range(0,100) if num % 2 == 0])

# for sets we can do the same thing
# will return only unique values
my_set = {char for char in 'hello'}
print(my_set)
