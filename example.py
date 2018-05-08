import urllib.request
import urllib.parse
import json
import datetime
import sys
# from flask import Flask, render_template

# app = Flask(__name__)
# # global playlist
# # playlist = get_playlist()

# @app.route('/')
# def main():
#     url = 'https://music.cieldev.com/api/getchart/melon'
#     # print(url)
#     u = urllib.request.urlopen(url)
#     data = u.read()
#     # print(data)
#     j = json.loads(data)
#     title = j[0]['title'] # 제목 
#     artist = j[0]['artist'] # 아티스트명 
#     thumbnail = j[0]['thumbnail'] # 앨범 링크 
#     # 멜론차트 1등 음악을 가져옴

#     title = urllib.parse.quote(title)
#     artist = urllib.parse.quote(artist)
#     url = 'https://music.cieldev.com/api/getyoutube/' + title + '/' + artist
#     # print(url)
#     u = urllib.request.urlopen(url)
#     data = u.read()
#     # print(data)
#     j = json.loads(data)
#     id = j["id"] # 유튜브 ID

#     return render_template(
#         'index.html',
#         id = id,
#         thumbnail = thumbnail,
#         title = title,
#         artist = artist
#     )

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', debug=True, port=8120)
#     # http://localhost:8120/ # 8120 => 나무위키에 시엘 뮤직 항목이 만들어진 날(Easter Egg)

url = 'https://music.cieldev.com/api/getchart/melon'
# print(url)
u = urllib.request.urlopen(url)
data = u.read()
# print(data)
j = json.loads(data)
title = j[0]['title'] # 제목 
artist = j[0]['artist'] # 아티스트명 
thumbnail = j[0]['thumbnail'] # 앨범 링크 
# 멜론차트 1등 음악을 가져옴

title = urllib.parse.quote(title)
artist = urllib.parse.quote(artist)
url = 'https://music.cieldev.com/api/getyoutube/' + title + '/' + artist
# print(url)
u = urllib.request.urlopen(url)
data = u.read()
# print(data)
j = json.loads(data)
id = j["id"] # 유튜브 ID

sys.stdout.write('[id] : ')
sys.stdout.write(id)
sys.stdout.write('\n[title] : ')
sys.stdout.write(title)
sys.stdout.write('\n[artist] : ')
sys.stdout.write(artist)
sys.stdout.write('\n[thumbnail image URL] : ')
sys.stdout.write(thumbnail)