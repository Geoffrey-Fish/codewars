#SOLVED but fuck, i needed nearly two hours whre others do a oneliner...
def count(string):
    # The function code should be here
    liste = list(string)
    mydict = {}
    x = 0
    
    for i in liste:
        if i in mydict.keys() :
            x += 1
            continue
        else :
            mydict.update({liste[x]:0})
            for i in liste :
                if i == liste[x] :
                    mydict[liste[x]] += 1
                else :
                    continue
            x += 1
    return mydict

print(count("trololokakarabums"))
