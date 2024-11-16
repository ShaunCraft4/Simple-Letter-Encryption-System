def Encrypt_Message(s,k):
    sm=""
    for i in s:
        av=ord(i)
        for j in range(k):
            if av==122:
                av=96
            if av==90:
                av=64
            av+=1
        sm+=chr(av)
    print("Encrypted Message: ",sm)

s=input("Enter string to be encypted: ")
k=int(input("Enter key value: "))
Encrypt_Message(s,k)
        
                    
            
            
            
    