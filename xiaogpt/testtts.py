import asyncio
import io
import os
import edge_tts

async def run(tts_lang):
    
    communicate = edge_tts.Communicate("""Sure. Here are two sentences in English: "Artificial Intelligence is revolutionizing the world. It helps in making our work easier and more efficient." 你好，我是小爱同学。GLPE是环保与增长的绿色政策（Green Long-term Policy for Environment，简称GLPE）的缩写。""", tts_lang)
    duration = 0
    stream = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            stream.write(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            duration = (chunk["offset"] + chunk["duration"]) / 1e7
    if duration == 0:
        raise RuntimeError(f"Failed to get tts from edge with voice={tts_lang}")
    stream.seek(0)

    with open("temp.mp3", "wb") as f:
        f.write(stream.getbuffer())

    # 使用 aplay 播放音频
    os.system("afplay temp.mp3")

if __name__ == "__main__":
    for lang in [
        "zh-CN-YunxiNeural", # 3
        "zh-CN-YunjianNeural", # 4
        "zh-CN-XiaoyiNeural", # 4
        "zh-CN-YunxiaNeural", # 2
        "zh-CN-shaanxi-XiaoniNeural", # haha
        "zh-TW-HsiaoChenNeural",
        "zh-TW-YunJheNeural",
        "zh-TW-HsiaoYuNeural",

        "zh-CN-YunyangNeural",
        "zh-CN-XiaochenNeural",
        "zh-CN-XiaohanNeural",
        "zh-CN-XiaomengNeural",
        "zh-CN-XiaomoNeural",
        "zh-CN-XiaoqiuNeural",
        "zh-CN-XiaoruiNeural",
        "zh-CN-XiaoshuangNeural",
        "zh-CN-XiaoxuanNeural",
        "zh-CN-XiaoyanNeural",
        "zh-CN-XiaoyouNeural",
        "zh-CN-XiaozhenNeural",
        "zh-CN-YunfengNeural",
        "zh-CN-YunhaoNeural",

        "zh-CN-YunyeNeural",
        "zh-CN-YunzeNeural",
    ]: 
        print(lang)
        try:
            asyncio.run(run(lang)) 
        except Exception as e:
            print(lang,"error:",e)