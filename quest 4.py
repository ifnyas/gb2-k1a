#code by @ifnyas

#input jumlah pembayaran dan harga produk
pay = input('bayar: ')
price = input('harga: ')

#menghitung jumlah kembalian
change = int(pay) - int(price)
print('total kembali: ' + str(change))

#fungsi kembalian
def sumofchange(change = 0):
  #pecahan 50k
  sumof50k = int(change / 50000)
  print ("\nkembali 50000: " + str(sumof50k) + ' lembar')
  change -= 50000 * sumof50k
  #print (change)

  #pecahan 20k
  sumof20k = int(change / 20000)
  print ("kembali 20000: " + str(sumof20k) + ' lembar')
  change -= 20000 * sumof20k
  #print (change)

  #pecahan 10k
  sumof10k = int(change / 10000)
  print ("kembali 10000: " + str(sumof10k) + ' lembar')
  change -= 10000 * sumof10k
  #print (change)

  #pecahan 5k
  sumof5k = int(change / 5000)
  print ("kembali  5000: " + str(sumof5k) + ' lembar')
  change -= 5000 * sumof5k
  #print (change)

  #pecahan 2k
  sumof2k = int(change / 2000)
  print ("kembali  2000: " + str(sumof2k) + ' lembar')
  change -= 2000 * sumof2k
  #print (change)

  #pecahan 1k
  sumof1k = int(change / 1000)
  print ("kembali  1000: " + str(sumof1k) + ' lembar')
  change -= 1000 * sumof1k
  #print (change)

  #pecahan 500
  sumof500 = int(change / 500)
  print ("kembali   500: " + str(sumof500) + ' lembar')
  change -= 500 * sumof500
  print ('\nsisa: ' + str(change))

sumofchange(change)