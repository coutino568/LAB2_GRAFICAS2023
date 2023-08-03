
scale = 50

def vertexShader(vertex,**kwargs):
	# print(vertex)
	transformedVertex= [vertex[0]*scale, vertex[1]*scale,vertex[2]*scale]
	# print("transformed")
	# print(transformedVertex)
	return transformedVertex

def fragmentShader(**kwargs):
	color = (1,1,1)
	return color