#!/usr/bin/python
#Please enter your public.xml path into line bellow (EG. framework-res/res/values/public.xml)
public='framework-res/res/values/public.xml'
import os
def mid(line,n,n2):
	linee = ""
	i=n
	for i in range(n,n2):
		linee+=line[i]
	linee+='\n'
	return linee
fn = open(public,'r')
nf= open('public.lst','w')
for line in fn:
	t = line.find('id=')+4
	if t>3:
		line = mid(line,t,t+10)
		nf.write(line)
nf.close()
f = open('public.lst','r')
nf= open('public_sorted.lst','w')
nfs=[]
for line in f:
	nfs+=[line]
nfs.sort()
nfsd=""
for line in nfs:
	nfsd+=line
nf.write(nfsd)
f.close()
os.remove('public.lst')
nf.close()
f = open('public_sorted.lst','r')
nf= open('public_sorted.xml','w')
nf.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')
fn.seek(0,0)
for line in f:
	line=line[:-1]
	for liner in fn:
		if(liner.find(line)>=0):
			nf.write(liner)
	fn.seek(0,0)
nf.write('</resources>')
f.close()
os.remove('public_sorted.lst')
nf.close()
fn.close()
