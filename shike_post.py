#coding=utf-8
import requests
import socket
def zan(sign):
	url = 'http://shike.com/shike/appShare/clickZan'
	data = {
	 'sign':sign,
	'zoid':'84UR6yiuGM1_'
	}
	count = 0
	for i in range(250):
		r = requests.post(url, data = data)
		d = eval(r.text)
		print u'第%d次:%s' % (i,d['data'])
		if d['data'] ==0.01:
			count = count + 1
			if count == 10:
				print 'ten times alredy'
				break
	return 1
def sub():
	url = 'http://shike.com/shike/api/appList?download=1&asin=qLgKdimlcEytwJYKW12%2F5y%2BvOZWEPz%2FwkmG17F3vLqsP6zo93qWp9DZjPmJCrze2ZS16OiesB7hUQFdlYdRNiCKlK%2FgH6J%2FWZIAVqs5vEg2GxDso8GBGfRGFSzKzMoK8GuaeRuoN1mQ22sddXP441GF16P%2BctzFgoMlf19r4oS4n%2F9gA254GbQRKb2XqS%2B3U%2Bh0RSu1vVYkniErN83gsERElTxFAwgxZ%2BF75Ob0j7gmkq1fZmGo360EtqJww9H78Vp%2BBdobDXx6FueTx7JYFgA%3D%3D'
	data = {
	'sign':'E4489162F89FEF3E0590A5057961B1A0346B3EB28E81FE1ABB7313CC708735CB51D167C549FEBD6D321B412C7ECFF6B3',
	'type':'1'
	}
	cookies = {
	'JSESSIONID':'504A493A9FB07C5F749A5FAB7A97798C',
	'OD':'zC5dvdXyP6DV+Qo/nENu2F8SS5D+5Xe+vY8LqBpJorPByY4vAcX+a6lHCEadqT51',
	'IORI':'eoI/lvo/hKa7K5smBj6EGLn7UedNSzevVWjlcKTCfvanIYdqCguX2RDEWaIpVNDmhFTIgEfNMYmr/dFPzeBJcvapKjOSyEwyHzWiA5D88g0=',
	'KYO':'oq-knTWXCazC7Q0-dDc8BTBpVy9-ov*l',
	'UIDD':'undefined'
	}
	r = requests.post(url, data = data, cookies = cookies)
	print r.text
	return 1
def start_zan(sign):
	url = 'http://shike.com/shike/appShare/startZan'
	data = {
	'sign':sign
	}
	r = requests.post(url, data = data)
	print r.text
def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 0))
        ip = s.getsockname()[0]
    except:
        ip = "x.x.x.x"
    finally:
        s.close()
    return ip
print getip()
#s = start_zan('GGqqJ3QKKYbIMoAGbSJ9HxkJtb95JpRJ')
s= zan(' GGqqJ3QKKYZj2WJcd8j7QOwcxVeVyYoN')
