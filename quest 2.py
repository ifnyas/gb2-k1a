#code by ifnyas

#input password
passw = input()

#verify password
def verify(passw):
  #set default condition
  up = False
  lo = False
  di = False
  le = False
  sp = False
  valid = False
  
  for p in passw:
    #check password has 8 char
    if (len(passw) == 8): le = True

    #check password has uppercase
    if p.isupper(): up = True
    
    #check password has lowercase
    if p.islower(): lo = True
    
    #check password has digit
    if p.isdigit(): di = True

    #check password has special char
    #asumption based on example: only '&' and '_' allowed
    if p == '&' or p == '_': sp = True
    
  #check password has all requirements
  if le == True and up == True and lo == True and di == True and sp == True: valid = True
  
  #debug
  #print(up, lo, di, sp, le)
  #print (valid)
  
  return valid

#run verify
verify(passw)