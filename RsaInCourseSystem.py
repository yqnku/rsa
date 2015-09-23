#!/usr/bin/python3
# -*- coding: <utf-8> -*-

#************************************************************************
# File Name: rsaPwd.py
# Author: yq
# Mail: xiqian013@live.com 
# Created Time: 2015/09/22
#************************************************************************

#RSA algorithm
import binascii
#public key
publicKey = int("00b6b7f8531b19980c66ae08e3061c6295a1dfd9406b32b202a59737818d75dea03de45d44271a1473af8062e8a4df927f031668ba0b1ec80127ff323a24cd0100bef4d524fdabef56271b93146d64589c9a988b67bc1d7a62faa6c378362cfd0a875361ddc7253aa0c0085dd5b17029e179d64294842862e6b0981ca1bde29979",16)

def Encrypt(pwd):
    #reverse
    pwd = pwd[::-1]
    #change to Ascii code
    pwdAscii = binascii.b2a_hex(bytes(pwd,encoding = 'gb2312'))
    pwdAscii = int(pwdAscii,16)
    #encrypt
    password = pwdAscii**65537%publicKey
    #change to hexadecimal
    password = hex(password)[2:]
    return password

if __name__ == "__main__":
    pwdStr = input("Enter your password:")
    print(Encrypt(pwdStr))

