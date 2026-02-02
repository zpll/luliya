from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import requests
import json

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("xm查询")
    async def xmsearch(self, event: AstrMessageEvent):
        """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        null="null"
        false="false"
        true="true"
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        wupin= text.split(' ', 1)[1] if ' ' in text else ""
        url = 'https://api.x-metash.cn/h5/home/searchAppNew'
        headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer",
        "content-type": "application/json",
        "origin": "https://xmeta.x-metash.cn",
        "priority": "u=1, i",
        "referer": "https://xmeta.x-metash.cn/",
        "sec-ch-ua-mobile": "?1",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36"
        }

        data={
        "pageNum": 1,
        "pageSize": 10,
        "search": wupin,
        "isShowArchive": true
        }
        data = json.dumps(data, separators=(',', ':'))
        # 发送GET请求
        response = requests.post(url, headers=headers, data=data)
        data=response.text
        resultText=""
        for i, goods in enumerate(data['data']['goodsList'], 1):
            resultText=resultText+f"\n商品{i}: {goods.get('name')} | 平台: {goods.get('platformName')} | 价格: ¥{goods.get('price')}"

        
        #yield event.image_result("http://v9.img.360kuai.com/video/360_202_/t11508c75c8d3683d207fd5da5d.jpg?size=576x1024") # 发送 URL 图片，务必以 http 或 https 开头
        yield event.plain_result(f"{user_name},查询结果：\n {resultText}") # 发送一条纯文本消
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`


    @filter.command("helloworld")
    async def helloworld(self, event: AstrMessageEvent):
        """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        #yield event.image_result("http://v9.img.360kuai.com/video/360_202_/t11508c75c8d3683d207fd5da5d.jpg?size=576x1024") # 发送 URL 图片，务必以 http 或 https 开头
        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!!!!") # 发送一条纯文本消息
     # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("图片")
    async def photo(self, event: AstrMessageEvent):
        """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        yield event.image_result("http://v9.img.360kuai.com/video/360_202_/t11508c75c8d3683d207fd5da5d.jpg?size=576x1024") # 发送 URL 图片，务必以 http 或 https 开头
        # yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!!!!!!!") # 发送一条纯文本消息
    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
    
