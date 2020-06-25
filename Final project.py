# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:58:06 2019

@author: Ray
"""
from bs4 import BeautifulSoup 
import requests
import youtube_dl
import lyricwikia


name = input("please enter the singer's name:") #輸入喜歡的歌手的名字(外國歌手)
url="https://www.youtube.com/results?search_query="+name #利用youtube搜尋網站  
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content,"html.parser") #製成湯

for all_mv in soup.select(".yt-lockup-video"): #找到source code第一層loop的.yt-lockup-video
    
    
    data = all_mv.select(".yt-lockup-meta-info")#找到source code第二層loop的.yt-lockup-meta-inf
    time = data[0].get_text("#").split("#")[0]#找到發佈時間
    see = data[0].get_text("#").split("#")[1]#找到觀看人數
    
    data = all_mv.select("a[rel='spf-prefetch']")#找到source code第二層loop的a[rel='spf-prefetch']
    print("名稱: {}".format(data[0].get("title")))#找到標題並印出
    print("連結: https://www.youtube.com{}".format(data[0].get("href")))#找到此影片在youtube上的連結

    print("發佈時間"+" "+ time)#印出發佈時間
    print("觀看人數"+" "+see)#印出觀看次數
    
      
    answer=input("do you want the lyric of this song?(Y/N)")#讓使用者選擇是否要這首歌的歌詞
    if answer.lower()=="y":

      #將標題完善化增加lyricwikia API找到歌詞的機會        
        songname=str()
        songname = data[0].get("title")
        first=songname.find("-")
        end=songname.find("(")  
    
        if end == -1:
            songname=songname[first+2:]
        else:
            songname=songname[first+2:end]
       #將標題完善化增加lyricwikia API找到歌詞的機會           
                      
        try:        
            lyrics = lyricwikia.get_lyrics(name,songname)
            print(lyrics)
               
        except:
            print("Sorry we cannot found the lyric of this song")#若找不到歌詞印出Sorry we cannot found the lyric of this song
            continue
            
        download=input("do you want to download this song?(Y/N)")#詢問使用者是否要下載此歌曲mp4
        if download.lower()=="y": 
                   #下載此歌曲
            url="https://www.youtube.com"+data[0].get("href") 
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                  #下載此歌曲
            
        key=input("Do you wan't to continue?(Y/N)")
        if key.lower()=="n":
            break
                    
    else:
        continue
    

print("THANK YOU!!!!!")
    
#example singers
#maroon 5
#Calum Scott
#Adele etc