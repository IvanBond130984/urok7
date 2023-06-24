str_x=input('Введите предложение:')
sn=''
ci=0
for si in str_x:
    if si==' ':
        ci+=1
        if ci==1:
            sn += si
    else:
        sn += si
        ci=0
print(sn)