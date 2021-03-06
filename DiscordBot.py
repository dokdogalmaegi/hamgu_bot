import asyncio
import discord
import bot2

res = bot2.DiscordChatBot()

app = discord.Client()
# discord.Client()를 그대로 쓰게 되면 계속 쓸때 귀찮아지기 떄문에 app으로 넘깁니다. discord.Client() 객체를 받아오는 작업입니다.

# 기본 도움말(Embed)
embed = discord.Embed(title="이 봇은 햄구봇입니다", description="이 봇은 햄구봇입니다. 우리의 햄구봇의 명령어는\n```!나무위키(!namu) 검색어 : 나무위키 검색\n!지식인(!sik) 검색어 : 네이버 지식인 검색\n!유튜브(!you) 검색어 : 유튜브 검색\n!번역(!t) lang(언어) 문장 : 한국어를 원하는 언어로 번역을 합니다.\n강현구 : 햄구햄구\n!help : 도움말\n!help 2 : 번역 도움말```\n이 있습니다.", color=0x00f000)

# 번역 도움말 (Translate_embed)
translate_embed = discord.Embed(title="이 봇은 햄구봇입니다.", description="이 봇은 햄구봇입니다. 우리의 햄구봇이 번역할 수 있는 언어는\n```kr(01) - 한국어\nen(02) - 영어\njp(03) - 일본어\ncn(04) - 중국어\nvi(05) - 베트남어\nid(06) - 인도네시아어\nar(07) - 아랍어\nbn(08) - 뱅갈어\nde(09) - 독일어\nes(10) - 스페인어\nfr(11) - 프랑스어\nhi(12) - 힌디어\nit(13) - 이탈리아어\nms(14) - 말레이시아어\nnl(15) - 네덜란드어\npt(16) - 포르투갈어\nru(17) - 러시아어\nth(18) - 태국어\ntr(19) - 터키어```\n을 지원합니다", color=0x00f000)

# 이스터 에그(Easter egg)
ham_tutorial = discord.Embed(title='이 봇은 햄구봇입니다.', description='이 봇은 햄구봇입니다.')
ham_tutorial.set_image(url="https://avatars0.githubusercontent.com/u/25629441?s=460&v=4")

# embed는 !help를 했을 때 가독성을 높이는 help문을 만들기 위해 사용됩니다.

token = "MyToken" # token = "MyToken"
# 디스코드 봇을 만들었을 때 발급되는 봇 token을 token에 넣어줍니다.

activity = discord.Game(name="안녕하세요! 반갑습니다 :D")
# 디스코드 봇의 활동으로 할 내용을 activity변수에 담습니다. Ex) ㅁㅁㅁ님이 ㅁㅁㅁ를(을) 하는중

# 이제부터는 봇이 구동되었을 때 실제로 구동되는 코드부분입니다.
@app.event
async def on_ready():
    # 봇이 플레이중인 게임을 실행할 수 있다. 아래의 "반갑습니다"를 수정하면 된다.
    await app.change_presence(status=discord.Status.idle, activity=activity)
    # 위에 activity로 설정해준것을 실제로 띄워줍니다.

# 봇이 새로운 메세지를 수신했을때 동작되는 코드입니다.
# res.namu_search(), res.naver_search(), res.youtube_serarch() 등 선언하지 않은 함수들은 밑에서 사용되는 함수들은 class bot2에서 가져와서 사용하는 함수들입니다.
@app.event
async def on_message(msg):
    if msg.author.bot: # 만약 메세지를 보낸사람이 봇일 경우에는
        return None # 동작하지 않고 무시한다.
    # 나무위키 명령어를 사용할 때 실행되는 코드
    if msg.content.startswith('!나무위키') or msg.content.startswith('!namu'):
        title = msg.content[6:]
        await msg.channel.send('당신의 키워드 `{}`에대한 나무위키 검색 결과입니다. \n{}'.format(title, res.namu_search(title))) 
    # 지식인 명령어를 사용할 때 실행되는 코드
    if msg.content.startswith('!지식인') or msg.content.startswith('!sik'):
        title = msg.content[5:]
        await msg.channel.send('당신의 키워드 `{}`에대한 네이버 지식인 검색 결과입니다 {}'.format(title, res.naver_search(title)))
    # 유튜브 명령어를 사용할 때 실행되는 코드
    if msg.content.startswith('!유튜브') or msg.content.startswith('!you'):
        title = msg.content[5:]
        await msg.channel.send('당신의 키워드 `{}`에대한 유튜브 검색 결과입니다. {}'.format(title, res.youtube_search(title).replace(" ", "%20")))
    # 이스터에그
    if msg.content == '강현구':
        await msg.channel.send('햄구햄구')
        await msg.channel.send(embed=ham_tutorial)
    # 도움말 명령어를 사용할 때 실행되는 코드
    if msg.content == '!help':
        await msg.channel.send(embed=embed)
    # 번역 도움말 명령어를 사용할 때 실행되는 코드
    if msg.content == '!help 2':
        await msg.channel.send(embed=translate_embed)
    # 번역 명령어를 사용할 때 실행되는 코드
    if msg.content.startswith('!번역'):
        text = msg.content.replace(" ", "")
        lang = text[3:5]
        text = text[5:]
        await msg.channel.send('{} -> {}'.format(text, res.kakao_translate(lang, text)))
    # 번역 명령어를 영어로 입력했을 때 실행되는 코드
    if msg.content.startswith('!t'):
        text = msg.content.replace(" ", "")
        lang = text[2:4]
        text = text[4:]
        await msg.channel.send('```{}``` ↓ ```{}```'.format(text, res.kakao_translate(lang, text)))
    if msg.content.startswith('!전적'):
        text = msg.content.replace(" ", "")
        title = text[3:]
        level,kda,rating,rank,img_url = res.Rsix(title)
        rainbow_embed = discord.Embed(title="{}의 전적입니다.".format(title), description="```레벨(level) : {}\n랭크 평균 KDA : {}\nMMR : {}\n랭크(Rank) : {}```\n # Most Operator".format(level, kda, rating, rank))
        rainbow_embed.set_image(url=img_url)
        await msg.channel.send(embed=rainbow_embed)

# 봇 가동
app.run(token)
