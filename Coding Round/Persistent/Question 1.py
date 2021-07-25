def dictWords(textInput):
    #Write you code here
    WordString = textInput.split(" ")
    s=[]
    for i in WordString:
        if WordString.count(i)>1:
            #This condition will only true if the word is present more than one in textInput
            s.append(i)
    #s list will only contain those words which is occured more than once in textInput
    s=set(s)

    s = list(s)

    s.sort()
    if len(s)==0:
        #This means there are no duplicate words present in textInput
        return ["NA"]

    return s
            



def main():
    #input for text input
    textInput =input()

    result = dictWords(textInput)

    print(" ".join([str(res) for res in result]))

    
if __name__ == "__main__":
    main()
