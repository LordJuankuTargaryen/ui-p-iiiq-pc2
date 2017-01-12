

grados = float(input("escriba la cantidad de grados de temperatura farenheit\n"))


conversion = (grados -32) * 5 /9
print ("los grados celsius es de : " + str (conversion ))
if grados >= 100:
	print ('y eso es caliente!! ')

else:
	print ("y eso es frio!!")
