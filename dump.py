# uttf-8 coding python
# by kall xd , dont change author name!!

#> Module Yg Dibutuhkan
from rich import print as cetak
from rich.console import Console
import requests , json , re , os , time

#> Indication Init
ses = requests.Session()
uid , uid2 , uid3 = [] , [] , []
ok , cp , loop = 0 , 0 , 0

#> Jangan Di Hapus!!
data = {
  'Author' : 'Kall Xd' , 
  'Facebook' : '' , 
  'Github' : '',
  'Versi' : '1.0',
  'Script' : 'Dump',
  'Stat' : ''
}

def login():#> Buat Login (EAAB TOKEN)
	try:
		if data['Author'] == 'Kall Xd':pass
		else:cetak('[bold white]([bold red]x[bold white]) Mau Apa Hayoo!! Hargai Yg Buat!!');exit()
		os.system('clear')
		cetak('[bold white]([bold green]+[bold white]) Masukan Cookies Tumbal Anda')
		cok = {'cookie': Console().input('[bold white]([bold green]?[bold white]) Cookies : ')}
		link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
		gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
		get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
		tok = re.search('accessToken="(.*?)"',str(get)).group(1)
		open('tokek.txt' , 'w').write(tok)
		open('cokek.txt' , 'w').write(cok['cookie'])
		cetak('\n[bold white]([bold green]+[bold white]) Token : {}'.format(tok))
		exit()
	except(Exception) as e:
		cetak('[bold white]([bold green]x[bold white]) Cookies Mokad') ; time.sleep(3)
		login()
		
def uiditing():#> Cek Tumbal Dan Uid
	try:
		tok = open('tokek.txt' , 'r').read()
		cok = {'cookie': open('cokek.txt' , 'r').read()}
	except(FileNotFoundError):
		cetak('[bold white]([bold green]?[bold white]) Anda Belom Login') ; time.sleep(3)
		login()
	if data['Author'] == 'Kall Xd':pass
	else:cetak('[bold white]([bold red]x[bold white]) Mau Apa Hayoo!! Hargai Yg Buat!!');exit()
	try:
		params = {
		  'access_token': tok,
		  'fields': 'name,id'
		}
		po = ses.get('https://graph.facebook.com/me', params = params , cookies = cok).json()
		os.system('clear')
		cetak('[bold white]([bold green]+[bold white]) Welcome [bold green]{} [bold white]In Script Dump'.format(po['name']))
	except(KeyError):
		cetak('[bold white]([bold red]x[bold white]) Cookies anda mokad') ; time.sleep(3)
		login()
	try:
		uid = Console().input('[bold white]([bold green]?[bold white]) uid : ').split(',')
		if uid in ['' , ' ']:
			cetak('[bold white]([bold red]x[bold white]) Jangan Kosong')
			exit()
		cetak('\n[bold white]([bold green]![bold white]) Tekan [bold green]Ctrl+C [bold white]Untuk Stop')
		for i in uid:
			dumping(i , '' , tok , cok)
	except(KeyboardInterrupt) as e:
		loop = 0
		print('\r\n');cetak('[bold white]([bold green]+[bold white]) Contoh : [bold green]dump.txt')
		file = Console().input('[bold white]([bold green]?[bold white]) Nama File?: ')
		cetak('\n[bold white]([bold green]+[bold white]) Contoh [bold green]10009,10001,10003 [bold white]gunakan [bold green]"," [bold white]untuk pemisah')
		cetak('[bold white]([bold green]+[bold white]) Ketik [bold green]NEW [bold white]Untuk Uid New [bold green]OLD [bold white]untuk uid old [bold green] RANDOM [bold white]Untuk Uid Random')
		pisah = Console().input('[bold white]([bold green]?[bold white]) Pemisah Uid?: ')
		cetak('\n[bold white]([bold green]+[bold white]) Proses Memisahkan Uid')
		if pisah in ['old','OLD']:
			for x in uid3:
				id = x.split('|')[0]
				if len(id)<11:
					loop+=1
					cetak('[bold white]([bold green]+[bold white]) Mengumpulkan {}|{} Uid'.format(id,loop) , end = ' \r');time.sleep(0.0007)
					with open(file , 'a') as kall:
						kall.write(x +'\n')
			cetak('\n[bold white]([bold green]+[bold white]) Dump Selesai Tersimpan Di [bold green]{}'.format(file))
		elif pisah in ['NEW','new']:
			for x in uid3:
				id = x.split('|')[0]
				if len(id)<11:
					pass
				else:
					if len(id)<15:
						loop+=1
						cetak('[bold white]([bold green]+[bold white]) Mengumpulkan {}|{} Uid'.format(id,loop) , end = ' \r');time.sleep(0.0007)
						with open(file , 'a') as kall:
							kall.write(x +'\n')
			cetak('\n[bold white]([bold green]+[bold white]) Dump Selesai Tersimpan Di [bold green]{}'.format(file))
		elif pisah in ['RANDOM','random']:
			for x in uid3:
				loop+=1
				id = x.split('|')[0]
				cetak('[bold white]([bold green]+[bold white]) Mengumpulkan {}|{} Uid'.format(id,loop) , end = ' \r');time.sleep(0.0007)
				with open(file , 'a') as kall:
					kall.write(x +'\n')
			cetak('\n[bold white]([bold green]+[bold white]) Dump Selesai Tersimpan Di [bold green]{}'.format(file))
		else:
			for x in uid3:
				id = x.split('|')[0]
				for tahun in pisah.split(','):
					if id[0:5]==tahun:
						loop+=1
						cetak('[bold white]([bold green]+[bold white]) Mengumpulkan {}|{} Uid'.format(id,loop) , end = ' \r');time.sleep(0.0007)
						with open(file , 'a') as kall:
							kall.write(x +'\n')
			cetak('\n[bold white]([bold green]+[bold white]) Dump Selesai Tersimpan Di [bold green]{}'.format(file))
		
