a = input('how many points a team scored')
a = int (a)
if a>= 15: 
    print('earned a gold medal') 
else:
    if 12<=a<=14: 
        print('earned a silver medal')
    else:
        if 9<=a<=11: 
            print('earned a bronze medal')
        else: 
            print('no medal earned')
