import math
def _main() -> None:
  n = int(input())
  a = input()
  h = 0
  k = 1
  p = 2
  
  lista = a.split(" ")
  listaPociones = [eval(i) for i in lista] 
  estadisticas = input()
  lista2 = estadisticas.split(" ")
  listaEstadisticas = [eval(j) for j in lista2]
  
  resultado = listaEstadisticas[k] * listaEstadisticas[p] 
  resultado2 = resultado / listaEstadisticas[h]
  s = listaEstadisticas[p] - math.ceil(resultado2 * listaEstadisticas[k])
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