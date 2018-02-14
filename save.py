def export(data, file):
	tdata = data
	for key, value in tdata.items():
		for line in file:
			if line.split("=")[0] == key:
				line = key + "=" + value
			else:
				file.append(key + "=" + value)