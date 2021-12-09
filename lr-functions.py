def nameofthefunction(funcin):
    answervar1 = funcin%7
    answervar2 = funcin//7
    return [answervar1,answervar2]


passthruvar = int(input('NuMiN: '))
thebootofthecar = nameofthefunction(passthruvar)

print(thebootofthecar)

