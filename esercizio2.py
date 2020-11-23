
from random import randint
print("ecco la media degli stipendi dei dipendenti a, b, c, d, e,")
while True:
    q =  int(input("Inserisci -1 per bloccare"))
    stipendioa = randint(1500, 3000)
    stipendiob = randint(1500, 3000)
    stipendioc = randint(1500, 3000)
    stipendiod = randint(1500, 3000)
    stipendioe = randint(1500, 3000)
    mediastipendi = ((stipendioa + stipendiob + stipendioc + stipendiod + stipendioe)/5)
    print(mediastipendi)
    if q == -1:
        break
    
        
        


   
    

        


