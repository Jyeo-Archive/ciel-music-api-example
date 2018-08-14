# Using Ciel Music API

본 문서는 [시엘 뮤직(Ciel Music)](https://music.cieldev.com/)의 API, `getyoutube`, `getchart`와 이를 사용한 간단한 예시 코드에 대해서 설명한다.


## Search

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

#### Query

```
https://music.cieldev.com/api/search?query=연애
```

#### Result

```JSON
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

## Getyoutube

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

#### Query

```
https://music.cieldev.com/api/getyoutube/花요일/EXO-CBX
```

#### Result

```JSON
{
  "id":"WPAOpBstaYk",
  "title":"EXO-CBX (첸백시) - Blooming Day (花요일) (Color Coded Lyrics) [HAN\/ROM\/ENG]",
  "thumbnail":"https:\/\/i.ytimg.com\/vi\/WPAOpBstaYk\/default.jpg",
  "artist":"EXO-CBX"
}
```

## Getchart

차트 데이터 가져오기

```
https://bot.cielsoft.me/raw/(개수)/(차트)
```

멜론, 벅스, 네이버, 엠넷, 지니의 음원차트 데이터를 파싱해 JSON 형식으로 가져온다.

위 링크의 `(개수)` 자리에 표시될 상위 차트 데이터의 수를 입력하고, `(차트)` 자리에 데이터를 가져올 차트의 이름을 넣고 GET 요청을 보내면 된다.

| 식별자 | 차트 |
| :------------- | :------------- |
| `melon` | 멜론 |
| `bugs` | 벅스 |
| `naver` | 네이버 뮤직 |
| `mnet` | 엠넷 |
| `genie` | 지니 |

| 필드명 | 설명 |
| :------------- | :------------- |
| `thumbnail` | 앨범 썸네일 |
| `title` | 동영상 제목 |
| `artist` | 아티스트 |

### Melon-Example-Query

```
https://bot.cielsoft.me/raw/3/melon
```

#### Result

```JSON
[
  {
    "thumbnail" : "https://cdnimg.melon.co.kr/cm/album/images/101/91/694/10191694_500.jpg/melon/resize/120/quality/80/optimize", 
    "artist": "Red Velvet (레드벨벳)", 
    "title": "Power Up"
  }, 
  {
    "thumbnail": "https://cdnimg.melon.co.kr/cm/album/images/101/79/508/10179508_500.jpg/melon/resize/120/quality/80/optimize", 
    "artist": "숀 (SHAUN)", 
    "title": "Way Back Home"
  }, 
  {
    "thumbnail": "https://cdnimg.melon.co.kr/cm/album/images/101/83/127/10183127_500.jpg/melon/resize/120/quality/80/optimize", 
    "artist": "TWICE (트와이스)", 
    "title": "Dance The Night Away"
  }
]
```

### Bugs-Example-Query

```
https://bot.cielsoft.me/raw/3/bugs
```

#### Result

```JSON
[
  {
    "thumbnail": "https://image.bugsm.co.kr/album/images/50/201865/20186568.jpg?version=20180814180106",
    "artist": "(여자)아이들", 
    "title": "한 (一)"
  }, 
  {
    "thumbnail": "https://image.bugsm.co.kr/album/images/50/201847/20184771.jpg?version=20180807002840", 
    "artist": "Red Velvet (레드벨벳)", 
    "title": "Power Up"
  }, 
  {
    "thumbnail": "https://image.bugsm.co.kr/album/images/50/7573/757375.jpg?version=20180628180004", 
    "artist": "숀(SHAUN)", 
    "title": "Way Back Home"
  }
]
```

### Naver-Example-Query

```
https://bot.cielsoft.me/raw/3/naver
```

#### Result

```JSON
[
  {
    "thumbnail": "https://musicmeta-phinf.pstatic.net/album/002/472/2472826.jpg?type=r32Fll&v=20180724120801", 
    "artist": "숀 (SHAUN)", 
    "title": "Way Back Home "
  }, 
  {
    "thumbnail": "https://musicmeta-phinf.pstatic.net/album/002/495/2495239.jpg?type=r32Fll&v=20180806175905", 
    "artist": "Red Velvet (레드벨벳)", 
    "title": "Power Up "
  }, 
  {
    "thumbnail": "https://musicmeta-phinf.pstatic.net/album/002/480/2480898.jpg?type=r32Fll&v=20180717160329", 
    "artist": "TWICE(트와이스)", 
    "title": "Dance The Night Away "
  }
]
```

### Mnet-Example-Query

```
https://bot.cielsoft.me/raw/3/mnet
```

#### Result

```JSON
[
  {
    "thumbnail": "https://cmsimg.mnet.com/clipimage/album/50/003/141/3141195.jpg", 
    "artist": "Red Velvet (레드벨벳)", 
    "title": "Power Up"
  }, 
  {
    "thumbnail": "https://cmsimg.mnet.com/clipimage/album/50/003/069/3069077.jpg", 
    "artist": "숀(SHAUN)", 
    "title": "Way Back Home"
  }, 
  {
    "thumbnail": "https://cmsimg.mnet.com/clipimage/album/50/003/140/3140324.jpg", 
    "artist": "iKON", 
    "title": "죽겠다 (KILLING ME)"
  }
]
```

### Genie-Example-Query

```
https://bot.cielsoft.me/raw/3/genie
```

#### Result

```JSON
[
  {
    "thumbnail": "https://image.genie.co.kr/Y/IMAGE/IMG_ALBUM/081/091/693/81091693_1533539947065_1_140x140.JPG", 
    "artist": "Red Velvet (레드벨벳)", 
    "title": "Power Up"
  }, 
  {
    "thumbnail": "https://image.genie.co.kr/Y/IMAGE/IMG_ALBUM/081/078/885/81078885_1530075209642_1_140x140.JPG", 
    "artist": "숀 (SHAUN)", 
    "title": "Way Back Home"
  }, 
  {
    "thumbnail": "https://image.genie.co.kr/Y/IMAGE/IMG_ALBUM/081/074/005/81074005_1529044460289_1_140x140.JPG", 
    "artist": "BLACKPINK", 
    "title": "뚜두뚜두 (DDU-DU DDU-DU)"
  }
]
```

# Example Usage

PR을 통해서 새로운 예제를 추가해 주세요.

Add your own examples via Pull Requests.

- [Example with cURL](./example-curl.sh)
- [Example with Python2/Python3](./example-python.py)
