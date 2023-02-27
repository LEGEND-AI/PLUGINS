from telethon import functions
from telethon.errors import ChatAdminRequiredError, UserAlreadyInvitedError
from telethon.tl.types import Channel, Chat, User

from .. import legend
from ..core.managers import eod, eor
from ..helpers.utils import mentionuser

menu_category = "extra"

async def chat_vc_checker(event, chat, edits=True):
    if isinstance(chat, User):
        await eod(event, "Voice Chats are not available in Private Chats")
        return None
    result = await get_group_call(chat)
    if not result:
        if edits:
            await eod(event, "No Group Call in this chat")
        return None
    return result

@legend.legend_cmd(
    pattern="vcstart",
    command=("vcstart", menu_category),
    info={
        "header": "To end a stream on Voice Chat.",
        "description": "To end a stream on Voice Chat",
        "usage": "{tr}vcstart",
        "examples": "{tr}vcstart",
    },
)
async def start_vc(event):
    "To start a Voice Chat."
    vc_chat = await legend.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat, False)
    if gc_call:
        return await eod(event, "Group Call is already available in this chat")
    try:
        await legend(
            functions.phone.CreateGroupCallRequest(
                peer=vc_chat,
                title="LegendBot VC",
            )
        )
        await eod(event, "Started Group Call")
    except ChatAdminRequiredError:
        await eod(event, "You should be chat admin to start vc", time=20)

