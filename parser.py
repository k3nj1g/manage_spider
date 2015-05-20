#-*- coding: utf-8 -*-
import xlwt

services = ('service_374','service_385','service_388','service_389','service_394','service_395','service_397')

f = open('sp_r_service.txt', 'r')
#f_2 = open('output_f.txt','w')
book = xlwt.Workbook('utf8')
sheet = book.add_sheet('oktmo')

counter = 0
for line in f.readlines():
	oktmo = line.split('\t')[0]
	for s in services:
		sheet.write(counter,0,s)
		sheet.write(counter,1,oktmo)
		sheet.write(counter,2, 'FSU_'+oktmo)
		sheet.col(0).width = 200
		counter += 1
		#f_2.write( s +' '+oktmo+' '+oktmo+'\n' )
	
book.save('oktmo_CR.xls')
