citylist = [
  'jakarta','surabaya','tokyo','oslo'
]

inputkota = input('Input City Name:')

i=0
while i<len(citylist):

  if citylist[i].lower() == inputkota.lower():
    print('Ketemu Di Index',i)
    break
  
  print('Tidak Ada Dalam Index',citylist[i])
  i +=1