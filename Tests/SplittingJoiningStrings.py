song = "The rain in Spain..."
wds = song.split()
print(wds) 

s2= song.split("i")
print(s2) 

#Joining
wds=["red","blue","green"]
glue=";"
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message= by + " " + az + io + "," + qy
print(message)