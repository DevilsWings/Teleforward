import telethon as te
from telethon import TelegramClient, events
from telethon.utils import get_display_name
api_id = <api_id>
api_hash = <api_hash>

client = te.TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage())
async def my_event_handler(event):
    await client.get_dialogs()
    sender = await event.get_sender()
    chatno = str(event.chat_id)
    print('Message Recieved')
    if (chatno[1::] == targetno):
        package = str("Chat recieved from target group \n sender: " + get_display_name(sender))
        print(event)
        await client.send_message(destno, package)
        await client.send_message(destno, event.message)

async def main():
    dialogs = await client.get_dialogs(20)
    print("Chat Id of your first 20 chats:")
    for dialog in dialogs:
        print(get_display_name(dialog.entity), dialog.entity.id)

client.start()
client.loop.run_until_complete(main())
targetno = input("Input your Desired Origin Chat ID: ")
destno = int(input("Input your desired Destination (input their corresponding Chat ID.): "))
client.run_until_disconnected()