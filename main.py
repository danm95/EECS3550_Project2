
import collections 
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def parseFileDATA(fileData):
    temp = ""
    domain = 0
    parsedData = []

    fileData = [x.strip() for x in fileData]

    for x in fileData:

        if (x == "<") & (len(temp) == 0):
            temp = temp + x
            domain = 1
        elif x == "<":
            parsedData.append(temp)
            temp = ""
            temp = temp + x
            domain = 1
        elif (domain == 1) & (x != "") & (x != ">"):
            temp = temp + x
        elif x == ">":
            temp = temp + x
            parsedData.append(temp)
            temp = ""
            domain = 0
        elif (x != "") & (x != ";") & (domain == 0):
            temp = temp + x
        elif (x == ";") & (domain == 0):
            parsedData.append(temp)
            temp = ""

    return parsedData


def Infix_to_Postfix(expression, postDomain):


    operators = ["+", "*"]
    Parentheses = ["(", ")"]
    stack = []
    postfix = ""
    expressionPostfix = []
    setsPostfix = {}
    listExpressionPostfix = []
    postlist = []
    inList = 0

    expression = expression.split("=")

    for y in expression:
        for z in y:

            if z in Parentheses:                                    #Manage Parentheses
                if z == "(":
                    stack.append("(")
                else:
                    while stack[len(stack)-1] != "(":
                        if stack[len(stack)-1] not in Parentheses:
                            postfix = postfix + stack[len(stack)-1]
                        stack.pop()
                    stack.pop()

            elif z in operators:                                      #Add Operator
                if len(stack) != 0:
                    if (stack[len(stack)-1] == "+") & (z == "+") | (stack[len(stack)-1] == "*") & (z == "+"):
                        postfix = postfix + stack[len(stack) - 1]
                        stack.pop()
                        stack.append(z)
                    else:
                        stack.append(z)
                else:
                    stack.append(z)

            else:                                                   #Add Operand
                postfix = postfix + z

        while len(stack) != 0:
            postfix = postfix + stack[len(stack) - 1]
            stack.pop()

        expressionPostfix.append(postfix)
        postfix = ""

    return expressionPostfix

    '''if postDomain == "<sets>":
        for x in expressionPostfix:
            for y in x:
                if y == "{":
                    inList = 1
                elif (y not in operators) & (y != ",") & (inList == 1) & (y != "}"):
                    postlist.append(y)
                elif y == "}":
                    listExpressionPostfix.append(postlist)
                    setsPostfix = set(postlist)
                    listExpressionPostfix.append(setsPostfix)
                    postlist.clear()
                    inList = 0
                elif y in operators:
                    postlist.append(y)
                    setsPostfix = set(postlist)
                    listExpressionPostfix.append(setsPostfix)
                    postlist.clear()

        expressionPostfix = listExpressionPostfix

        return expressionPostfix
    else:'''


def evaluateExp(exp, expDomain):
    evalOper = ["+", "*"]
    evalStack = []
    evalSet1 = []
    evalSet2 = []
    result = []
    evalTemp1 = ""
    evalTemp2 = ""
    evalResultTemp = ""
    postlist = []
    setsPostfix = {}
    inList = 0
    

    if expDomain == "<algebra>":
        for x in exp:
            for y in x:
                if y in evalOper:
                    evalTemp1 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    evalTemp2 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    if y == "*":
                        evalResultTemp = str(int(evalTemp1) * int(evalTemp2))
                        evalStack.append(evalResultTemp)
                    else:
                        evalResultTemp = str(int(evalTemp1) + int(evalTemp2))
                        evalStack.append(evalResultTemp)
                else:
                    evalStack.append(y)
            result.append(evalStack[len(evalStack)-1])

    elif expDomain == "<strings>":
        for x in exp:
            for y in x:
                if y in evalOper:
                    evalResultTemp = ""
                    evalTemp1 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    evalTemp2 = evalStack[len(evalStack) - 1]
                    evalStack.pop()
                    if y == "*":
                        for z in range(int(evalTemp1)):
                            evalResultTemp = evalResultTemp + evalTemp2
                        evalStack.append(evalResultTemp)
                    else:
                        evalResultTemp = evalTemp2 + evalTemp1
                        evalStack.append(evalResultTemp)
                else:
                    evalStack.append(y)
            result.append(evalStack[len(evalStack) - 1])


    elif expDomain == "<sets>":
        for x in exp:
            for y in x:                   
                if y == "{":
                    inList = 1
                elif (y != ",") & (inList == 1) & (y != "}"):
                    postlist.append(y)
                elif y == "}":
                    setsPostfix = set(postlist)
                    evalStack.append(setsPostfix)
                    postlist.clear()
                    inList = 0

                elif y in evalOper:
                    evalSet1 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    evalSet2 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    if y[0] == "*":
                        evalStack.append(evalSet1.union(evalSet2))
                        evalsetResult = evalStack[len(evalStack)-1]                           
                    else:
                        evalStack.append(evalSet1.intersection(evalSet2))
                        evalsetResult = evalStack[len(evalStack)-1]                            
            result.append(evalsetResult)
            evalStack.clear()

    else:
        for x in exp:
            for y in x:
                if y in evalOper:
                    evalTemp1 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    evalTemp2 = evalStack[len(evalStack)-1]
                    evalStack.pop()
                    if y == "*":
                        if (evalTemp1 == "1") & (evalTemp2 == "1"):
                            evalStack.append("1")
                        else:
                            evalStack.append("0")
                    elif y == "+":
                        if (evalTemp1 == "1") | (evalTemp2 == "1"):
                            evalStack.append("1")
                        else:
                            evalStack.append("0")
                else:
                    evalStack.append(y)
            result.append(evalStack[len(evalStack) - 1])

    return result


def checkResult(result, domain):
    if domain == '<sets>':
        first = []
        first[result[0]]
        for x in result:
            if result[x] == first:
                return "True"
        return "False"


    else:
        first = result[0]
        T = "True"
        F = "False"
        for x in result:
            if x != first:
                return "False"
        return "True"


expressionFile = open('ExpressionTest.txt', 'r')
expressionData = expressionFile.read()
expressionFile.close()
domain = ['<strings>', '<algebra>', '<sets>', '<boolean>']
parsedFileData = parseFileDATA(expressionData)
expPostfix = []
expResults = []
currentDomain = []
index = 0


'''expPostfix = Infix_to_Postfix(parsedFileData[5], '<sets>')
evaluateExp(expPostfix, '<sets>')'''

for x in parsedFileData:

    if x in domain:
        currentDomain.append(x)
        index = index + 1
    elif x == "</>":
        currentDomain.pop()
        index = index + 1
    else:
        print("Current Domain: " + currentDomain[len(currentDomain) - 1])
        print("Infix Expression: " + str(x))
        expPostfix = Infix_to_Postfix(str(x), currentDomain[len(currentDomain) - 1])
        print("Postfix Expression: " + str(expPostfix))
        expResults = evaluateExp(expPostfix, currentDomain[len(currentDomain) - 1])
        print("Evaluate Expression Results: " + str(expResults))
        print("True/False: " + checkResult(expResults, currentDomain[len(currentDomain) - 1]))
        index = index + 1











































