#code by @ifnyas

#debug
#drawLine(8)

#drawing line
def drawLine(n):
  #membuat isi per baris
  garis = []

  #membuat isi baris i
  for i in range(0,n):
    #membuat spasi diakhiri *
    #asumsi jumlah spasi sebanyak i * 4
    garis.append( ' ' * i * 4 + '*' )
  
  #menggambar garis miring
  #asumsi setiap * berjarak 2 lines
  print("\n\n".join(garis)) 