keys = ["name","place","role"]

values = ["Anand","Cochin","Student"]

# {"name":"Anand","place":"Cochin","role":"Student"}

d = {}

for i in range(len(keys)):

    d[keys[i]] = values[i]

print(d)    #{'name': 'Anand', 'place': 'Cochin', 'role': 'Student'}