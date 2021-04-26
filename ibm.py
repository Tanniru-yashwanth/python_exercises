def calculatevaccdrivelist(adharnumber, DOB, comorbidity):
    print(adharnumber)
    print(DOB)
    print(comorbidity)
    #for elements in calculatevaccdrivelist:
        #print(elements)
    if comorbidity == 'yes':
        print('1')
    if DOB < '1/1/1960':
        print('1')
    if DOB > '1/1/1990':
        print('2')


calculatevaccdrivelist('1234 4567 7895', '11/4/1958', 'no')