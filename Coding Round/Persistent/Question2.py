def Filpped(num1,num2):
    #Converting decimal value to binary number
    binaryNum1 = bin(num1)
    binaryNum1 = str(binaryNum1)[2:]
    
    #Converting decimal value to binary number
    binaryNum2 = bin(num2)
    binaryNum2 = str(binaryNum2)[2:]
    #This will count how many times we have flip 
    count=0
    
    if len(binaryNum2)==len(binaryNum1):
        for i,j in zip(binaryNum1,binaryNum2):
            if i!=j :
                #This means we have to flipped binaryNum1
                count+=1 
        return count
    else:
        #if length of binaryNum2 is greater than length of binaryNum2 then do this 
        binaryNum1 = "0"*(len(binaryNum2)-len(binaryNum1)) + binaryNum1
        for i,j in zip(binaryNum1,binaryNum2):
            if i!=j :
                #This means we have to flipped binaryNum1
                count+=1 
        return count
    
    

def main():
    num1 = int(input())
    num2 = int(input())
    
    result = Filpped(num1,num2)
    
    print(result)

if __name__  == "__main__":
    main()
