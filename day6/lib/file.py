#encoding: utf-8
# -*- coding: utf-8 -*-

__author__ = 'editrobot'

import sys
import codecs
import os
import stat # needed for file stat
import shutil
import platform
from zipfile import * 
import zipfile
import glob
import json
from collections import deque

def path_path_split_code():
	sysstr = platform.system()
	if(sysstr =="Windows"):
		return '\\'
	elif(sysstr == "Linux"):
		return '/'
	else:
		return '/'

def read_json_file(filename):
	tempList = []
	with open(filename, 'r', encoding='utf8', errors='ignore') as f:
		done = 0
		while not done:
			str = f.read(1)
			if(str != ''):
				tempList.append(str.strip('\n'))
			else:
				done = 1
	return json.loads("".join(tempList))

#name  文件名
def read_file_to_str(name,encoding='utf8'):
	strl = ""
	with codecs.open(name, 'r', encoding=encoding, errors='ignore') as f:
		done = 0
		while not done:
			str = f.read(1)
			if(str != ''):
				strl = "%s%s" % (strl,str)
			else:
				done = 1
	return strl

#name  文件名 ,function  函数名
def read_str_file(name,function,encoding='utf8'):
	with codecs.open(name, 'r', encoding=encoding, errors='ignore') as f:
		done = 0
		while not done:
			str = f.read(1)
			if(str != ''):
				function(str)
			else:
				done = 1


def write_str_file(name,str):
	file = codecs.open(name,"w","utf-8")
	file.write(str)
	file.close()

# 按行读取文本
def read_line_file(name):
	return_list = []
	with codecs.open(name, 'r',"utf-8") as f:
		for line in f.readlines():
			return_list.append(line.strip()) # 把末尾的'\n'删掉
	return return_list

# 目录递归拷贝函数
def dir_copyTree(src, dst):
	names = os.listdir(src)
	# 目标文件夹不存在，则新建
	if not os.path.exists(dst):
		os.mkdir(dst)
	# 遍历源文件夹中的文件与文件夹
	for name in names:
		srcname = os.path.join(src, name)
		dstname = os.path.join(dst, name)
		try:
			# 是文件夹则递归调用本拷贝函数，否则直接拷贝文件
			if os.path.isdir(srcname):                
				dir_copyTree(srcname, dstname)
			else:
				if (not os.path.exists(dstname)
					or ((os.path.exists(dstname))
						and (os.path.getsize(dstname) != os.path.getsize(srcname)))):
					# print(dstname)
					shutil.copy2(srcname, dst)
		except:
			error.traceback();
			raise



# 删除整个文件夹
def del_all_dirfile(path):
	def remShut(*args):
		func, path, _ = args # onerror returns a tuple containing function, path and     exception info
		os.chmod(path, stat.S_IWRITE)
		os.remove(path)
	shutil.rmtree(path, onerror = remShut)

def getfilelist(path,mode = "filenames"):
	from os import walk
	f = []
	for (dirpath, dirnames, filenames) in walk(path):
		if mode == "dirnames":
			f.extend(dirnames)
		elif mode == "filenames":
			f.extend(filenames)
		elif mode == "dirpath":
			f.extend(dirpath)
	
	return f

def del_formatfile(src,format):
	import os
	n = 0
	for root, dirs, files in os.walk(src):
		# print(root, dirs, files)
		for name in files:
			if(name.endswith(format)):
				n += 1
				print(root,name)
				os.remove(os.path.join(root, name))

# 删除长方形尺寸的图片
def del_imgsize(src,format):
	import os
	for root, dirs, files in os.walk(src):
		print(root)
		for name in files:
			if(name.endswith(format)):
				# print(root+"\\"+name)
				from PIL import Image
				im = Image.open(root+"\\"+name)
				scale1 = im.size[0] / im.size[1]
				scale2 = im.size[1] / im.size[0]
				im.close()
				if scale1 > 1.4 or scale1 < 0.6 or scale2 > 1.4 or scale2 < 0.6:
					# print(root+"\\"+name)
					os.chmod(root+"\\"+name, stat.S_IWRITE)
					os.remove(os.path.join(root, name))

def copy_img(src, dst):
	import imghdr
	names = os.listdir(src)
	# 目标文件夹不存在，则新建
	if not os.path.exists(dst):
		os.mkdir(dst)
	# 遍历源文件夹中的文件与文件夹
	for name in names:
		srcname = os.path.join(src, name)
		dstname = os.path.join(dst, name)
		try:
			# 是文件夹则递归调用本拷贝函数，否则直接拷贝文件
			if os.path.isdir(srcname):
				copy_img(srcname, dstname)
			elif (not os.path.exists(dstname)
					or ( (os.path.exists(dstname)) and (os.path.getsize(dstname) != os.path.getsize(srcname))
					)
				):
					imgType == imghdr.what(imageFile)
					if imgType == "png" or imgType == "jpeg" or imgType == "gif":
						print(dstname)
						shutil.copy2(srcname, dst)
		except:
			error.traceback();
			raise
	
	
