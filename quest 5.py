#code by @ifnyas

def count_handshake(num):
  #reset counter 1st person
  i = 0
  
  #reset counter handshake
  hs = 0

  #start handshaking from the 1st person
  while i < num:
    #reset counter 2nd person
    j = i + 1

    #start handshaking to the 2nd person
    while j < num:
      #count handshake + 1
      hs += 1

      #to the next 2nd person
      j += 1

    #to the next 1st person
    i += 1

  #return count handshake
  return hs

print(count_handshake(6))