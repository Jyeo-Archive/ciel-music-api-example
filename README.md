# Using Ciel Music API
본 문서는 [시엘 뮤직(Ciel Music)](https://music.cieldev.com/)의 API, `getyoutube`, `getchart`와 이를 사용한 간단한 예시 코드에 대해서 설명한다.


## search
검색어로 노래 제목, 아티스트, Ciel Music Verified 여부를 가져옵니다
```
https://music.cieldev.com/api/search
```
GET 파라미터 `query` 에 검색어를 입력하면 json 타입으로 반환됩니다

| 필드명 | 설명 |
| :------------- | :------------- |
| `name` | 노래 제목 |
| `artist` | 아티스트 |
| `verified` | 검증된 노래 여부 (true), 없으면 verified 값 자체가 없음 |


- `'`, `&`, `*`은 disallowed character로 취급되므로 URL에 포함되어서는 안된다.


### Example

#### query
```
https://music.cieldev.com/api/search?query=연애
```

#### result
```
[
  {
    "name":"연애재판 (恋愛裁判)",
    "artist":"Raon Lee (이라온)",
    "verified":true
  },
  {
    "name":"바케모노가타리 (Bakemonogatari) - 연애 서큘레이션",
    "artist":"휴복 (HUBOG)",
    "verified":true
  },
  {
    "name":"을의 연애 (with 박주원)",
    "artist":"IU",
    "thumbnail":"https:\/\/lastfm-img2.akamaized.net\/i\/u\/300x300\/d6fcaab20cf4ba07d5d00cef3ad96433.png"
  }, 
  ...
]
```

## getyoutube
제목과 아티스트명으로 검색해서 Youtube ID 가져오기 
```
https://music.cieldev.com/api/getyoutube/(제목)/(아티스트)
```
위 링크의 `(제목)`과 `(아티스트)`에 해당하는 곳에 검색할 곡의 제목과 아티스트명을 넣어주면 검색 결과가 JSON 형식으로 반환된다.

| 필드명 | 설명 |
| :------------- | :------------- |
| `id` | Youtube ID |
| `title` | 동영상 제목 |
| `thumbnail` | 동영상 썸네일 |
| `artist` | 아티스트 |

- `'`, `&`, `*`은 disallowed character로 취급되므로 URL에 포함되어서는 안된다.

- 가끔 `title`과 `artist` 필드가 unicode로 encoding되서 나오기도 한다.

- `(제목)`과 `(아티스트)` 모두 입력해야 한다.

### Example

#### query
```
https://music.cieldev.com/api/getyoutube/花요일/EXO-CBX
```

#### result
```
{
  "id":"WPAOpBstaYk",
  "title":"EXO-CBX (첸백시) - Blooming Day (花요일) (Color Coded Lyrics) [HAN\/ROM\/ENG]",
  "thumbnail":"https:\/\/i.ytimg.com\/vi\/WPAOpBstaYk\/default.jpg",
  "artist":"EXO-CBX"
}
```

## getchart
```
https://music.cieldev.com/api/getchart/melon
```
```
https://music.cieldev.com/api/getchart/bugs
```
```
https://music.cieldev.com/api/getchart/naver
```
```
https://music.cieldev.com/api/getchart/mnet
```
```
https://music.cieldev.com/api/getchart/genie
```
멜론, 벅스, 네이버, 엠넷, 지니의 음원차트 데이터를 파싱해 JSON 형식으로 가져온다.

| 필드명 | 설명 |
| :------------- | :------------- |
| `thumbnail` | 앨범 썸네일 |
| `title` | 동영상 제목 |
| `artist` | 아티스트 |

### Example

#### query
```
https://music.cieldev.com/api/getchart/genie
```

#### result
```
[
  {
    "thumbnail":"//image.genie.co.kr/Y/IMAGE/IMG_ALBUM/081/056/930/81056930_1524214278122_1_140x140.JPG",
    "title":" 주지마",
    "artist":"로꼬 & 화사 (마마무)"
  },
  {
    "thumbnail":"//image.genie.co.kr/Y/IMAGE/IMG_ALBUM/081/059/187/81059187_1525072803622_1_140x140.JPG",
    "title":" 밤 (Time for the moon night)",
    "artist":"여자친구 (GFRIEND)"
  },
  {
    "thumbnail":"//image.genie.co.kr/Y/IMAGE/IMG_ALBUM/080/997/959/80997959_1509347822288_1_140x140.JPG",
    "title":" 지나오다",
    "artist":"닐로 (Nilo)"
  },
  ...
  {
    "thumbnail":"//image.genie.co.kr/Y/IMAGE/IMG_ALBUM/081/053/641/81053641_1523613436076_1_140x140.JPG",
    "title":" 이로한 (Feat. ELO & Jessi ) (Prod. by Padi)",
    "artist":"이로한 (WEBSTER B)"
  }
]
```

# Python Example
`example.py`에서는 멜론차트 1위 음악의 Youtube ID와 앨범 썸네일, 제목과 아티스트명을 가져와 출력한다.<br>
이를 사용해서 Python Flask를 이용해서 HTML template에 값을 전달한다던가 하는 것이 가능할 것이다(만들다가 현타와서 주석처리했다).<br>
`getchart`를 사용해서 1위 음악 정보를 가져온 뒤 이를 이용해서 `getyoutube`로 Youtube ID를 얻는 방식이다.
```
PS C:\Users\JunhoYeo\Desktop\ciel music api> python .\example.py
[id] : LS74a_bbOgE
[title] : 주지마
[artist] : 로꼬
[thumbnail image URL] : https://cdnimg.melon.co.kr/cm/album/images/101/60/487/10160487_500.jpg/melon/resize/120/quality/80/optimize
```
