#run commandline - pip install Covid 

from covid import Covid

covid= Covid()
x=str(input("read country name:"))
cases= covid.get_status_by_country_name(x)
for x in cases:
	print(x,":",cases[x])