#to convert a hex input to decimal. 
hexNumbers={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
            'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
def HextoDec(hexNum):
    print('The string you have entered is',len(hexNum),'character(s) long')

    
    
    if len(hexNum)>5:
        return None #don't want to blow up 
    
    for element in hexNum: #checks hex input
        #print (element)
        if element not in hexNumbers:
            return None
            
    sum=0
    for i in range (len(hexNum)): 
         
        print(hexNumbers[hexNum[i]]*(16**i))
        sum=sum+hexNumbers[hexNum[i]]*(16**i)
    return sum   
        

print(HextoDec('BBB'))  #function call
print('The int conversion of AAA is',int('BBB', 16)) #verifying correctness with int() 
    



