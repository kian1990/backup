#!/usr/bin/python
#coding=utf-8

import os
import time

source_dir='./source'
backup_dir='./backup'
dir_year=backup_dir+os.sep+time.strftime('%Y')
dir_month=dir_year+os.sep+time.strftime('%m')
dir_date=dir_month+os.sep+time.strftime('%d')
backup_file=dir_date+os.sep+time.strftime('%H%M%S')+'.tar.gz'
if not os.path.exists(backup_dir):
	os.mkdir(backup_dir)
if not os.path.exists(dir_year):
	os.mkdir(dir_year)
if not os.path.exists(dir_month):
	os.mkdir(dir_month)
if not os.path.exists(dir_date):
	os.mkdir(dir_date)
tar_command='tar -zcvf {0} {1}'.format(backup_file,source_dir)
print('tar command is:')
print(tar_command)
print('running...')
if os.system(tar_command)==0:
	print('successful backup to:',backup_file)
else:
	print('backup failed!')