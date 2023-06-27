graf=[[0,1,0,0,1,0,0,0,1,0],                          #potrzebna jest reprezentacja grafu jako macierzy sasiedztwa
   [1,0,1,1,0,0,0,0,0,0],
   [0,1,0,1,0,0,0,0,0,0],
   [0,1,1,0,0,0,0,0,0,0],
   [0,0,0,0,0,1,1,1,0,0],
   [0,0,0,0,1,0,0,0,0,0],
   [0,0,0,0,1,0,0,0,0,0],
   [0,0,0,0,1,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,1],
   [0,0,0,0,0,0,0,1,1,0],
   ]
start=1                                               #podajemy punkt poczatkowy 


def DSF(graf,start):                                  #funkcja potrzebuje 2 argumentow punktu startowego i grafu wyrazonego jako macierz sasiedztwa
    result=[start-1]
    #unvisited=[]
    visited = [False] * len(graf)
    visited[start-1]=True                             #czy wierzholek byl odwiedzony
    j=start-1                                         #wybranie wierzcholka startowego
    while (False in visited):
        
        for y in range(len(graf[j])):                 #przeszukiwanie macierzy w poszukiwaniu polaczen
            if(graf[j][y]==1 and not visited[y]  ):   #jezeli wierzcholek jest polaczony z innym nie odwiedzonym ktorego nie ma na liscie jest on dodawany
                result.insert(0,y)                              
                visited[y]=True
                j=result[0]
                break
                
            if(y==len(graf[j])-1 and  graf[j][y]!=1): #jeżeli nie ma poloczonych nie odwiedzonych wierzolkow
                                                      #sprawdzny jest pierwszy polaczony wierzolek
                for y in range(len(graf[j])):
                   if(graf[j][y]==1   ): 
                       result.insert(0,y) 
                       j=result[0]
                       break
                
            
        
        
    result.reverse()
    result = [x+1 for x in result]                    #powiekszenie wyniku o 1 poniewaz listy w pythonie zaczynaja sie od indexu 0
    print(result) 



DSF(graf,start)                                       #przykladowe uzycie funkcji