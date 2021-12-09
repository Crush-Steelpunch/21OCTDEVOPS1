# LOOPS

# While loop

#test1 = x
#while test of test1:
#    test1 = somechangeof test1

startvar = 0
while startvar < 20:
    print("I'm a loop!")
    startvar = startvar + 1




# For loop

# for var in iterablelist:
#     code



for var in 'abcde':
    print(var)

# iterable, lists, tuples, strings

dictvar1 = { 'name':'leon', 'face':'beautiful','personality':'sarcastic' }
print(dictvar1.keys())

for var in dictvar1.keys():
    print(dictvar1[var])


for x in range(6):
    print(x)