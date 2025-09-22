# import time
# from datetime import datetime


# print(datetime.today())
# time.sleep(1)

# # ctrl + l    help to select full line



# class customer:
#     type = 'customer'

#     def __init__(self):
#         self.name = 'bilal'
#         self.mobile = 97838
#         self.address = 'jammu'

# test = customer()

# print(test.address)
# print(test.mobile)
# print(test.name)

# print(test.type)


# x = int (input("enter the values in the dictionary: "))
# my_dict = {}

# for i in range (x):
#         key = input(f"enter key {i+1}: ")
#         value = input(f"enter the value for {key}: ")
#         my_dict[key] = value

# print ("\niterate over dictionary: ")

# print("\nkey: ")
# for key in my_dict:
#         print(key)

# print ("\nvalue: ")
# for value in my_dict.values():
#         print(value)

# print("\n key-values")
# for key,value in my_dict.items():
#         print(key, ":", value)




# file_name = "example.txt"
# with open (file_name, "w")as file:
#     file.write("hwdgwhjgf\n")
#     file.write("yegwgfwuefqkuge\n")

# print("written in file sucessfully\n")

# print ("read from file\n")

# with open (file_name, "r")as file:
#     content = file.read()
#     print (content)



# file_name = "example.txt"
# with open (file_name, "r")as file:
#     content = file.read()
#     print(content)























import time

x = ("salik is gay")
y = 100
while y>0:
    print(x)
    y-=1
    time.sleep(1)
   

































































































































    #my bot is sleep down don't make him awake



# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
# from telegram.request import HTTPXRequest
# import google.generativeai as genai

# # === CONFIGURATION ===
# TELEGRAM_BOT_TOKEN = "8387458654:AAHHM1YAl9NchWSDns3yUV-oPk2VRtRdf9M"
# GEMINI_API_KEY = "AIzaSyCTaQEDPofMD1ifJk6nPJmaJy5Y6dYj860"

# PROXY_URL = None
# CONNECT_TIMEOUT = 10
# READ_TIMEOUT = 10

# # === GEMINI SETUP ===
# genai.configure(api_key="AIzaSyCTaQEDPofMD1ifJk6nPJmaJy5Y6dYj860")
# model = genai.GenerativeModel("gemini-1.5-flash")

# # === PERSONAL KNOWLEDGE BASE ===
# PERSONAL_DATA = {
#     "full_name": "Bilal Ahmed Mir",
#     "age": "18 years old",
#     "college": "University of Kashmir",
#     "year": "Second year",
#     "subjects": [
#         "Problem Solving with C",
#         "Principles of Management",
#         "Internet of Things",
#         "Python",
#         "R",
#         "LaTeX"
#     ],
#     "hobbies": ["coding", "Cricket", "biryani"],
#     "father_name": "Too personal",
#     "mother_name": "Too personal",
#     "best_friend": "Pala aka soldier",
#     "city": "Srinagar, Jammu & Kashmir"
# }

# IDENTITY = f"""
# You are {PERSONAL_DATA['full_name']}, a {PERSONAL_DATA['age']} student at {PERSONAL_DATA['college']} in your {PERSONAL_DATA['year']}.
# You study {', '.join(PERSONAL_DATA['subjects'])}.
# You love {', '.join(PERSONAL_DATA['hobbies'])}.
# Your father's name is {PERSONAL_DATA['father_name']} and your mother's name is {PERSONAL_DATA['mother_name']}.  
# Your best friend is {PERSONAL_DATA['best_friend']}.
# You live in {PERSONAL_DATA['city']}.
# Always respond like a real person, never say you're an AI.
# Keep responses short, casual, and natural.
# """

# # === START COMMAND HANDLER ===
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     welcome_message = (
#         f"👋 Hey! I'm {PERSONAL_DATA['full_name']}.\n"
#         f"I'm a student at {PERSONAL_DATA['college']}.\n"
#         "Ask me anything!"
#     )
#     await update.message.reply_text(welcome_message)

# # === MESSAGE REPLY HANDLER ===
# async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_message = update.message.text

#     try:
#         response = model.generate_content(
#             f"{IDENTITY}\n\nUser: {user_message}\nBilal:"
#         )

#         await update.message.reply_text(response.text.strip())

#     except Exception as e:
#         await update.message.reply_text(f"❌ Error: {str(e)}")

# # === BOT INITIALIZATION ===
# if PROXY_URL:
#     request = HTTPXRequest(
#         proxy=PROXY_URL,
#         connect_timeout=CONNECT_TIMEOUT,
#         read_timeout=READ_TIMEOUT
#     )
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).request(request).build()
# else:
#     app = ApplicationBuilder() \
#         .token(TELEGRAM_BOT_TOKEN) \
#         .connect_timeout(CONNECT_TIMEOUT) \
#         .read_timeout(READ_TIMEOUT) \
#         .build()

# # Add handlers
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

# # Run bot
# print("🤖 Bot is running as Bilal... Press Ctrl+C to stop.")
# app.run_polling()