def dumping(uidz , after , tok , cok):#> Buat Dump Uid
	try:
		if data['Author'] == 'Kall Xd':pass
		else:cetak('[bold white]([bold red]x[bold white]) Mau Apa Hayoo!! Hargai Yg Buat!!');exit()
		if len(uid)==0:
			params = {
			  'access_token': tok,
			  'fields': 'friends'
			}
		else:
			params = {
			  'access_token': tok,
			  'fields': 'friends.after({})'.format(after)
			}
		po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
		for x in po['friends']['data']:
			try:
				berkelanjutan(str(x.get('id')) , '' , tok , cok)
				uid.append(str(x.get('id')))
			except(KeyError):
				pass
		afr = po['friends']['paging']['cursors']['after']
		dumping(uidz , afr , tok , cok)
	except(KeyError) as e:
		if len(uid3)==0:
			cetak('[bold white]([bold green]![bold white]) Uid Tydak Publik')
		else:
			cetak('\n\n[bold white]([bold green]![bold white]) Kesalahan [bold green]{}'.format(e))
			Console().input('[bold white]([bold green]![bold white]) Cookies Mokad Silahkan Ctrl+C + Tekan Enter Untuk Selanjutnya')
		
def berkelanjutan(uidz , after2 , tok , cok):#> Dump Sesi 2
	if len(uid2)==0:
		params = {
		  'access_token': tok,
		  'fields': 'friends'
		}
	else:
		params = {
		  'access_token': tok,
		  'fields': 'friends.after({})'.format(after2)
		}
	po2 = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
	if 'paging' in po2['friends']:
		for x in po2['friends']['data']:
			uid2.append(str(x.get('id')))
			uid3.append(str(x.get('id'))+'|'+str(x.get('name')))
		cetak('[bold white]([bold green]![bold white]) Mengumpulkan [bold green]{}|{} [bold white]Uid'.format(str(x.get('id')) , len(uid3)) , end = ' \r')
	else:
		uid2.clear()
	afr2 = po2['friends']['paging']['cursors']['after']
	berkelanjutan(uidz , afr2 , tok , cok)
	
if __name__ == '__main__':
	if Console().width>=88:
		os.system('clear')
		cetak('[bold white]([bold green]+[bold white]) Lebar Terminal {}'.format(Console().width))
		cetak('[bold white]([bold green]+[bold white]) Lebar Terminal Pas Selamat Menggunakan Script')
		time.sleep(3)
		if data['Author'] == 'Kall Xd':uiditing()
		else:cetak('[bold white]([bold red]x[bold white]) Mau Apa Hayoo!! Hargai Yg Buat!!');exit()
	else:
		os.system('clear')
		cetak('[bold white]([bold green]+[bold white]) Lebar Terminal {}'.format(Console().width))
		cetak('[bold white]([bold green]x[bold white]) Tolong Kecilkan Layar Terminal Anda Dengan [bold green]Mencubit [bold white]Layar Anda Hingga Angka [bold green]88 [bold white]!!');exit()