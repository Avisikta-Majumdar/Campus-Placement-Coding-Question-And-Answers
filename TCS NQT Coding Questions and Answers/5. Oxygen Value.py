'''
The selection of MPCS exams includes a fitness test which is conducted on the ground. There will be a batch of 3 trainees, appearing for a running test on track for 3 rounds.

You need to record their oxygen level after every round. After trainees are finished with all rounds, calculate for each trainee his average oxygen level over the 3 rounds and select the one with the highest average oxygen level as the fittest trainee. If more than one trainee attains the same highest average level, they all need to be selected. Display the fittest trainee(or trainers) and the highest average oxygen level.



Note:

1.The oxygen value entered should not be accepted if it is not in the range between 1 and 100.

2.If the calculated maximum average oxygen value of the trainees is below 70 then declare the trainees as unfit with a meaningful message as “All trainees are unfit”

3.Average oxygen values should be rounded


Example 1:



Input #1:
95
92
95


92

90

92

90

92

90





Output:

Trainee Number: 1

Trainee Number: 3



Note: Input should be 9 integer values representing oxygen levels entered in order as 



Round 1: 

Oxygen value of trainee 1

Oxygen value of trainee 2

Oxygen value of trainee 3



Round 2:

Oxygen value of trainee 1

Oxygen value of trainee 2 

Oxygen value of trainee 3



Round 3:

Oxygen value of trainee 1

Oxygen value of trainee 2

Oxygen value of trainee 3



Oxygen must be in the given format as in the above example. For any wrong input, the final output should display “INVALID INPUT”



Input #2:
91
92
45
92
80
90
90
92
90

Output:
Trainee Number: 1
'''


trainee1,trainee2,trainee3=[],[],[]
for i in range(1,10):
    Input=int(input())
    if Input in range(1,101):
        if i in[1,4,7]:
            trainee1.append(Input)
        elif i in [2,5,8]:
            trainee2.append(Input)
        else:
            trainee3.append(Input)
#print(trainee1,trainee2,trainee3)
Avgt1,Avgt2,Avgt3 = int(sum(trainee1)/3) , int(sum(trainee2)/3) , int(sum(trainee3)/3)
#print(Avgt1 , Avgt2 , Avgt3)
if Avgt1<=70 and Avgt2<=70 and Avgt3<=70:
    print('All trainees are unfit')
else:
    dic={'trainee1':Avgt1 , 'traineet2':Avgt2 , 'trainee3':Avgt3}
    avg=[Avgt1 , Avgt2 , Avgt3]
    max_=max(avg)
count=0
for i in avg:
    if i==max_:
        print("Trainee number:",avg.index(i)+1+count)
        avg.remove(i)
        count+=1
        
    
