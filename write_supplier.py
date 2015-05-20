#-*- coding: utf-8 -*-

services = ('service_374','service_377','service_385','service_388','service_389','service_394','service_395','service_396','service_397','service_400','service_401')
services_cheb = ('service_377','service_385','service_389','service_396','service_397','service_400','service_401')
services_ibresi = ('')
services_kanash = ('service_377','service_389')

f1 = open("r-service.txt","w")
f2 = open("oktmo.txt", "r")

for line in f2.readlines():
    oktmo = line.split('\t')[0]
    for s in services:
        f1.write(s+','+oktmo+','+'FSU_'+oktmo+'\n')

f1.close
f2.close


def set_omsu(r_services, oktmo):
    file = open("r-service.txt","r+")
    for line in file.readlines():
        service = line[:11]
        if oktmo in line:
            if service in r_services:
                line = line[:25]+'omsu_'+oktmo
                f2.write(line + '\n')    
            else:
                f2.write(line)
    file.close

f2 = open("r_service_final.txt", "w")
set_omsu(services_cheb, '97644')
set_omsu(services_kanash, '97616')
f2.close

