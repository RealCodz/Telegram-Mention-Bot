# بوت تاك تيليكرام 🔥 | Telegram Mention Bot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Telethon](https://img.shields.io/badge/Telethon-Latest-orange)

## وصف | Description

بوت تاك يسوي منشنات للأعضاء بشكل دوري ويختار رسائل عشوائية من ملف نصوص.

*A Telegram bot that mentions group members periodically with random messages from a text file.*

<br>

## شنو يسوي؟ | What it does?

**بالعربي:**
- يسوي تاكات لكل أعضاء الكروب
- يختار رسالة عشوائية من ملف النصوص
- يشتغل بأمر "/on" ويبدأ التاكات بأمر "/tag"
- يوكف عمله بأمر "/off"

**In English:**
- Mentions all group members
- Selects random messages from a text file
- Activates with "/on" command and starts tagging with "/tag" command
- Stops tagging with "/off" command

<br>

## الملفات | Files

**بالعربي:**
- `bot.py`: الكود الرئيسي للبوت بلغة بايثون
- `texts.txt`: قائمة الرسائل العشوائية اللي راح تنرسل مع التاكات
- `requirements.txt`: المكاتب المطلوبة
- `Procfile`: ملف خاص بخدمة Heroku للتشغيل
- `runtime.txt`: إصدار بايثون المستخدم

**In English:**
- `bot.py`: Main Python code for the bot
- `texts.txt`: List of random messages that will be sent with mentions
- `requirements.txt`: Required libraries
- `Procfile`: Heroku deployment file
- `runtime.txt`: Python version used

<br>

## تنصيب من كيتهاب | Installation from GitHub

```bash
git clone https://github.com/RealCodz/Telegram-Mention-Bot.git
cd Telegram-Mention-Bot
pip install -r requirements.txt
```

<br>

## طريقة التشغيل | How to Run

**بالعربي:**
1. ضيف API_ID و API_HASH و BOT_TOKEN الخاصة بيك بملف `bot.py`
2. نزل المكاتب: `pip install -r requirements.txt`
3. شغل البوت: `python bot.py`

**In English:**
1. Add your API_ID, API_HASH, and BOT_TOKEN to `bot.py` file
2. Install required libraries: `pip install -r requirements.txt`
3. Run the bot: `python bot.py`

<br>

## الأوامر | Commands

| الأمر العربي | English Command | الوصف | Description |
|-------------|----------------|--------|-------------|
| `تفعيل`     | `/on`          | يفعل البوت | Activates the bot |
| `تاك`       | `/tag`         | يبدأ بعمل تاكات | Starts tagging members |
| `ايقاف`     | `/off`         | يوقف عمل التاكات | Stops tagging members |
| `تواصل`     | `/contact`     | يعرض روابط التواصل | Shows contact links |

<br>

## المميزات التقنية | Technical Features

**بالعربي:**
- مكتوب بلغة بايثون 🐍
- يستخدم مكتبة Telethon للتعامل مع API تيليكرام
- سهل التثبيت والتشغيل
- يشتغل على منصة Heroku مباشرة

**In English:**
- Written in Python 🐍
- Uses Telethon library for Telegram API interaction
- Easy installation and operation
- Works directly on Heroku platform

<br>

## الرخصة | License

هذا المشروع مرخص تحت [رخصة MIT](LICENSE)

*This project is licensed under the [MIT License](LICENSE)*
