import datetime

def _gen_fixture_data():
    styles = ['빈티지', '아웃도어', '재생건축']
    targets = ['가족여행', '로컬투어', '커플여행']
    amenities = ['명상', '스파', '쾌적한 정원']
    tourspots = ['cafe', 'restaurant', 'shopping']
    features = ['barbeque', 'breakfast', 'open_air_bath']
    image_urls = ['https://www.stayfolio.com/system/pictures/images/000/037/809/large/e057b2c932688b16dae7849024afeb3b757954fe.jpg?1567645869',
                  'https://www.stayfolio.com/system/pictures/images/000/037/810/large/dbc9d352232cd5e0d78209ec6ec46cddd58a089c.jpg?1567645879',
                  'https://www.stayfolio.com/system/pictures/images/000/037/812/large/3d4dba0024f35aa94e6b271d3042abda0ba33d55.jpg?1567645899',
                  'https://www.stayfolio.com/system/pictures/images/000/037/811/large/e2da16aa4409eaa82c8946eaeb90379a8a6cb70a.jpg?1567645897',
                  'https://www.stayfolio.com/system/pictures/images/000/037/819/large/a834ceddd6050518c62e7485d989b22b92722fc8.jpg?1567646056',
                  'https://www.stayfolio.com/system/pictures/images/000/037/817/large/222222cc193b0ca261b6a6bd9e7328c9b6b171b0.jpg?1567646035',
                  'https://www.stayfolio.com/system/pictures/images/000/037/818/large/72ac6e50fa89b5d4a486baf967fbb57ee5da9ded.jpg?1567646054',
                  'https://www.stayfolio.com/system/pictures/images/000/037/821/large/a31f4cf2bf6218b02766f4db67ef31a6e5261d32.jpg?1567646079',
                  'https://www.stayfolio.com/system/pictures/images/000/037/822/large/3b471abfb4fcf44fdd5306b1ce6297019fdb87a5.jpg?1567646081',
                  'https://www.stayfolio.com/system/pictures/images/000/037/823/large/705be3e616a447ae9cafbdc8874cc3de456df37b.jpg?1567646083',
                  'https://www.stayfolio.com/system/pictures/images/000/037/824/large/6ede388a23f375dfdfbb6253ee67d4c0bc38a5a0.jpg?1567646084',
                  'https://www.stayfolio.com/system/pictures/images/000/037/836/large/70520b9d2077c64521b3a6826be9e4872cd4b872.jpg?1567646369',
                  'https://www.stayfolio.com/system/pictures/images/000/037/825/large/2e24c0d5139ceca39e844a20318fd4f1f88af2f7.jpg?1567646109',
                  'https://www.stayfolio.com/system/pictures/images/000/037/826/large/4f17794e5699b2823aefc514e3fba4ca4daa4080.jpg?1567646110',
                  'https://www.stayfolio.com/system/pictures/images/000/037/827/large/ad79ab6eb6bc9e826878469198c3faeb4b35524a.jpg?1567646112',
                  'https://www.stayfolio.com/system/pictures/images/000/037/828/large/17611eb291d732789947144444430ff5d7801cb0.jpg?1567646113',
                  'https://www.stayfolio.com/system/pictures/images/000/037/829/large/5a6cbab932e1a60d25768d3c204395f97b60d85f.jpg?1567646115',
                  'https://www.stayfolio.com/system/pictures/images/000/037/835/large/9ffe45e4c0ca31950e6b61f6412462508679db5a.jpg?1567646210',
                  'https://www.stayfolio.com/system/pictures/images/000/037/831/large/46e0c63eb4355a1e89079efe09b98c2dfc498f77.jpg?1567646164',
                  'https://www.stayfolio.com/system/pictures/images/000/037/832/large/d80345649f931a3e5b95a054b23429235b15fdfa.jpg?1567646165',
                  'https://www.stayfolio.com/system/pictures/images/000/037/833/large/b6ab3941585710dc6eadd0243432ed5b055e1b46.jpg?1567646166',
                  ]
    identifier = 'dolchae'
    title = '잠시 쉬어가도 좋은 우도의 하루'
    subtitle = '더욱 특별한 제주 여행이 필요하다면'
    description = '''제주를 바라보는 섬, 성산에서 배를 타고 바다를 느끼면 이내 닿는 곳 우도에 돌집 스테이, 돌채가 문을 열었다.제주의 돌집이 주는 묵직하고 차분한 여운과 고요한 우도의 밤을 경험할 수 있는 돌채는 특별히 무엇을 하지 않아도 평온한 휴식의 시간을, 일상에서 수고로움으로 지친 마음에 작은 위로를 건네준다.이 공간을 만든 호스트는 제주 여행 속 진짜 제주를 만날 수 있는 우도에서 오랜 시간 자연스럽게 뿌리내릴 공간을 만들고 싶었다. 돌채의 공간은 가족이 머물기 좋은 ROOM A와, 2인 객실 ROOM B로 구성된다. A룸은 거실과 주방, 침실로 나뉘며 대형 사이즈의 욕조 및 사우나 시설이 갖추어져 있다. 객실 안에는 안마 의자와 스타일러 등을 구비해 여행의 편의를 높였다. B동은 주방과 침실, 대형 사이즈의 욕조의 공간 구성이다. 두 객실 모두 돌담으로 둘러 쌓인 정원, 야외에서 즐길 수 있는 바베큐장을 함께 이용할 수 있다. 머무는 이들을 위해 돌채에서는 매일 아침 전복죽 조식 서비스와, 픽업을 제공한다. 반나절 머무는 여행지가 호스트가 추천해주는 가이드를 따라 아닌 돌채에서 머무르며 느껴보는 우도는 또 다른 매력의 제주를 느껴볼 수 있는 기회가 될 것이다. 우도의 풍경이 곳곳이 품고 있는 특별한 이야기, 마을 깊숙이 들어와야 보이는 진짜 우도를 돌채를 통해 경험해보자. Designed by 돌채 Photo by WEBMATE'''
    main_image_url = 'https://www.stayfolio.com/system/pictures/images/000/037/808/medium/f7f3462c036b6604769b916de6309c7082244205.jpg?1567645828'

    data = {
        'place':
           {
               'name': '돌채',
               'full_address': '제주특별자치도 제주시 우도면 우목길 60-3',
               'zipcode': '63365',
               'street': '60-3',
               'county': '제주시 우도면 우목길',
               'city': '제주시',
               'province': '제주도',
               'country': '한국',
               'longitude': '126.949035',
               'latitude': '33.508973',
               'website': 'bit.ly/2m0TwWo',
               'facebook': 'dolchae',
               'instagram': 'dolchae',
               'phone': '0504-0904-2346',
               'price_min': 150000.0,
               'price_max': 300000.0,
               'persons_min': 1,
               'persons_max': 5,
               'room_capacity': 2,
               'check_in': '16:00',
               'check_out': '11:00',
               'place_type': '렌탈하우스',
           },
        'place_tag':
        {
               'styles': styles,
               'targets': targets,
               'amenities': amenities,
               'tourspots': tourspots,
               'features': features,
           },
        'pick':
        {
               'identifier': identifier,
               'title': title,
               'subtitle': subtitle,
               'description': description,
               'main_image_url': main_image_url,
           },
        'image_urls': image_urls,
    }

    return data

def get_today():
    return datetime.date.today()
