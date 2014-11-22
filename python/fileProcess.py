fname = '/export/qhome/zyu/intersect/data/NC_OHWPA_FULL_2013_09_30/'
with open(fname) as f:
    content = f.readlines()
#print type(content)
myfile = open('/export/qhome/zyu/intersect/zhenglin/xyz.py', 'w')





for i in content:
    a = i.split('|')
    #print len(a)
    #print a

    sum_RTT_values = a[21]
    sum_RTT_counts = a[22]
    myfile.write('sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts) + '\n')


myfile.close()






fname = '/export/qhome/zyu/intersect/data/NC_OHWPA_FULL_2013_09_30/RNC.NC.OHWPA.PA.1380574800.dat'
f = open('/export/qhome/zyu/intersect/data/NC_OHWPA_FULL_2013_09_30/RNC.NC.OHWPA.PA.1380574800.dat', 'r')
content = f.readlines()
#print type(content)
myfile = open('/export/qhome/zyu/intersect/zhenglin/bigRTT2.txt', 'w')





for i in content:
    a = i.split('|')
    #print len(a)
    #print a
    sum_RTT_values = a[21]
    sum_RTT_counts = a[22]
    if int(sum_RTT_values) > 50: myfile.write('sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts) + '  divided results:'+ str(int(sum_RTT_values)/int(sum_RTT_counts))+ '\n')

f.close()
myfile.close()




f = open('/export/qhome/zyu/intersect/data/NC_OHWPA_FULL_2013_09_30/RNC.NC.OHWPA.PA.1380574800.dat', 'r')
content = f.readlines()
#print type(content)
myfile = open('/export/qhome/zyu/intersect/zhenglin/bigRTT.txt', 'w')





for i in content:
    a = i.split('|')
    #print len(a)
    #print a
    sum_RTT_values = a[21]
    sum_RTT_counts = a[22]
    if int(sum_RTT_values) > 50: myfile.write('sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts) + '  divided results:'+ str(float(sum_RTT_values)/float(sum_RTT_counts))+ '\n')

f.close()
myfile.close()





###################################################################
### Code for reading in gzip files for intersection project     ###
### Author: Ashwin Lall                                         ###
### Start date: 2013-11-16                                      ###
###################################################################
import gzip   # for reading in gzip files
import time   # for convering to epoch time f


# pair 1
rnc_item = {}
service_domain = {}

# pair 2
rnc_service = {}
item_domain = {}

# pair 3
rnc_domain = {}
item_service = {}

# pair 3
rnc_domain = {}
item_service = {}


'''
base_path = "/q/gp04/dpi/SQM2"

regions = ["NC/ILNWI", "NC/MININ", "NC/NSNMI", "NC/OHWPA", "NE/NWEND", "NE/NYCNJ", "NE/PANNJ", "NE/UPSNY", "NE/VAWVA", "NE/WADCM", "SC/ARNOK", "SC/MONKS", "SC/NTHTX", "SC/STHTX", "SE/ALMSL", "SE/GEORG", "SE/NCNSC", "SE/NTHFL", "SE/PRTRC", "SE/STHFL", "SE/TNNKY", "UK/AKRUK", "UK/ARLUK", "UK/ATCUK", "UK/BTCUK", "UK/BWYUK", "UK/CNCUK", "UK/STCUK", "UK/VNNUK", "UK/VTCUK", "WS/AZNMN", "WS/COUTW", "WS/LASCA", "WS/SDLVH", "WS/SFNSA", "WS/SORID"]

year = "2014"
month = "01"
day = "01"
hour = "00"


region = regions[0]
super_region = region[:2]
sub_region = region[3:]

# t = time.mktime(time.strptime("29.08.2011 11:05:02", "%d.%m.%Y %H:%M:%S"));
epoch_time = str(int(time.mktime(time.strptime(day + "." + month + "." + year + " " + hour + ":00:00", "%d.%m.%Y %H:%M:%S"))))

filename = base_path + "/" + region + "/FULL/" + year + "/" + month + "/" + day +  "/RNC." + super_region + "." + sub_region + ".PA." + epoch_time + ".dat.gz"


'''


import gzip
temp='/home/zyu/intersect/zhenglin/data/RNC.NE.NYCNJ.PA.1388548800.dat.gz'
f = gzip.open(temp, 'rb')
file_contents = f.read().strip()
f.close()

lines = file_contents.split("\n")

item_id_domain_id={}

myfile = open('/export/qhome/zyu/intersect/zhenglin/bruteForce.txt', 'w')
for i in range(len(lines)):
        line = lines[i]
        fields = line.split("|")

        #if item_id != 'PDA00201':continue
        sum_RTT_counts  = float(fields[21])
        sum_RTT_values = float(fields[22])
        divided = float(sum_RTT_values)/float(sum_RTT_counts)
        #if divided < 2e-5:continue
        timestamp = fields[0]
        rnc = fields[1]
        item_id = fields[10]
        service_category = fields[17]
        domain_id = fields[18]

        temp =item_id + "|" + domain_id
        if temp not in item_id_domain_id: item_id_domain_id[temp] = [sum_RTT_values, sum_RTT_counts]
        else: item_id_domain_id[temp] = [item_id_domain_id[temp][0]+sum_RTT_values, item_id_domain_id[temp][1]+sum_RTT_counts]

        #item_domain[item_id + "|" + domain_id] = item_domain.get(item_id + "|" + domain_id, 0) + 1

for i in item_id_domain_id:
    myfile.write( ' item_id__domain_id: ' + str(i)  +  'divided RTT results:'+ str(item_id_domain_id[i][0]/item_id_domain_id[i][1])+ '\n')


myfile.close()

        #print line
        #print timestamp, rnc, item_id, service_category, domain_id, sum_RTT_values, sum_RTT_counts

        #rnc_item[rnc + item_id] = [sum_RTT_values, sum_RTT_counts] if rnc + item_id in rnc_item else:[rnc_item[rnc + item_id][0]+ sum_RTT_values  ,  rnc_item[rnc + item_id][1] + sum_RTT_counts]
        #service_domain[service_category + domain_id]  = 0
        #rnc_service[rnc + service_category] = 0
        #item_domain[item_id + domain_id] = 0
        #rnc_domain[rnc + domain_id] = 0
        #item_service[item_id + service_category] = 0







temp='/home/zyu/intersect/zhenglin/data/RNC.NE.NYCNJ.PA.1388548800.dat'
f = open( temp, 'r')
file_contents = f.read().strip()
f.close()

lines = file_contents.split("\n")

item_id_domain_id={}

myfile = open('/export/qhome/zyu/intersect/zhenglin/right_Tue_Dec_31_23_00_00 2013.txt', 'w')
for i in range(len(lines)):
        line = lines[i]
        fields = line.split("|")
        item_id = fields[10]
        if item_id != 'PDA00201':continue
        sum_RTT_counts = float(fields[21])
        sum_RTT_values  = float(fields[22])
        divided = float(sum_RTT_values)/float(sum_RTT_counts)
        #if divided < 2e-5:continue
        '''
        timestamp = fields[0]
        rnc = fields[1]

        service_category = fields[17]
        domain_id = fields[18]

        temp =item_id + "|" + domain_id
        '''

        myfile.write( 'sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts)  + '  divided results:  '+ str(divided)+ '\n')

        '''
        if temp not in item_id_domain_id: item_id_domain_id[temp] = [sum_RTT_values, sum_RTT_counts]
        else: item_id_domain_id[temp] = [item_id_domain_id[temp][0]+sum_RTT_values, item_id_domain_id[temp][1]+sum_RTT_counts]

        #item_domain[item_id + "|" + domain_id] = item_domain.get(item_id + "|" + domain_id, 0) + 1

for i in item_id_domain_id:
    myfile.write( ' item_id__domain_id: ' + str(i)  +  'divided RTT results:'+ str(item_id_domain_id[i][0]/item_id_domain_id[i][1])+ '\n')
'''

myfile.close()











temp='/home/zyu/intersect/zhenglin/data/RNC.NE.NYCNJ.PA.1388548800.dat'
f = open( temp, 'r')
file_contents = f.read().strip()
f.close()

lines = file_contents.split("\n")

item_id_domain_id={}

myfile = open('/export/qhome/zyu/intersect/zhenglin/right_Tue_Dec_31_23_00_00 2013.txt', 'w')
for i in range(len(lines)):
        line = lines[i]
        fields = line.split("|")
        item_id = fields[10]
        if item_id != 'PDA00201':continue
        sum_RTT_counts = float(fields[21])
        sum_RTT_values  = float(fields[22])
        divided = float(sum_RTT_values)/float(sum_RTT_counts)
        divided =''
        #if divided < 2e-5:continue
        '''
        timestamp = fields[0]
        rnc = fields[1]

        service_category = fields[17]
        domain_id = fields[18]

        temp =item_id + "|" + domain_id
        '''

        if divided :
            myfile.write( 'sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts)  + '  divided results:  '+ str(divided)+ '\n')

        '''
        if temp not in item_id_domain_id: item_id_domain_id[temp] = [sum_RTT_values, sum_RTT_counts]
        else: item_id_domain_id[temp] = [item_id_domain_id[temp][0]+sum_RTT_values, item_id_domain_id[temp][1]+sum_RTT_counts]

        #item_domain[item_id + "|" + domain_id] = item_domain.get(item_id + "|" + domain_id, 0) + 1

for i in item_id_domain_id:
    myfile.write( ' item_id__domain_id: ' + str(i)  +  'divided RTT results:'+ str(item_id_domain_id[i][0]/item_id_domain_id[i][1])+ '\n')
'''

myfile.close()






temp='/home/zyu/intersect/zhenglin/data/RNC.NE.NYCNJ.PA.1388548800.dat'
f = open( temp, 'r')
file_contents = f.read().strip()
f.close()

lines = file_contents.split("\n")

item_id_domain_id={}

myfile = open('/export/qhome/zyu/intersect/zhenglin/A_certain_combination_Tue_Dec_31_23_00_00 2013.txt', 'w')
for i in range(len(lines)):
        line = lines[i]
        fields = line.split("|")
        item_id = fields[10]
        #if item_id != 'PDA00201':continue
        sum_RTT_counts = float(fields[21])
        sum_RTT_values  = float(fields[22])
        divided = float(sum_RTT_values)/float(sum_RTT_counts)
        divided = divided/1000
        #if divided < 2e-5:continue

        timestamp = fields[0]
        rnc = fields[1]
        item_id = fields[10]
        service_category = fields[17]
        domain_id = fields[18]

        if item_id == 'PG01229' and  timestamp == '201401010400' and  rnc == 'NYCMBSC14' and service_category == '29':
            myfile.write('timestamp ' + timestamp +  ' rnc ' + rnc + ' item_id ' + item_id +  ' service_category ' + service_category + ' domain_id '  + domain_id   +  ' sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts)  + '  divided results:  '+ str(divided)+' ms'+ '\n')



myfile.close()









temp='/home/zyu/intersect/zhenglin/data/RNC.NE.NYCNJ.PA.1388548800.dat'
f = open( temp, 'r')
file_contents = f.read().strip()
f.close()

lines = file_contents.split("\n")

item_id_domain_id={}

myfile = open('/export/qhome/zyu/intersect/zhenglin/Full_information_A_certain_combination_Tue_Dec_31_23_00_00 2013.txt', 'w')
for i in range(len(lines)):
        line = lines[i]
        fields = line.split("|")
        item_id = fields[10]
        #if item_id != 'PDA00201':continue
        sum_RTT_counts = float(fields[21])
        sum_RTT_values  = float(fields[22])
        divided = float(sum_RTT_values)/float(sum_RTT_counts)
        divided = divided/1000
        #if divided < 2e-5:continue

        timestamp = fields[0]
        rnc = fields[1]
        item_id = fields[10]
        service_category = fields[17]
        domain_id = fields[18]

        if item_id == 'PG01229' and  timestamp == '201401010400' and  rnc == 'NYCMBSC14' and service_category == '29':
            myfile.write(line+ '\n')



myfile.close()








temp='/home/zyu/intersect/zhenglin/data/RNC.NE.NYCNJ.PA.1388548800.dat'
f = open( temp, 'r')
file_contents = f.read().strip()
f.close()

lines = file_contents.split("\n")

item_id_domain_id={}

myfile = open('/export/qhome/zyu/intersect/zhenglin/A_certain_combination_Tue_Dec_31_23_00_00 2013.txt', 'w')
for i in range(len(lines)):
        line = lines[i]
        fields = line.split("|")
        item_id = fields[10]
        #if item_id != 'PDA00201':continue
        sum_RTT_counts = float(fields[21])
        sum_RTT_values  = float(fields[22])
        divided = float(sum_RTT_values)/float(sum_RTT_counts)
        divided = divided/1000
        #if divided < 2e-5:continue

        timestamp = fields[0]
        rnc = fields[1]
        item_id = fields[10]
        service_category = fields[17]
        domain_id = fields[18]

        myfile.write('timestamp ' + timestamp +  ' rnc ' + rnc + ' item_id ' + item_id +  ' service_category ' + service_category + ' domain_id '  + domain_id   +  ' sum_RTT_values:' + str(sum_RTT_values)+' sum_RTT_counts:'+str(sum_RTT_counts)  + '  divided results:  '+ str(divided)+' ms'+ '\n')



myfile.close()















###################################################################
### Code for reading in gzip files for intersection project     ###
### Author: Ashwin Lall                                         ###
### Start date: 2013-11-16                                      ###
###################################################################

import gzip   # for reading in gzip files
import time   # for convering to epoch time
import sys    # for command line arguments
import os
base_path = "/q/gp04/dpi/SQM2"

regions = ["NC/ILNWI", "NC/MININ", "NC/NSNMI", "NC/OHWPA", "NE/NWEND", "NE/NYCNJ", "NE/PANNJ", "NE/UPSNY", "NE/VAWVA", "NE/WADCM", "SC/ARNOK", "SC/MONKS", "SC/NTHTX", "SC/STHTX", "SE/ALMSL", "SE/GEORG", "SE/NCNSC", "SE/NTHFL", "SE/PRTRC", "SE/STHFL", "SE/TNNKY", "UK/AKRUK", "UK/ARLUK", "UK/ATCUK", "UK/BTCUK", "UK/BWYUK", "UK/CNCUK", "UK/STCUK", "UK/VNNUK", "UK/VTCUK", "WS/AZNMN", "WS/COUTW", "WS/LASCA", "WS/SDLVH", "WS/SFNSA", "WS/SORID"]

regions = ["NC/ILNWI"]

fraction = 0.05
if len(sys.argv) > 1:
        fraction = float(sys.argv[1])

year = "2013"
month = "01"
#day = "01"
days = ['01', '02', '03', '04', '05']

# pair 1
rnc_item = {}
service_domain = {}
# pair 2
rnc_service = {}
item_domain = {}
# pair 3
rnc_domain = {}
item_service = {}


# dictionary for all combinations
all_day01 = {}
all_day02 = {}
all_day03 = {}
all_day04 = {}
all_day05 = {}
myfile = open('/export/qhome/zyu/intersect/zhenglin/Different_dates_Tue_Dec.txt', 'w')
for r in range(len(regions)):
    for j in range(len(days)):
        for h in range(1):
                hour = str(h)
                hour = (2 - len(hour)) * "0" + hour

                region = regions[r]
                super_region = region[:2]
                sub_region = region[3:]

                #print region, hour
                day = days[j]
                # t = time.mktime(time.strptime("29.08.2011 11:05:02", "%d.%m.%Y %H:%M:%S"));
                epoch_time = str(int(time.mktime(time.strptime(day + "." + month + "." + year + " " + hour + ":00:00", "%d.%m.%Y %H:%M:%S"))))
                if not os.path.isfile(filename): continue
                filename = base_path + "/" + region + "/FULL/" + year + "/" + month + "/" + day +  "/RNC." + super_region + "." + sub_region + ".PA." + epoch_time + ".dat.gz"
                f = gzip.open(filename, 'rb')
                file_contents = f.read().strip()
                f.close()

                lines = file_contents.split("\n")
                if len(lines) == 1: # empty file
                        lines = []

                for i in range(len(lines)):
                        line = lines[i]
                        fields = line.split("|")

                        timestamp = fields[0]
                        rnc = fields[1]
                        item_id = fields[10]
                        service_category = fields[17]
                        domain_id = fields[18]
                        sum_RTT_counts = fields[21]
                        sum_RTT_values = fields[22]
                        if j==0:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day01:
                                all_day01[temp][0] = sum_RTT_counts
                                all_day01[temp][1] = sum_RTT_values
                            else:
                                all_day01[temp][0] = all_day01[temp][0] + sum_RTT_counts #if temp in all_day01 else sum_RTT_counts
                                all_day01[temp][1] = all_day01[temp][1] + sum_RTT_values #if temp in all_day01 else sum_RTT_values
                        elif j == 1:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day02:
                                all_day02[temp][0] = sum_RTT_counts
                                all_day02[temp][1] = sum_RTT_values
                            else:
                                all_day02[temp][0] = all_day02[temp][0] + sum_RTT_counts #if temp in all_day02 else sum_RTT_counts
                                all_day02[temp][1] = all_day02[temp][1] + sum_RTT_values #if temp in all_day02 else sum_RTT_values
                        elif j == 2:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day03:
                                all_day03[temp][0] = sum_RTT_counts
                                all_day03[temp][1] = sum_RTT_values
                            else:
                                all_day03[temp][0] = all_day03[temp][0] + sum_RTT_counts #if temp in all_day03 else sum_RTT_counts
                                all_day03[temp][1] = all_day03[temp][1] + sum_RTT_values #if temp in all_day03 else sum_RTT_values
                        elif j == 3:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day04:
                                all_day04[temp][0] = sum_RTT_counts
                                all_day04[temp][1] = sum_RTT_values
                            else:
                                all_day04[temp][0] = all_day04[temp][0] + sum_RTT_counts #if temp in all_day04 else sum_RTT_counts
                                all_day04[temp][1] = all_day04[temp][1] + sum_RTT_values #if temp in all_day04 else sum_RTT_values
                        elif j == 4:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day05:
                                all_day05[temp][0] = sum_RTT_counts
                                all_day05[temp][1] = sum_RTT_values
                            else:
                                all_day05[temp][0] = all_day05[temp][0] + sum_RTT_counts #if temp in all_day05 else sum_RTT_counts
                                all_day05[temp][1] = all_day05[temp][1] + sum_RTT_values #if temp in all_day05 else sum_RTT_values


'''
                        rnc_item[rnc + "|" + item_id] = rnc_item.get(rnc + "|" + item_id, 0) + 1
                        service_domain[service_category + "|" + domain_id]  = service_domain.get(service_category + "|" + domain_id, 0) + 1
                        rnc_service[rnc + "|" + service_category] = rnc_service.get(rnc + "|" + service_category, 0) + 1
                        item_domain[item_id + "|" + domain_id] = item_domain.get(item_id + "|" + domain_id, 0) + 1
                        rnc_domain[rnc + "|" + domain_id] = rnc_domain.get(rnc + "|" + domain_id, 0) + 1
                        item_service[item_id + "|" + service_category] = item_service.get(item_id + "|" + service_category, 0) + 1
'''

                        #all[rnc + "|" + item_id + "|" + service_category + "|" + domain_id] = all.get(rnc + "|" + item_id + "|" + service_category + "|" + domain_id, 0) + 1
'''
for key in all:
        (rnc, item_id, service_category, domain_id) = key.split("|")
        if all[key] >= fraction * rnc_service[rnc + "|" + service_category] and all[key] >= fraction * item_domain[item_id + "|" + domain_id]:
                print key#, all[key], rnc_service[rnc + "|" + service_category], item_domain[item_id + "|" + domain_id]
                '''
for i in all_day01:
    if i in all_day02 and i in all_day03 and i in all_day04 and i in all_day05:
        myfile.write('day 01 January ' + i + ' total sum_RTT_values:' + str(all_day01[1])+' total sum_RTT_counts:'+str(all_day01[0])  + '  divided results:  '+ str(divided)+' ms'+ '\n')
        myfile.write('day 02 January ' + i + ' total sum_RTT_values:' + str(all_day02[1])+' total sum_RTT_counts:'+str(all_day02[0])  + '  divided results:  '+ str(divided)+' ms'+ '\n')
        myfile.write('day 03 January ' + i + ' total sum_RTT_values:' + str(all_day03[1])+' total sum_RTT_counts:'+str(all_day03[0])  + '  divided results:  '+ str(divided)+' ms'+ '\n')
        myfile.write('day 04 January ' + i + ' total sum_RTT_values:' + str(all_day04[1])+' total sum_RTT_counts:'+str(all_day04[0])  + '  divided results:  '+ str(divided)+' ms'+ '\n')
        myfile.write('day 05 January ' + i + ' total sum_RTT_values:' + str(all_day05[1])+' total sum_RTT_counts:'+str(all_day05[0])  + '  divided results:  '+ str(divided)+' ms'+ '\n')

myfile.close()

#print len(rnc_item.keys()), len(service_domain.keys())
#print len(rnc_service.keys()), len(item_domain.keys())
#print len(rnc_domain.keys()), len(item_service.keys())
#print len(all.keys())






__author__ = 'zhenglinyu'


import gzip   # for reading in gzip files
import time   # for convering to epoch time
import sys    # for command line arguments
import os
base_path = "/q/gp04/dpi/SQM2"

regions = ["NC/ILNWI", "NC/MININ", "NC/NSNMI", "NC/OHWPA", "NE/NWEND", "NE/NYCNJ", "NE/PANNJ", "NE/UPSNY", "NE/VAWVA", "NE/WADCM", "SC/ARNOK", "SC/MONKS", "SC/NTHTX", "SC/STHTX", "SE/ALMSL", "SE/GEORG", "SE/NCNSC", "SE/NTHFL", "SE/PRTRC", "SE/STHFL", "SE/TNNKY", "UK/AKRUK", "UK/ARLUK", "UK/ATCUK", "UK/BTCUK", "UK/BWYUK", "UK/CNCUK", "UK/STCUK", "UK/VNNUK", "UK/VTCUK", "WS/AZNMN", "WS/COUTW", "WS/LASCA", "WS/SDLVH", "WS/SFNSA", "WS/SORID"]

regions = ["NC/ILNWI"]


year = "2014"
month = "01"
#day = "01"
days = ['06', '07', '08', '09', '10']

# pair 1
rnc_item = {}
service_domain = {}
# pair 2
rnc_service = {}
item_domain = {}
# pair 3
rnc_domain = {}
item_service = {}


# dictionary for all combinations
all_day01 = {}
all_day02 = {}
all_day03 = {}
all_day04 = {}
all_day05 = {}
print 'hi'
myfile = open('/export/qhome/zyu/intersect/zhenglin/Different_dates_Tue_Dec.txt', 'w')
for r in range(len(regions)):
    for j in range(len(days)):
        for h in range(4):
                hour = str(h)
                hour = (2 - len(hour)) * "0" + hour

                region = regions[r]
                super_region = region[:2]
                sub_region = region[3:]

                #print region, hour
                day = days[j]
                # t = time.mktime(time.strptime("29.08.2011 11:05:02", "%d.%m.%Y %H:%M:%S"));
                epoch_time = str(int(time.mktime(time.strptime(day + "." + month + "." + year + " " + hour + ":00:00", "%d.%m.%Y %H:%M:%S"))))

                filename = base_path + "/" + region + "/FULL/" + year + "/" + month + "/" + day +  "/RNC." + super_region + "." + sub_region + ".PA." + epoch_time + ".dat.gz"
                #print filename
                if not os.path.isfile(filename): continue
                #print 'one hour'
                f = gzip.open(filename, 'rb')
                file_contents = f.read().strip()
                f.close()

                lines = file_contents.split("\n")
                if len(lines) == 1: # empty file
                        lines = []

                for i in range(len(lines)):
                        line = lines[i]
                        fields = line.split("|")

                        timestamp = fields[0]
                        rnc = fields[1]
                        item_id = fields[10]
                        service_category = fields[17]
                        domain_id = fields[18]
                        sum_RTT_counts = float(fields[21])
                        sum_RTT_values = float(fields[22])
                        if j==0:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day01:
                                all_day01[temp] = [0, 0]
                                all_day01[temp][0] = sum_RTT_counts
                                all_day01[temp][1] = sum_RTT_values
                            else:
                                all_day01[temp][0] = all_day01[temp][0] + sum_RTT_counts #if temp in all_day01 else sum_RTT_counts
                                all_day01[temp][1] = all_day01[temp][1] + sum_RTT_values #if temp in all_day01 else sum_RTT_values
                        elif j == 1:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day02:
                                all_day02[temp] = [0, 0]
                                all_day02[temp][0] = sum_RTT_counts
                                all_day02[temp][1] = sum_RTT_values
                            else:
                                all_day02[temp][0] = all_day02[temp][0] + sum_RTT_counts #if temp in all_day02 else sum_RTT_counts
                                all_day02[temp][1] = all_day02[temp][1] + sum_RTT_values #if temp in all_day02 else sum_RTT_values
                        elif j == 2:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day03:
                                all_day03[temp] = [0, 0]
                                all_day03[temp][0] = sum_RTT_counts
                                all_day03[temp][1] = sum_RTT_values
                            else:
                                all_day03[temp][0] = all_day03[temp][0] + sum_RTT_counts #if temp in all_day03 else sum_RTT_counts
                                all_day03[temp][1] = all_day03[temp][1] + sum_RTT_values #if temp in all_day03 else sum_RTT_values
                        elif j == 3:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day04:
                                all_day04[temp] = [0, 0]
                                all_day04[temp][0] = sum_RTT_counts
                                all_day04[temp][1] = sum_RTT_values
                            else:
                                all_day04[temp][0] = all_day04[temp][0] + sum_RTT_counts #if temp in all_day04 else sum_RTT_counts
                                all_day04[temp][1] = all_day04[temp][1] + sum_RTT_values #if temp in all_day04 else sum_RTT_values
                        elif j == 4:
                            temp = rnc + "|" + item_id + "|" + service_category + "|" + domain_id
                            if temp not in all_day05:
                                all_day05[temp] = [0, 0]
                                all_day05[temp][0] = sum_RTT_counts
                                all_day05[temp][1] = sum_RTT_values
                            else:
                                all_day05[temp][0] = all_day05[temp][0] + sum_RTT_counts #if temp in all_day05 else sum_RTT_counts
                                all_day05[temp][1] = all_day05[temp][1] + sum_RTT_values #if temp in all_day05 else sum_RTT_values


for i in all_day01:
    if i in all_day02 and i in all_day03 and i in all_day04 and i in all_day05 and i in all_day01:

        myfile.write('day 01 January ' + i + ' total sum_RTT_values:' + str(all_day01[i][1])+' total sum_RTT_counts:'+str(all_day01[i][0])  + '  divided results:  '+ str((float(all_day01[i][1])/float(all_day01[i][0]))/1000)+' ms'+ '\n')
        myfile.write('day 02 January ' + i + ' total sum_RTT_values:' + str(all_day02[i][1])+' total sum_RTT_counts:'+str(all_day02[i][0])  + '  divided results:  '+ str((float(all_day02[i][1])/float(all_day02[i][0]))/1000)+' ms'+ '\n')
        myfile.write('day 03 January ' + i + ' total sum_RTT_values:' + str(all_day03[i][1])+' total sum_RTT_counts:'+str(all_day03[i][0])  + '  divided results:  '+ str((float(all_day03[i][1])/float(all_day03[i][0]))/1000)+' ms'+ '\n')
        myfile.write('day 04 January ' + i + ' total sum_RTT_values:' + str(all_day04[i][1])+' total sum_RTT_counts:'+str(all_day04[i][0])  + '  divided results:  '+ str((float(all_day04[i][1])/float(all_day04[i][0]))/1000)+' ms'+ '\n')
        myfile.write('day 05 January ' + i + ' total sum_RTT_values:' + str(all_day05[i][1])+' total sum_RTT_counts:'+str(all_day05[i][0])  + '  divided results:  '+ str((float(all_day05[i][1])/float(all_day05[i][0]))/1000)+' ms'+ '\n')

myfile.close()

#print len(rnc_item.keys()), len(service_domain.keys())
#print len(rnc_service.keys()), len(item_domain.keys())
#print len(rnc_domain.keys()), len(item_service.keys())
#print len(all.keys())


'''
                        rnc_item[rnc + "|" + item_id] = rnc_item.get(rnc + "|" + item_id, 0) + 1
                        service_domain[service_category + "|" + domain_id]  = service_domain.get(service_category + "|" + domain_id, 0) + 1
                        rnc_service[rnc + "|" + service_category] = rnc_service.get(rnc + "|" + service_category, 0) + 1
                        item_domain[item_id + "|" + domain_id] = item_domain.get(item_id + "|" + domain_id, 0) + 1
                        rnc_domain[rnc + "|" + domain_id] = rnc_domain.get(rnc + "|" + domain_id, 0) + 1
                        item_service[item_id + "|" + service_category] = item_service.get(item_id + "|" + service_category, 0) + 1


                        #all[rnc + "|" + item_id + "|" + service_category + "|" + domain_id] = all.get(rnc + "|" + item_id + "|" + service_category + "|" + domain_id, 0) + 1

for key in all:
        (rnc, item_id, service_category, domain_id) = key.split("|")
        if all[key] >= fraction * rnc_service[rnc + "|" + service_category] and all[key] >= fraction * item_domain[item_id + "|" + domain_id]:
                print key#, all[key], rnc_service[rnc + "|" + service_category], item_domain[item_id + "|" + domain_id]
fraction = 0.05
if len(sys.argv) > 1:
        fraction = float(sys.argv[1])



                '''

