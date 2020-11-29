from itertools import product

def replace_escape(reg,word):
    while "\\" in reg:
        if reg.find("\+") != -1:
            reg = reg.replace("\\"+"+",'P')
            word = word.replace("+",'P')
        elif reg.find("\*") != -1:
            reg = reg.replace("\\"+"*",'A')
            word = word.replace("*",'A')
        elif reg.find("\?") != -1:
            reg = reg.replace("\\"+"?",'Q')
            word = word.replace("?",'Q')
        elif reg.find("\^") != -1:
            reg = reg.replace("\\"^".",'Ş')
            word = word.replace("^",'Ş')
        elif reg.find("\$") != -1:
            reg = reg.replace("\\"+"$",'D')
            word = word.replace("$",'D')
        elif reg.find("\.") != -1:
            reg = reg.replace("\\"+".",'N')
            word = word.replace(".",'N')
        elif reg.find("\\") != -1:
            reg = reg.replace("\\\\",'E')
            word = word.replace("\\",'E')
    return (reg,word)

reg, word = replace_escape(*input().split("|"))

a=[]
def asteriks_mark(reg):
    regl = reg.split("*")
    length = len(word) + reg.count('*') + 3 - len(reg)
    def asteriks(reg):
        tup = []
        for i in range(length):
            if reg:
                tup.append(reg[0:-1] + reg[-1] * i)
            else:
                tup.append("")
        return(tup)

    pos=list(map(asteriks,regl))
    for i in product(*pos):
        if len("".join(i)) <= len(word) + length:
            yield "".join(i)
        
def plus_mark(reg):
    regl = reg.split("+")
    length = len(word) + reg.count('+') + 3 - len(reg)

    def plus(reg):
        tup = []
        for i in range(length):
            if reg:
                tup.append(reg + reg[-1] * i)
            else:
                tup.append("")
        return(tup)

    pos = list(map(plus,regl))

    for i in product(*pos):
         if len("".join(i)) <= len(word) + length:
            yield "".join(i)

def question_mark(reg):
    regl =reg.split("?")
    def question(reg):
        tup = []
        for i in range(2):
            if reg:
                tup.append(reg[0:-1] + reg[-1] * i)
            else:
                tup.append("")
        return(tup)
    pos = list(map(question,regl))
    for i in product(*pos):
            yield "".join(i)

def regex(reg, word):
#     print(reg)
    if reg in word or (len(reg) == reg.count('.') <= len(word)) :
        a.append(True)
    
    elif "?" in reg:
        k = question_mark(reg)
        for i in k:
            if i == word:
                a.append(True)
            elif "+" in i or "*" in i or "." in i or "^" in i or "$" in i:
                return regex(i, word)
        else:
            a.append(False)
            
    elif "*" in reg:
        k = asteriks_mark(reg)
        for i in k:
            if i == word:
                a.append(True)
            elif "?" in i or "+" in i or "." in i or "^" in i or "$" in i:
                a.append(regex(i, word))
        else:
            a.append(False)
            
    elif "+" in reg:
        k = plus_mark(reg)
        match = False
        for i in k:
            if i in word:
                match = True
                a.append(True)
            if match:
                break
            elif "?" in i or "*" in i or "." in i or "^" in i or "$" in i:
                a.append(regex(i, word))
        else:
            a.append(False)
    
    elif reg[-1] == "$":
        reg = reg[0:-1]
        if reg[-1] == '.':
            a.append(regex(reg, word[-len(reg):]))
        elif reg[-1] != word[-1]:
            a.append(False)
        else:
            a.append(regex(reg, word[-len(reg):]))
        
    elif reg[0] == '^':
        reg = reg[1:]
        a.append(regex(reg, word[:len(reg)]))
    else:
        if word and (reg[0] == '.' or reg[0] == word[0]):
            a.append(regex(reg[1:], word[1:]))
        else:
            return a.append(False)

regex(reg, word)
print(any(a))
