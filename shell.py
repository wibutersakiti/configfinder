#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#kawan kelam copyright ga isin buncid

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("kawankelam.txt","r");
	link = raw_input("masukin namaweblu \n jangan pake http:// atau https:// \n karena udh gua tambahin jangan lupa web nya ke gini \n (ex : example.com or www.example.com ): ")
	print "\n\nweb di temukan  : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "ada nieh cok => ",req_link

def Credit():
	Space(9); print "_______________________"
	Space(9); print "#   *** config finder ***   #"
	Space(9); print "#     ganti worldlistnya di kawankelam.txt #"
	Space(9); print "#    kawan kelam @copyright 2021  #"
	Space(9); print "#______________________#"
Credit()
findAdmin()
