#-*- coding: utf-8 -*-

services = ('service_374','service_377','service_385','service_388','service_389','service_394','service_395','service_396','service_397','service_400','service_401')
services_cheb = ('service_377','service_385','service_388')

f1 = open("r-service.txt","w")
f2 = open("oktmo.txt", "r")

for line in f2.readlines():
    oktmo = line.split('\t')[0]
    for s in services:
        f1.write(s+','+oktmo+','+'FSU_'+oktmo+'\n')

f1.close
f2.close

f1 = open("r-service.txt","r+")
f2 = open("r_service_final.txt", "w")

for line in f1.readlines():
    oktmo = '97603'
    service = line[:11]
    if oktmo in line and service in services_cheb:
        line = line[:25]+'omsu_'+oktmo
        f2.write(line + '\n')    
    else:
        f2.write(line)
f1.close
f2.close