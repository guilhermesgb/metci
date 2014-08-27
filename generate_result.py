import linecache
import sys
import string

results = {
    "carga" : [ [ "0" for i in range(9) ] for j in range(10) ],
    "consulta" : [ [ "0" for i in range(9) ] for j in range(10) ],
    "memoria" : [ [ "0" for i in range(9) ] for j in range(10) ]
}

offset = {
    "carga" : 1,
    "consulta" : 2,
    "memoria" : 3
}

for tipo in results.keys():
  for j in range(10):
    for i in range(9):
      result_path = "treatments/treatment_"+str(i)+"/run_"+str(j)+"/result"

      if ( i % 3 == 0 ):
        pos = 1000
      elif ( i % 3 == 1 ):
        pos = 10000
      else:
        pos = 100000
      pos = pos + offset[tipo]

      line = linecache.getline(result_path, pos)
      print "line is: ", line
      if ( tipo == "carga" ):
        line = line.replace("tempo_de_carga: ", "").replace(" segundos", "")
      elif ( tipo == "consulta" ):
        line = line.replace("tempo_da_consulta: ", "").replace(" segundos", "")
      else:
        line = line.replace("consumo_de_memoria: ", "").replace(" MB", "")
      print "line now is: ", line
      results[tipo][j][i] = line.strip()

  new = open(tipo+".csv", "w")
  for i in range(10):
    new.write(string.join(results[tipo][i],",") + "\n")
  new.close()
