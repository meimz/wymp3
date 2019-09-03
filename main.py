# -*- coding: utf-8 -*-
import os
import time

def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            if file_path.endswith('.uc'):
                list_name.append(file_path)

def change(inputFile,outPutFile):
    with open(inputFile,'rb') as f:
        a = f.read()
        f.close()
        dic={}
        with open(outPutFile,'wb') as f2:
            for i in a:
                f2.write(bytes([0xA3^i]))
            f2.close()
        f.close()

if __name__ =='__main__':
    print('''
    
    网易音乐缓存文件转mp3
    技术参考 鬼手 博客 https://blog.csdn.net/qq_38474570/article/details/87878235?tdsourcetag=s_pcqq_aiomsg
    作者 小葱
    
    将该exe文件放入缓存文件双击即可自动转换成同文件名的MP3文件
                                   
    本软件仅供学习请勿做其他用途 后果自负
    
    2019-09-03
    
    ''')
    mp3 = []
    listdir('./', mp3)
    print('共获取到{}个缓存文件'.format(len(mp3)))
    index=1
    for m in mp3:
        # if not m.endswith('.uc'):
        #     continue
        print('正在处理{}/{}'.format(index,len(mp3)))
        try:
            if os.path.exists(m.replace('.uc','.mp3')):
                print('{} 已处理跳过'.format(m))
                continue
            change(m,m.replace('.uc','.mp3'))
            print('处理成功{}'.format(m))
        except:
            print('处理失败{}'.format(m))
    print('60秒后自动关闭')
    time.sleep(60)