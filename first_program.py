NEC = 0  
FFA = 0    
EDU = 0  
LTSS = 0   
PLAY = 0       
GIVA = 0       

necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05

expectedIncome = 1000

print ("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""")
suma = 0

while (suma < expectedIncome):
    line = int(input())
    suma += line

    NEC += line * necRate
    FFA += line * ffaRate
    EDU += line * eduRate
    LTSS += line * ltssRate
    PLAY += line * playRate
    GIVA += line * giveRate

    print("\n Enter the amount please:")

print("At the end we have:\n\
    Necessity Envelop has:                       " + str(int(NEC)) + "\n\
    Financial Freedom Envelop has:               " + str(int(FFA)) + "\n\
    Education Envelop                            " + str(int(EDU)) + "\n\
    Long Term Saving for Spending Envelop has:   " + str(int(LTSS)) + "\n\
    Play Envelop has:                            " + str(int(PLAY)) + "\n\
    Give Envelop has:                            " + str(int(GIVA)) + "\n\
    _______________________________________________________________\n\
\
    Thanks for using our software :)")