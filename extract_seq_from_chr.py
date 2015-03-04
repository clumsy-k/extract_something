#!/bin/env python
# -*- coding:utf-8 -*-

# DNA配列から目的の領域を抜き出すプログラム (multi fasta は非対応)
# 入力は、
# 1. 染色体番号 2. 抜き出したい配列の開始点 3. 抜き出したい配列の終了点 4. 配列のストランド
# 5. ヘッダー情報 6. 出力ファイル名

import sys

usr_in_chr_num = raw_input("Please input chromosome number: ")
usr_in_start = raw_input("Please input sequence start number: ")
usr_in_end = raw_input("Please input equence end number: ")
usr_in_strand = raw_input("Please input strand, forward = 1 or reverse = 2: ")
usr_header_info = raw_input("Please input header information: ")
output_name = raw_input("Please input file name: ")

inputfile = open(sys.argv[1], 'r')

flag 	= False
num	= int(usr_in_chr_num)
start	= int(usr_in_start)
end	= int(usr_in_end)
strand	= int(usr_in_strand)
seq	= ''
extract	= ''

# 配列をA/T, T/A, G/C, C/Gに置換する関数
def change_seq(string):
	perfect_seq = ''
	for i in range(len(string)):
		if string[i] == "A":
			perfect_seq += "T"
		elif string[i] == "T":
			perfect_seq += "A"
		elif string[i] == "G":
			perfect_seq += "C"
		elif string[i] == "C":
			perfect_seq += "G"
		else:
			perfect_seq += string[i]

	return perfect_seq

# 読み込んだファイルの中の配列をつなげる
for line in inputfile:
	temp = line.rstrip()
	if flag:
		if temp[0] == ">":
			break
		else:
			seq += temp 
	if temp[0] == ">":
		judge = temp.split()[0]
		judge = judge.split(">")[1]
		if str(num) == str(judge):
			flag = True

# 配列の取得 (ストランドを考慮する)
if strand == 1:
	extract = seq[start:end]
else:
	extract = seq[start:end]
	extract = extract[::-1]
	extract = change_seq(extract)

# ファイルの書き出し
f = open(str(output_name) + ".out", 'w')
f.write(">" + str(usr_header_info) + "\n")
f.close()
f = open(str(output_name) + ".out", 'a')
f.write(extract)
f.close()
inputfile.close()
print "This chromosome sequence length is " + str(len(seq))
