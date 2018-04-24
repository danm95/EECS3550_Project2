
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
    print(parsedData)
    return parsedData


def Infix_to_Postfix(expression, postDomain):
    print("The expression passed to Infix_to_Postfix is: " + expression)

    operators = ["+", "*"]
    Parentheses = ["(", ")"]
    stack = []
    postfix = ""
    expressionPostfix = []
    setsPostfix = {}

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

    print("Postfix expression: " + str(expressionPostfix))

    listExpressionPostfix = []
    postlist = []
    inList = 0

    if postDomain == "<sets>":
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


def evaluateExp(exp, expDomain):
    evalOper = ["+", "*"]
    evalStack = []
    evalSet1 = []
    evalSet2 = []
    result = []
    evalTemp1 = ""
    evalTemp2 = ""
    evalResultTemp = ""

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
                if y[0] in evalOper:
                    evalResultTemp = ""
                    evalSet1.append(evalStack[len(evalStack)-1])
                    evalStack.pop()
                    evalSet2.append(evalStack[len(evalStack)-1])
                    evalStack.pop()
                    if y[0] == "*":
                        evalStack.append(evalSet1.union(evalSet2))
                    else:
                        evalStack.append(evalSet1.intersection(evalSet2))
                else:
                    evalStack.append(y)
            result.append(evalStack[len(evalStack) - 1])

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

    print(str(result))


expressionFile = open('ExpressionTest.txt', 'r')
expressionData = expressionFile.read()
expressionFile.close()

parsedFileData = parseFileDATA(expressionData)
expPostfix = []

listofsets.append((list(a_list), a_list[0]))


expPostfix = Infix_to_Postfix(parsedFileData[5], '<sets>')

evaluateExp(expPostfix, '<sets>')




'''for x in parsedFileData:
    if x in domain:
        currentDomain.append(x)
    elif x == "</>":
        currentDomain.pop()
    else:
       expPostfix = Infix_to_Postfix(parsedFileData[1])'''





















