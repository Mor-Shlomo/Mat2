
def revword(word:str)->str:
    answer=word[::-1]
    return(answer.lower())


   
 
def countword():
    Xfile=open('text.txt')
    word=Xfile.readline()
    word=word.rstrip()
    word=word.lower()
    cunter=1
    for i in Xfile:
        line=i.split()
        for k in line:
            if revword(k) == word:
                cunter=cunter+1
    return(cunter)
