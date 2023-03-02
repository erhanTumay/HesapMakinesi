s1=int(input(""))
print(s1)

islem=input("")
print(s1,islem)

s2=int(input(""))

if islem=="+":
    sonuc=(s1)+(s2)
elif islem=="-": 
    sonuc=(s1)-(s2)
elif islem=="*": 
    sonuc=(s1)*(s2)
elif islem=="/": 
    sonuc=(s1)/(s2)        
else: print("hatalı islem girdiniz")

print(s1,islem,s2,"=",sonuc)  