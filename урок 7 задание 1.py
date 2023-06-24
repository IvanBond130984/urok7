sx=input('Введите слово для проверки:')
sxl=sx.lower()
n=len(sxl)
if sxl==sxl[n::-1]:
    print('yes')
else:
    print('no')