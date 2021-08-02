
import os
import asyncio
from ppgan.apps import Photo2CartoonPredictor#人像动漫化
from PIL import Image
from ppgan.apps import AnimeGANPredictor#场景动漫化
from stylenew import envirstyle#场景模拟
# predictor = AnimeGANPredictor()
# predictor.run(PATH_OF_IMAGE)
# p2c = Photo2CartoonPredictor(output_path='../output')
# p2c.run('../samples/plain.jpg')

from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)
robot_state = 0 #机器人状态
style = ''#待模拟风格

def Stitching_images(input_path:str):
    """
    input_path:输入图像地址
    return:覆盖生成图像
    本函数将完成生成图像与护照的拼接
    """
    save_img = input_path
    M_Img = Image.open('./output/huzhao.png')
    S_Img = Image.open(input_path)
    coordinate=(21,64)
    M_Img.paste(S_Img, coordinate, mask=None)
    M_Img.save(save_img)

async def on_message(msg: Message):
    talker = msg.talker()
    global robot_state
    global style
    # robot_state = 0
    if msg.text() == 'ding':
        await msg.say('这是自动回复: dong dong dong')
    if msg.text() == 'hi' or msg.text() == '你好' or msg.text()=='救救我' or msg.text()=='请求帮助':
        await talker.say('Dont Painc，这里是星际旅行向导小天，虽然星际旅行危机四伏，千变万化。\n但在这里我将帮助你完成星际旅航\n对我回复：“我在哪？”即可以获得附近星球坐标。')
    if msg.text() == '我在哪'or msg.text() == '我在哪？':
        await talker.say('你目前处于大麦哲伦星系左悬臂附近，以目前飞船能量周围可去行星有：平面行星，海洋行星，电子行星，星云行星以及艺术行星')
        await talker.say('你可以发送‘获取+行星名字+详细信息’来获取相关行星的详细信息\n例如‘获取海洋行星详细信息’')
    if msg.text() == '再见':
        await talker.say('很高兴为您服务，祝您星际旅途愉快！')
    if msg.text() == '获取海洋行星详细信息':
        # 海洋行星具体介绍
        await talker.say('海洋行星为距离飞船3AU的液态水行星，该星球由百分之99的水构成，为地球初代海洋样貌。\n\n经大麦哲伦星际旅行局报告显示，该星球不适宜生存，也尚未发现明显的生物存在痕迹')
        await talker.say('因飞船瞭望镜受损无法观察行星真实全貌，您可以发送“模拟海洋行星”并给出一张照片，旅行向导将模拟出照片环境在海洋行星的景象。')
    if msg.text() == '获取电子行星详细信息':
        # 电子行星具体介绍
        await talker.say('电子行星为距离飞船1AU的岩石行星，该行星本来为一颗岩石行星，因为大麦哲伦星系的电子产品垃圾均往该行星倾倒，目前该行星已经通体为电子绿色\n\n经大麦哲伦星际旅行局报告显示，该星球不适宜生存')
        await talker.say('因飞船瞭望镜受损无法观察行星真实全貌，您可以发送“模拟电子行星”并给出一张照片，旅行向导将模拟出照片环境在电子行星的景象。')
    if msg.text() == '获取星云行星详细信息':
        # 星云行星具体介绍
        await talker.say('星云行星为距离飞船4AU的气态行星，该行星属于星云附近粒子相互作用而出现的产物，整颗行星由90%的氢气和10%的氮气构成\n\n经大麦哲伦星际旅行局报告显示，该星球不适宜生存，也尚未发现明显的生物存在痕迹')
        await talker.say('因飞船瞭望镜受损无法观察行星真实全貌，您可以发送“模拟星云行星”并给出一张照片，旅行向导将模拟出照片环境在星云行星的景象。')
    if msg.text() == '获取艺术行星详细信息':
        # 扭曲行星具体介绍
        await talker.say('艺术行星为距离飞船18AU的固态行星，该行星为大麦哲伦造星俱乐部所创造的产物，某位宇宙金主为纪念其喜欢的艺术家而花重金打造而成，该行星风貌通体扭曲但却呈现了一种别样的美丽。\n\n经大麦哲伦星际旅行局报告显示，此为观赏行星，不适于生存。')
        await talker.say('因飞船瞭望镜受损无法观察行星真实全貌，您可以发送“模拟艺术行星”并给出一张照片，旅行向导将模拟出照片环境在艺术行星的景象。')
    if msg.text() == '获取平面行星详细信息':
        # 平面行星具体介绍
        await talker.say('平面行星为距离飞船1AU的固态行星，该行星为飞船附近唯一可居住行星，该行星本为一颗宜居岩石行星，但该行星一名画家为了其狂热的梦想制造了二向粒子，导致其行星变为二维平面，凡是进入该星球的人或飞船皆会被二向化。')
        await talker.say('因飞船瞭望镜受损无法观察行星真实全貌，您可以发送“模拟平面行星”并给出一张照片，旅行向导将模拟出照片环境在平面行星的景象。')
        await talker.say('如有意向登陆平面行星，请发送‘制作平面行星护照’并给出一张证件照，旅行向导将为你制作登陆平面行星所需的护照！')
    if msg.text() == '制作平面行星护照':
        robot_state = 1
        await talker.say('已收取到制作平面行星护照请求，请发送证件照！')
    if msg.text() == '模拟海洋行星':
        robot_state = 2
        await talker.say('已收到模拟海洋行星环境请求，请发送待模拟的环境图片！')
    if msg.text() == '模拟电子行星':
        robot_state = 3
        await talker.say('已收到模拟电子行星环境请求，请发送待模拟的环境图片！')
    if msg.text() == '模拟星云行星':
        robot_state = 4
        await talker.say('已收到模拟星云行星环境请求，请发送待模拟的环境图片！')
    if msg.text() == '模拟艺术行星':
        robot_state = 5
        await talker.say('已收到模拟艺术行星环境请求，请发送待模拟的环境图片！')
    if msg.text() == '模拟平面行星':
        robot_state = 6
        await talker.say('已收到模拟平面行星环境请求，请发送待模拟的环境图片！')
    if robot_state == 1 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  制作平面星球护照
        await talker.say('已收到证件照，开始制作中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        # await msg.say('已收到证件照，开始制作中。。。。。。')
        
        p2c = Photo2CartoonPredictor(output_path='./output')
        p2c.run('./'+img_path)
        print("生成成功！")
        Stitching_images('./output/p2c_cartoon.png')#制作护照图像
        file_box_final_result = FileBox.from_file('./output/p2c_cartoon.png')
        robot_state = 0
        await talker.say('制作完成，请携带护照入境。')
        await msg.say(file_box_final_result)
    if robot_state == 2 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  模拟海洋行星景象
        await talker.say('已收到图像，开始模拟中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './envimage/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)

        style = 'ocean'#模拟海洋行星

        envirstyle(img_path,style)

        file_box_final_result = FileBox.from_file('./output_dir/LapStyle/stylized.png')
        robot_state = 0
        await talker.say('模拟完成!')
        await msg.say(file_box_final_result)
    if robot_state == 3 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  模拟电子行星景象
        await talker.say('已收到图像，开始模拟中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './envimage/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)

        style = 'circuit'#模拟电子行星

        envirstyle(img_path,style)

        file_box_final_result = FileBox.from_file('./output_dir/LapStyle/stylized.png')
        robot_state = 0
        await talker.say('模拟完成!')
        await msg.say(file_box_final_result)
    if robot_state == 4 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  模拟星云行星景象
        await talker.say('已收到图像，开始模拟中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './envimage/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)

        style = 'stars'#模拟星云行星

        envirstyle(img_path,style)

        file_box_final_result = FileBox.from_file('./output_dir/LapStyle/stylized.png')
        robot_state = 0
        await talker.say('模拟完成!')
        await msg.say(file_box_final_result)
    if robot_state == 5 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
            #  模拟扭曲行星景象
            await talker.say('已收到图像，开始模拟中')
            # 将Message转换为FileBox
            file_box_user_image = await msg.to_file_box()
        
            # 获取图片名
            img_name = file_box_user_image.name
        
            # 图片保存的路径
            img_path = './envimage/' + img_name
        
            # 将图片保存为本地文件
            await file_box_user_image.to_file(file_path=img_path)

            style = 'starrynew'#模拟扭曲行星

            envirstyle(img_path,style)

            file_box_final_result = FileBox.from_file('./output_dir/LapStyle/stylized.png')
            robot_state = 0
            await talker.say('模拟完成!')
            await msg.say(file_box_final_result)
    if robot_state == 6 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
            #  模拟平面行星景象
            await talker.say('已收到图像，开始模拟中')
            # 将Message转换为FileBox
            file_box_user_image = await msg.to_file_box()
        
            # 获取图片名
            img_name = file_box_user_image.name
        
            # 图片保存的路径
            img_path = './envimage/' + img_name
        
            # 将图片保存为本地文件
            await file_box_user_image.to_file(file_path=img_path)
            predictor = AnimeGANPredictor()
            predictor.run(img_path)
            file_box_final_result = FileBox.from_file('./output/anime.png')
            robot_state = 0
            await talker.say('模拟完成!')
            await msg.say(file_box_final_result)
            
    

async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    print(user)


async def main():
    # 确保我们在环境变量中设置了WECHATY_PUPPET_SERVICE_TOKEN
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan',      on_scan)
    bot.on('login',     on_login)
    bot.on('message',   on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())