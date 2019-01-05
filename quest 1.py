#code by ifnyas

#python to json
import json

def returnjson():
  #input name
  name = 'Irfan'

  #input address
  address = 'Bandung'

  #input hobbies
  hobbies = ['gaming', 'futsal']

  #input is_married
  is_married = False

  #input school
  school = {
    'highSchool':'SMAN 2 Bandung',
    'university':'Universitas Padjadjaran'
  }

  #input skill
  sk1 = 'hustler'
  sk2 = 'hipster'
  sk3 = 'hacker'
  skill = [sk1, sk2, sk3]

  #convert to json
  biodata = [name, address, hobbies, is_married, school, skill]
  biojson = json.dumps(biodata)

  #debug
  #print (biojson)

  return biojson

#debug
#returnjson()