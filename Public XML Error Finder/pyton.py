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
def c(x):
    return {
		0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
    }.get(x,'E')
def h(x):
    return {
		'0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
    }.get(x,16)
def linem1(line,i):
	print line
	j=0
	linee=''
	for j in range(i):
		if (h(line[i-j])==0):
			linee+='f'
			line=line[:-1]
		else:
			linee+=c(h(line[i-j])-1)
			line=line[:-1]
			break
	i=0
	for i in range(j+1):
		line+=linee[j-i]
	print line
	return line
def chtohex(ch,i,i2):
	j=i
	he=0
	po=1
	for j in range(i,i2):
		po*=16
	j=i
	for j in range(i,i2):
		po/=16
		if(h(ch[j])==16):print 'Error in chtohex'
		he+=(h(ch[j])*po)
	return he
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
nf.close()
os.remove('public.lst')
f = open('public_sorted.lst','r')
values=[]
for line in f:
	values += [(line [2] + line [3] + line [4] + line [5])]
values=list(set(values))
values.sort()
fn.seek(0,0)
f.seek(0,0)
temp=-1
nf = open('error.txt','w')
error=0
for i in values:
	for line in f:
		if(i==(line [2] + line [3] + line [4] + line [5])):
			iline = chtohex(line,6,10)
			if (temp!=-1):
				if(iline!=temp+1):
					nf.write('error in line(s):\n\n')
					line=line[:-1]
					j=0
					k=0
					for liner in fn:
						j+=1
						if(liner.find(line)>=0):
							k+=1
							nf.write(str(j)+'|'+liner)
					if(k>1):
						nf.write('Why?\n	because there were '+str(k)+' values with same id('+line+')\n\n')
					if(k==1):
						line=linem1(line,9)
						nf.write('Why?\n	because there were no values with ('+line+') id\n	you can not simply skip that\n\n')
					if(k<=0):
						nf.write("not sure why but couldn't find any with ("+line+") id in public.xml\n	you might wanna look for that id again\n\n")
					fn.seek(0,0)
					error+=1
			else:
				if (iline!=0):
					nf.write('error in line:\n\n')
					line=line[:-1]
					j=0
					k=0
					for liner in fn:
						j+=1
						if(liner.find(line)>=0):
							nf.write(str(j)+'|'+liner)
					print line
					line=line[:-4]
					nf.write('Why?\n	because there were no values with ('+line+'0000) id\n	you can not simply skip that\n\n')
					error+=1
			temp=iline
	f.seek(0,0)
	temp=-1;
if (error==0):
	print '	No error found!'
	os.remove('error.txt')
else:
	print '	found '+str(error)+' error'
	print '	you can see it in error.txt file'
os.remove('public_sorted.lst')
print "	happy 'dev'ing :-D"
print '	-sijav'
