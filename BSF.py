graf=[[0,1,0,0,1,0,0,0,1,0],                      #potrzebna jest reprezentacja grafu jako macierzy sasiedztwa
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
start=1                                            #podajemy punkt poczatkowy 


def BSF(graf,start):                               #funkcja potrzebuje 2 argumentow punktu startowego i grafu wyrazonego jako macierz sasiedztwa
    result=[start-1]
    queue=[]                                       #kolejka wierzcholkow do odwiedzenia
    j=start-1                                      #wybranie wierzcholka startowego
    while (len(result)<10):
   
        for y in range(len(graf[j])):               #przeszukiwanie macierzy w poszukiwaniu polaczen
            if(graf[j][y]==1 and ( y not in queue )and  y not in result): #jezeli wierzcholek jest polaczony z innym nie odwiedzonym ktorego nie ma na liscie jest on dodawany
                queue.append(y)
        result.append(queue[0])                     #wybieramy pierwszy wierzcholek z koleiki i jest on dodawany do rozwiazania
        j=queue[0]
        queue.pop(0)
    result = [x+1 for x in result]
    print(result)              



BSF(graf,start)                                     #przykladowe uzycie funkcji