#解压zip文件 
def unzip(source_zip,target_dir):
	myzip=ZipFile(source_zip)
	myfilelist=myzip.namelist()
	for name in myfilelist:
		f_handle=open(target_dir+name,"wb")
		f_handle.write(myzip.read(name))
		f_handle.close()
	myzip.close()
	
#添加文件到已有的zip包中 
def addzip(ZipName,fileName): 
	f = zipfile.ZipFile(ZipName,'w',zipfile.ZIP_DEFLATED) 
	f.write(fileName)
	f.close()

#把整个文件夹内的文件打包 
def adddirfile(zipName,startdir): 
	files = glob.glob("%s/*" % startdir)
	print(files)
	f = zipfile.ZipFile(zipName,'w',zipfile.ZIP_DEFLATED)
	for file in files:
		print(file)
		f.write(file)
	f.close()

def imgtobase64(input):
	import base64
	f=open(input,'rb')
	ls_f=base64.b64encode(f.read())
	f.close()
	return ls_f.decode()

def imgthumbnail(input,output,scale = 1,w = None,h = None,format='jpeg'):
	# file.imgthumbnail("filetemp\\img\\%s" % (imgname),"filetemp\\img\\to%s" % (imgname),0.48)
	from PIL import Image
	# 打开一个jpg图像文件，注意是当前路径:
	im = Image.open(input)
	# 获得图像尺寸:
	if w == None or h == None:
		w, h = im.size
	w = w*scale
	h = h*scale
	print('Original image size: %sx%s' % (w, h))
	# 缩放到50%:
	im.thumbnail((w, h))
	print('Resize image to: %sx%s' % (w, h))
	# 把缩放后的图像用jpeg格式保存:
	im.save(output, format)


# file.setfontinimg('./db/DSC_0080.png',
		# '字符',
		# 100,
		# "#000000",
		# [(50, 150),(150, 250),(250, 350)],
		# './db/result.png')
def setfontinimg(src,text,fontsize,fontcolor,coordinates,dst):
	from PIL import Image, ImageDraw, ImageFont

	im = Image.open(src)
	draw = ImageDraw.Draw(im)
	myfont = ImageFont.truetype('simsun.ttc',fontsize)
	for xy in coordinates:
		draw.text(xy, text, font=myfont, fill=fontcolor)
	im.save(dst,'png')
	# im.show()

def mergeimg():
	from PIL import Image
	base_img = Image.open('./db/产品框图.png')
	target = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
	target_W,target_H = target.size

	# 加载需要狐狸像
	region = Image.open('./db/DSC_0080.png')
	regionW,regionH = region.size
	
	left = round((target_W - regionW)/2)
	top = round((target_H - regionH)/2)
	box = (left, top, left+regionW, top+regionH) #区域
	
	#确保图片是RGBA格式，大小和box区域一样
	region = region.convert("RGBA")
	region = region.resize((box[2] - box[0], box[3] - box[1]))
	#先将狐狸像合成到底图上
	target.paste(region,box)
	#将手机图覆盖上去，中间透明区域将狐狸像显示出来。
	target.paste(base_img,(0,0),base_img) #第一个参数表示需要粘贴的图像，中间的是坐标，最后是一个是mask图片，用于指定透明区域，将底图显示出来。
	# target.show()
	target.save('./db/out.png')  # 保存图片


def get_web_data(url,header,postDict):
	import gzip
	import re
	import http.cookiejar
	import urllib.request
	import urllib.parse

	def ungzip(data):
		try: # 尝试解压
			print('正在解压.....')
			data = gzip.decompress(data)
			print('解压完毕!')
		except:
			print('未经压缩, 无需解压')
		return data


	def getOpener(head):
		# deal with the Cookies
		cj = http.cookiejar.CookieJar()
		pro = urllib.request.HTTPCookieProcessor(cj)
		opener = urllib.request.build_opener(pro)
		header = []
		for key, value in head.items():
			elem = (key, value)
			header.append(elem)
		opener.addheaders = header
		return opener

	opener = getOpener(header)

	postData = urllib.parse.urlencode(postDict).encode()
	op = opener.open(url, postData)
	data = op.read()
	data = ungzip(data)

	return data


def readxml(str,left = ["<"," "],right = [">","="],filter = "\r\n"):
	t_list = []
	temp = ""
	for x in str:
		if x in left and not temp == "":
			t_list.append(temp)
			temp = x
		elif x in left:
			temp = x
		elif x in right and not temp == "":
			temp = "%s%s" % (temp,x)
			t_list.append(temp)
			temp = ""
		elif x in right:
			t_list.append(x)
		elif not x == filter:
			temp = "%s%s" % (temp,x)

	if not temp == "":
		t_list.append(temp)

	return t_list
def getxmlnode(xml,node):
	result = ""
	lock = False
	for x in xml:
		if x == "<"+node+">":
			lock = True
		elif x == "</"+node+">":
			lock = False
		elif lock:
			result += x
	return result

def cut_pn(str):
	q = deque(str)
	if q[0] == "<" or q[0] == ">":
		q.popleft()
	if q[-1] == "<" or q[-1] == ">":
		q.pop()
	return "".join(q)