import math
def _main() -> None:
  n = int(input())
  valorPociones = input()
  h = 0
  k = 1
  p = 2
  
  listaPociones = valorPociones.split(" ")
  listaPociones = [eval(i) for i in listaPociones] 
  
  estadisticas = input()
  listaEstadisticas = estadisticas.split(" ")
  listaEstadisticas = [eval(j) for j in listaEstadisticas]
  
  s = listaEstadisticas[p] - math.ceil((math.pow(listaEstadisticas[k], 2) * listaEstadisticas[p]) / listaEstadisticas[h])
  pf = listaEstadisticas[p] - s
  pociones = 0
  x = 1
  while listaEstadisticas[k] >= x :
    
    listaEstadisticas[h] = listaEstadisticas[h] - pf

    while listaEstadisticas[h] <= pf:
      listaEstadisticas[h] = listaEstadisticas[h] + listaPociones[pociones]
      pociones+=1
      if listaEstadisticas[h] > 0 and listaEstadisticas[h] > pf:
        x+=1
        break
    x+=1  
      
  print("POCIONES: ",pociones)
  print("ESCUDO: ",s)
  
  pass

if __name__ == '__main__':
  _main()