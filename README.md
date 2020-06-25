# python-web-crwaling

Project name : 吉谱車
===
Project description: 
==
我想做這個project的原因是因為我常常會在youtube上面瀏覽影片，聽聽排行榜上的音樂。<br>
當聽到好聽的音樂或我喜歡的歌手時我就想要去網站上找他們的吉他譜。但如果有一個程式可<br>
以直接輸入網址後便能找到與這首歌曲風相似的歌曲不就很好嗎？所以我便利用這次的final project<br>
來完成我的一個小小的心願。<br>

Project planning:
==
這個程式的運作方法如下: 先在youtube上搜尋喜歡的歌手，把網址複製下來後輸入進入這個程<br>
式之中。這個程式便會開始爬youtube網頁上的html，利用Beautifulsoup找到一些重要內容，包含<br>
所有的歌曲名稱，觀看人數，發布時間等等資訊。之後再利用python ultimate guitar 的API (pipe PYPI)<br>
所回傳的json格式中找到吉他譜。最後再將所有資訊包含吉他譜一起輸出。我將這次的final project<br>
分成了三個部分，第一個部分是youtube網頁html的爬蟲，這個部份我覺得我比較熟悉，所以我給的時間會比<br>
較短一點。第二部分是利用多次的Web API，這個部份對我而言比較困難，我的時間會拉的必較長一點。最後<br>
則是測試程式(應該不用很久吧)。
Timeline: 12/31 以前做完 youtube 網頁的爬蟲
		 1/16 以前做完API 的程式碼
		 1/17 以前完成多次測試
 



Update 1
===
What I have done?
I finish using Youtube API search website while the user enter a singer’s name and using<br>
beautiful soup to crawl the 發布時間 觀看人數 連結 以及 名稱 and choose Y if you like this song<br>
and N if you do not like this song.(if Y, the program will find the guitar tab and download it)
Changes
I finally choose py ultimate guitar to be my second API and I plan to use pytube in the future<br>
if I have enough time.<br>
Timeline of the rest
I will finish my whole program before 1/15. I will finish all my other tests in 1/9, so I will <br>
got plenty of time to finish and complete my final project.<br>


Update2
===

I change using ultimate guitar pypi to find guitar lab because the PYPI have right reserved, and <br>
should py money for using it .Thus, I change my project intention to find the lyric of the song by<br>
using lyricwika Pypi. Also, I cannot success to download my video by pytube, it runs out that the url <br>
did not have a kind of form and I don,t really know what’s wrong with it. So I change to use youtube-dl<br>
Pypi to download the video.<br>

Run 
=
First, you should pip install youtube_dl and lyricwikia and beautiful soup. Then, you can start to run the <br>
project. First, the project will request the user to enter a singer’s name(for example Adele, maroon 5 etc). <br>
Then the project will demo a song and request the user to enter Y if you wan’t the lyric of the song(enter N if <br>
user do not want the lyric of the song), after it, the program will request user to enter Y if you wan’t to download<br>
the song, and enter Y if user would like to continue to the next song.<br>

