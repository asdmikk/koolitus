#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# Athor: Konstantin Tenman
# Date: 2014-10-17

import time

######## for 3.2 Vanus #########
import datetime              ###
today = datetime.date.today()###
year_now = today.year        ###
month_now = today.month      ###
day_now = today.day          ###
################################

#name = str(input('Sisesta palun nimi: '))
ID = str(input('Sisesta palun isikukood: '))
name = 'k'
#ID = '39706100250'

century = int(ID[0])
year = int(ID[1:3])
month = int(ID[3:5])
day = int(ID[5:7])
year_prefix = [1800, 1900, 2000]

months = (
'jaanuar',
' veebruar',
' märts',
' aprill',
' mai',
' juuni',
' juuli',
' august',
' september',
' oktoober',
' november',
' detsember'
)

kordajad1 = (1,2,3,4,5,6,7,8,9,1)
kordajad2 = (3,4,5,6,7,8,9,1,2,3)
n = summa = vanus = 0

################################ 3.1. VANUS ####################################

##current = time.localtime()
##current_in_seconds = time.mktime((current[0],current[1],current[2],0,0,0,0,0,0))
##birth_in_seconds = 0
##current_2 = time.time()
##
##if century in (1, 2):
##    birth_in_seconds = time.mktime(((year_prefix[0] + year),month,day,0,0,0,0,0,0))
##    vanus = int((current_2 - birth_in_seconds)//(60*60*24*365.25))
##elif century in (3, 4):
##    birth_in_seconds = time.mktime(((year_prefix[1] + year),month,day,0,0,0,0,0,0))
##    vanus = int((current_2 - birth_in_seconds)//(60*60*24*365.25))
##elif century in (5, 6):
##    birth_in_seconds = time.mktime(((year_prefix[2] + year),month,day,0,0,0,0,0,0))
##    vanus = int((current_2 - birth_in_seconds)//(60*60*24*365.25))

###############################################################################
    
################ 3.2. VANUS #####################
if century == 0:
    print("Isikukood on vale, sest sajand ei saa olla '0'.") 
elif century <= 2:
    if month < month_now or (month == month_now and day <= day_now):
        vanus = year_now - year - year_prefix[0]
    else:
        vanus = year_now - year - year_prefix[0] - 1
elif century <= 4:
    if month < month_now or (month == month_now and day <= day_now):
        vanus = year_now - year - year_prefix[1]
    else:
        vanus = year_now - year - year_prefix[1] - 1
elif century <= 6:
    if month < month_now or (month == month_now and day <= day_now):
        vanus = year_now - year - year_prefix[2]
    else:
        vanus = year_now - year - year_prefix[2] - 1
else:
    print("Isikukood on vale, sest sajand on tulevikus.") 
###############################################

################### KONTROLL ##################
for i in range(10):
    summa += int(ID[n]) * kordajad1[i]
    n+= 1
if summa%11 != 10:
    viimane = summa%11
else:
    n = summa = 0
    for kordaja in kordajad2:
        summa += int(ID[n]) * kordaja
        n += 1
    if summa%11 != 10:
        viimane = summa%11
    else:
        viimane = 0
# võrdleme viimast numbrit
accuracy = "õige"
if viimane != int(ID[10]):
    accuracy = "vale"

####################### PRINT RESULTS ######################### 
# 0. Isik
print("_________________________________________")
print("Isik: %s"% name)
# 1. Sünnipäev
print("Sünnipäev: %d.%s"% (day, months[month-1]))

# 2. Sugu
sugu = "NAINE"
if century%2 != 0:
    sugu = "MEES"
print("Sugu: %s"% sugu)

# 3. Vanus
print("Vanus: %d"% vanus)

# 4. Kontrollsumma    
print("Isikukood on %s, sest viimane number: %d!"% (accuracy, viimane))
print("-------------------------------------------------------------")
