# Conditionals

#  if <test>:
#      <code>


# == 
# >
# >=
# <=
# != 
#
# Boolean Operators
#
# test1 AND test2

# |  In1 | In2 | OUT |
# +------+-----+-----+
# |  0   |  0  |  0  |
# |  1   |  0  |  0  |
# |  0   |  1  |  0  |
# |  1   |  1  |  1  |


# test1 OR test2
# |  In1 | In2 | OUT |
# +------+-----+-----+
# |  0   |  0  |  0  |
# |  1   |  0  |  1  |
# |  0   |  1  |  1  |
# |  1   |  1  |  1  |

# NOT
# | In1 | Out |
# +-----+-----+
# |  1  |  0  |
# |  0  |  1  |


# if test1 AND NOT( test2 ):
#       code    

# Maths Functions
#  +  -  *  /  //  **  %


invar1 = int(input('NUM!: '))
ansvarof7 = invar1%7
ansvarof5 = invar1%5


if ansvarof7 == 0 and ansvarof5 == 0:
    print('divisible by 7 and multiple of 5')
else:
    print('not divisible by 7 and multiple of 5')


# needs a full test either side of the boolean operator

#not
# if ansvarof5 == 0 and > 7:
if ansvarof5 == 0 and ansvarof5 > 7:
    print('yay')
