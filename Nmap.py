import nmap
print("Nombre: César Alejandro Rodríguez Pérez -  Matricula: 1734223")
# take the range of ports to  
# be scanned 
begin =int(input("Ingres el incio: "))
end = int(input("Ingrese el final: "))
  
# assign the target ip to be scanned to 
# a variable 
target = input("Ingrese la ip: ")
str(target)
   
# instantiate a PortScanner object 
scanner = nmap.PortScanner() 
   
for i in range(begin,end+1):
    # scan the target port 
    res = scanner.scan(target,str(i))
    
    # the result is a dictionary containing  
    # several information we only need to 
    # check if the port is opened or closed 
    # so we will access only that information  
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']
    ar=open("ResE8CARP.csv","a")
    ar.write(res)
    ar.close()
    print(f'port {i} is {res}.')
   
