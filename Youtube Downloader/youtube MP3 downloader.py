import youtube_dl
from youtube_search import YoutubeSearch
import json
from shutil import move


songs = str("""Mehndi hai rachne waali,Dil chori sadda ho gaya,Mehndi Laga Ke Rakhna, Maine Payal Hai Chhankai,sadi gali,Ainvayi Ainvayi,Tenu Leke,Gujarati geet-mehndi te vavi,Kabira,Baari Barsi,Saajanji Ghar Aaye,Chunnari Chunnari,Bumbro,Mohabbatein Pairon Mein Bandhan Hai,Kithe chaliye morni banke,Dilli wali girlfriend,Coca cola,Kala chashma,Laal ghaghra,Maahi ve,Where's the party tonight,Iski Uski,Laung Da Lashkara,Abhi Toh Party Shuru Hui Ha,Mauja Hi Mauja,nagada nagada,Balam Pichkari,Kar Gayi Chull,Ghagra ,Salaam-E-Ishq ,Aapka Kya Hoga Janabe Ali,Sajanaji Vari Vari""").replace('\n', '')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
total_duration = 0
id = 1
youtube_short_url_prefix = 'youtu.be'
for song in songs.split(','):
    JSON = json.loads(YoutubeSearch(song, max_results=1).to_json())
    filename = str(JSON['videos'][0]['title'])
    duration = str(JSON['videos'][0]['duration'])
    results = str(youtube_short_url_prefix + JSON['videos'][0]['url_suffix'])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(json.loads(YoutubeSearch(song, max_results=1).to_json()))
        ydl.download([results])
        # move(filename.replace('|', '_').replace(':', ' -')+'-' +
        #      JSON['videos'][0]['id']+'.mp3', str(id)+'.mp3')
        total_duration += (int(duration.split(':')
                               [0])*60)+(int(duration.split(':')[1]))
print(total_duration)
# A.R. Rahman - Mehendi Hai Rachnewali Best Video_Zubeidaa_Karisma Kapoor_Alka Yagnik-ZTpxYgX6RPU
