import asyncio
from collections import deque

from Legendbot.plugins import eor, legend

menu_category = "fun"


@legend.legend_cmd(
    pattern="degi$",
    command=("degi", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}degi",
    },
)
async def degi(event):
    "animation command"
    event = await eor(event, "degi")
    await event.edit("WO")
    await asyncio.sleep(1.5)
    await event.edit("DegI")
    await asyncio.sleep(1.5)
    await event.edit("TuM")
    await asyncio.sleep(1.5)
    await event.edit("EkbaR")
    await asyncio.sleep(1.5)
    await event.edit("ManG")
    await asyncio.sleep(1.5)
    await event.edit("KaR")
    await asyncio.sleep(1.5)
    await event.edit("ToH")
    await asyncio.sleep(1.5)
    await event.edit("DekhO")
    await asyncio.sleep(1.5)
    await event.edit("Wo DeGi TuM eKbAr MaNg KaR tOh DeKhOπ")


@legend.legend_cmd(
    pattern="nehi$",
    command=("nehi", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nehi",
    },
)
async def nehi(event):
    "animation command"
    event = await eor(event, "nehi")
    await event.edit(
        "`Wo PaKkA DeGi Tu ManG KaR ToH DekH\n AuR NaA De To UskI BheN Ko PakaDππ`"
    )


@legend.legend_cmd(
    pattern="hnd$",
    command=("hnd", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}hnd <name>",
    },
)
async def hand(event):
    "animation command"
    name = event.text[4:]
    animation_interval = 0.5
    animation_ttl = range(6)
    event = await eor(event, "βοΈ")
    animation_chars = [
        "ππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏ                                          ππΏ\nππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏ",
        "ππΎππΎππΎππΎππΎππΎππΎππΎππΎ\nππΎ                                  ππΎ\nππΎ                                  ππΎ\nππΎ                                  ππΎ\nππΎ                                  ππΎ\nππΎ                                  ππΎ\nππΎ                                  ππΎ\nππΎ                                  ππΎ\nππΎππΎππΎππΎππΎππΎππΎππΎππΎ",
        "ππ½ππ½ππ½ππ½ππ½ππ½ππ½\nππ½                        ππ½\nππ½                        ππ½\nππ½                        ππ½\nππ½                        ππ½\nππ½                        ππ½\nππ½ππ½ππ½ππ½ππ½ππ½ππ½",
        "ππΌππΌππΌππΌππΌ\nππΌ              ππΌ\nππΌ              ππΌ\nππΌ              ππΌ\nππΌππΌππΌππΌππΌ",
        f"ππ»ππ»ππ»\n{name}\nππ»ππ»ππ»",
        f"ππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏ\nππΏππΎππΎππΎππΎππΎππΎππΎππΎππΎππΏ\nππΏππΎππ½ππ½ππ½ππ½ππ½ππ½ππ½ππΎππΏ\nππΏππΎππ½ππΌππΌππΌππΌππΌππ½ππΎππΏ\nππΏππΎππ½ππΌππ»ππ»ππ»ππΌππ½ππΎππΏ\nππΏ  {name}  ππΏ\nππΏππΎππ½ππΌππ»ππ»ππ»ππΌππ½ππΎππΏ\nππΏππΎππ½ππΌππΌππΌππΌππΌππ½ππΎππΏ\nππΏππΎππ½ππ½ππ½ππ½ππ½ππ½ππ½ππΎππΏ\nππΏππΎππΎππΎππΎππΎππΎππΎππΎππΎππΏ\nππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏππΏ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@legend.legend_cmd(
    pattern="think$",
    command=("think", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}think",
    },
)
async def think(event):
    "animation command"
    event = await eor(event, "think")
    deq = deque(list("π€π§π€π§π€π§"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="lmao$",
    command=("lmao", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}lmao",
    },
)
async def lmao(event):
    "animation command"
    event = await eor(event, "lmao")
    deq = deque(list("ππ€£ππ€£ππ€£"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="nothappy$",
    command=("nothappy", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nothappy",
    },
)
async def nothappy(event):
    "animation command"
    event = await eor(event, "nathappy")
    deq = deque(list("πβΉοΈπβΉοΈπβΉοΈπ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="clock$",
    command=("clock", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}clock",
    },
)
async def clock(event):
    "animation command"
    event = await eor(event, "clock")
    deq = deque(list("πππππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="muah$",
    command=("muah", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}muah",
    },
)
async def muah(event):
    "animation command"
    event = await eor(event, "muah")
    deq = deque(list("πππππ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="heart$",
    command=("heart", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}heart",
    },
)
async def heart(event):
    "animation command"
    event = await eor(event, "heart")
    deq = deque(list("β€οΈπ§‘πππππ€"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="gym$",
    command=("gym", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}gym",
    },
)
async def gym(event):
    "animation command"
    event = await eor(event, "gym")
    deq = deque(list("πβπβπ€Έβπβπβπ€Έβπβπβπ€Έβ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="earth$",
    command=("earth", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}earth",
    },
)
async def earth(event):
    "animation command"
    event = await eor(event, "earth")
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="moon$",
    command=("moon", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}moon",
    },
)
async def moon(event):
    "animation command"
    event = await eor(event, "moon")
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@legend.legend_cmd(
    pattern="smoon$",
    command=("smoon", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}smoon",
    },
)
async def smoon(event):
    "animation command"
    event = await eor(event, "smoon")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@legend.legend_cmd(
    pattern="tmoon$",
    command=("tmoon", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}tmoon",
    },
)
async def tmoon(event):
    "animation command"
    event = await eor(event, "tmoon")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
