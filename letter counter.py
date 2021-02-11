text = input()
dict = {
    
}
lenth=len(text)
i=0
c=0
while c <lenth:
    a=text[i]
    
    dict[a]=text.count(a)
    c+=1
    i+=1

print(dict)
