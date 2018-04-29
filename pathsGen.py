import json
import copy
import recruitmentProcessSheme
import dataInputProcessSheme

delimiter = " | "

def printPath(path):
    print delimiter.join(path)

def printExistingPaths(n, path, model):
    try:
        for node in model[n]:
            currentPath = copy.copy(path)
            if node == "#":
                printPath(currentPath)
                return
            else:
                currentPath.append(node)
                printExistingPaths(node, currentPath, model)
    except:
        print "Exception. Current path:" + str(path)


recruitmentProcessModel = json.load(open('recruitment.json'))
dataInputProcessModel = json.load(open('input.json'))

print "Recruitment Model:"
printExistingPaths('1.2.1', ["1.2.1"], recruitmentProcessModel)
printExistingPaths('1.4.1', ["1.4.1"], recruitmentProcessModel)
printExistingPaths('1.5.1', ["1.5.1"], recruitmentProcessModel)

print "Data Input Model:"
printExistingPaths('2.1.1', ['2.1.1'], dataInputProcessModel)
printExistingPaths('2.2.1', ['2.2.1'], dataInputProcessModel)
printExistingPaths('2.3.1', ['2.3.1'], dataInputProcessModel)