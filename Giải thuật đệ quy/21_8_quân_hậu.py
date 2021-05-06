from itertools import permutations

n=8
#bước nhảy
dem=0
cols = range(n)

for combo in permutations(cols):                      
    if n==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        dem += 1
        print('Bước nhảy thứ  '
        	+str(dem)+': '
        		+str(combo)+'\n')  
 
        print("\n".join(' O ' * i + ' ♥️ ' + ' O ' * (n-i-1) for i in combo) 
        	+"\n\n\n\n")