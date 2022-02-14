import operator

def zero(*args): #your code here
    if not args:
        return 0
    opstring = f"0{args[0]}"
    return(performOperation(opstring))
    

def one(*args): #your code here
    if not args:
        return 1
    opstring = f"1{args[0]}"
    return(performOperation(opstring))

def two(*args): #your code here
    if not args:
        return 2
    opstring = f"2{args[0]}"
    return(performOperation(opstring))

def three(*args): #your code here
    if not args:
        return 3
    opstring = f"3{args[0]}"
    return(performOperation(opstring))

def four(*args): #your code here
    if not args:
        return 4
    opstring = f"4{args[0]}"
    return(performOperation(opstring))

def five(*args): #your code here
    if not args:
        return 5
    opstring = f"5{args[0]}"
    return(performOperation(opstring))

def six(*args): #your code here
    if not args:
        return 6
    opstring = f"6{args[0]}"
    return(performOperation(opstring))

def seven(*args): #your code here
    if not args:
        return 7
    opstring = f"7{args[0]}"
    return(performOperation(opstring))

def eight(*args): #your code here
    if not args:
        return 8
    opstring = f"8{args[0]}"
    return(performOperation(opstring))

def nine(*args): #your code here
    if not args:
        return 9
    opstring = f"9{args[0]}"
    #print(opstring)
    return(performOperation(opstring))

def performOperation(opstring):
    leftnum,myop,rightnum = list(opstring)
    leftnum = int(leftnum)
    rightnum = int(rightnum)
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv}
    return ops[myop](leftnum,rightnum)

def plus(rightnum):
    return f"+{rightnum}"

def minus(rightnum):
    return f"-{rightnum}"

def times(rightnum):
    return f"*{rightnum}"

def divided_by(rightnum):
    return f"/{rightnum}"



print(zero(plus(one())))
print(three(times(six())))
print(six(divided_by(four())))
print(four(divided_by(zero())))
