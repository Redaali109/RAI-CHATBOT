# ==========================================================
#                    RAI AI 🤖
#              مشروع الذكاء الاصطناعي الأول
# ==========================================================

import json
import os
import datetime


MEMORY_FILE = "memory.json"
CHAT_FILE = "chat_history.json"


# ==========================================================
# تحميل الذاكرة
# ==========================================================

def load_memory():

    if os.path.exists(MEMORY_FILE):

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            pass

    return {
        "name": "",
        "memories": []
    }


# ==========================================================
# حفظ الذاكرة
# ==========================================================

def save_memory(memory):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            memory,
            file,
            ensure_ascii=False,
            indent=4
        )


# ==========================================================
# تحميل سجل المحادثة
# ==========================================================

def load_chat():

    if os.path.exists(CHAT_FILE):

        try:

            with open(CHAT_FILE, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            pass

    return []


# ==========================================================
# حفظ سجل المحادثة
# ==========================================================

def save_chat(chat):

    with open(CHAT_FILE, "w", encoding="utf-8") as file:

        json.dump(
            chat,
            file,
            ensure_ascii=False,
            indent=4
        )


# ==========================================================
# تحميل البيانات
# ==========================================================

memory = load_memory()
chat = load_chat()


# ==========================================================
# حفظ الرسالة
# ==========================================================

def save_message(user_message, bot_message):

    chat.append({

        "time": datetime.datetime.now().isoformat(),

        "user": user_message,

        "rai": bot_message

    })

    save_chat(chat)


# ==========================================================
# RAI - اللغة العربية
# ==========================================================

def rai_response_arabic(message):

    text = message.lower().strip()


    # ------------------------------------------
    # التحية
    # ------------------------------------------

    if text in [
        "سلام",
        "السلام عليكم",
        "السلام عليكم ورحمة الله وبركاته",
        "مرحبا"
    ]:

        return "وعليكم السلام ورحمة الله وبركاته يا رضا 🤖🖤"
    


    if text in [
        "هلا",
        "مرحبا",
        "اهلا",
        "أهلا",
        "أهلًا"
    ]:

        return "أهلًا! أنا RAI، او اختصار للمعنى رضا ولكن بالذكاء الاصطناعي مساعدك الشخصي 🤖"


    # ------------------------------------------
    # سؤال عن اسم RAI
    # ------------------------------------------

    if "اسمك" in text or "ماهو اسمك" in text:

        return "اسمي RAI 🤖"


    # ------------------------------------------
    # سؤال عن اسم المستخدم
    # ------------------------------------------

    if "اسمي" in text or "شنو اسمي" in text:

        if memory["name"]:

            return f"اسمك هو {memory['name']}."

        return "ما أعرف اسمك بعد. اكتب: /name اسمك",
    "الرجاء كتابه الاسم مستخدم❤"


    # ------------------------------------------
    # الوقت
    # ------------------------------------------

    if "الوقت" in text or "الساعة" in text or "ماهو الوقت الان" in text:

        now = datetime.datetime.now()

        return f"الوقت الآن هو {now.strftime('%H:%M:%S')}"


    # ------------------------------------------
    # التاريخ
    # ------------------------------------------

    if "التاريخ" in text or "اليوم" in text or "ماهو تاريخ اليوم" in text:

        now = datetime.datetime.now()

        return f"تاريخ اليوم هو {now.strftime('%Y-%m-%d')}"


    # ------------------------------------------
    # الذاكرة
    # ------------------------------------------

    if "شنو تتذكر" in text or "ماذا تتذكر" in text:

        if not memory["memories"]:

            return "ذاكرتي فارغة حاليًا 🧠"


        result = "هذه الأشياء التي أتذكرها:\n"


        for i, item in enumerate(memory["memories"], 1):

            result += f"{i}. {item}\n"


        return result


    # ------------------------------------------
    # كيف حالك
    # ------------------------------------------

    if "شلونك" in text or "كيف حالك" in text:

        return "أنا بخير وجاهز أساعدك 🤖🔥"


    # ------------------------------------------
    # شكراً
    # ------------------------------------------

    if "شكرا" in text or "شكرًا" in text:

        return "العفو! 🖤"


    # ------------------------------------------
    # وداع
    # ------------------------------------------

    if "باي" in text or "مع السلامة" in text:

        return f"  {name}مع السلامة يا 👋" or " مع السلامه يا صاح 👋"


    # ------------------------------------------
    # سؤال غير معروف
    # ------------------------------------------

    return (
        "ما زلت أتعلم 🤖\n"
        "لم أفهم السؤال بالكامل.\n"
        "في النسخة القادمة يمكننا إضافة نموذج AI حقيقي."
    )


# ==========================================================
# RAI - اللغة الإنجليزية
# ==========================================================

def rai_response_english(message):

    text = message.lower().strip()


    # ------------------------------------------
    # Greetings
    # ------------------------------------------

    if text in [
        "hello",
        "hi",
        "hey"
    ]:

        return "Hello! I am RAI, your personal assistant RAI Shortcut to Reda's personal AI assistant 🤖"


    if text in [
        "good morning"
    ]:

        return "Good morning! Have a great day 🤖☀️"


    if text in [
        "good evening"
    ]:

        return "Good evening! How can I help you? 🤖"


    # ------------------------------------------
    # Ask about RAI's name
    # ------------------------------------------

    if "your name" in text:

        return "My name is RAI 🤖"


    # ------------------------------------------
    # Ask about user's name
    # ------------------------------------------

    if "my name" in text or "what is my name" in text:

        if memory["name"]:

            return f"Your name is {memory['name']}."

        return "I don't know your name yet. Type: /name YourName"


    # ------------------------------------------
    # Time
    # ------------------------------------------

    if "time" in text or "clock" in text:

        now = datetime.datetime.now()

        return f"The current time is {now.strftime('%H:%M:%S')}"


    # ------------------------------------------
    # Date
    # ------------------------------------------

    if "date" in text or "today" in text:

        now = datetime.datetime.now()

        return f"Today's date is {now.strftime('%Y-%m-%d')}"


    # ------------------------------------------
    # Memory
    # ------------------------------------------

    if "what do you remember" in text or "your memory" in text:

        if not memory["memories"]:

            return "My memory is currently empty 🧠"


        result = "These are the things I remember:\n"


        for i, item in enumerate(memory["memories"], 1):

            result += f"{i}. {item}\n"


        return result


    # ------------------------------------------
    # How are you
    # ------------------------------------------

    if "how are you" in text:

        return "I'm doing great and I'm ready to help you 🤖🔥"


    # ------------------------------------------
    # Thank you
    # ------------------------------------------

    if "thank you" in text or "thanks" in text:

        return f"You're welcome! {name} 🖤" or "You're welcome bro! 🖤 "


    # ------------------------------------------
    # Goodbye
    # ------------------------------------------

    if "bye" in text or "goodbye" in text:

        return f"Goodbye! See you later {name} 👋" or "Goodbye! See you later bro 👋"


    # ------------------------------------------
    # Unknown question
    # ------------------------------------------

    return (
        "I'm still learning 🤖\n"
        "I didn't fully understand your question.\n"
        "In the next version, we can add a real AI model."
    )


# ==========================================================
# الواجهة العربية
# ==========================================================

def show_arabic_header():

    print()

    print("=" * 55)

    print("                 RAI AI 🤖")

    print("              مساعد رضا الشخصي")

    print("=" * 55)

    print()

    print("رجاء هذا البرنماج على قيد التطوير  ارجو معذره منكم 🌹")

    print()

    print("الأوامر:")

    print("/name اسمك       → حفظ اسمك")

    print("/remember شيء    → حفظ معلومة")

    print("/memory          → عرض الذاكرة")

    print("/forget رقم      → حذف ذاكرة")

    print("/clear           → مسح الذاكرة")

    print("/history         → عرض المحادثات")

    print("/help            → المساعدة")

    print("/exit            → خروج")

    print()


# ==========================================================
# الواجهة الإنجليزية
# ==========================================================

def show_english_header():

    print()

    print("=" * 55)

    print("                 RAI AI 🤖")

    print("           Raza's Personal Assistant")

    print("=" * 55)

    print()

    print("Please note that this program is currently under development; I ask for your understanding.")

    print()

    print("Commands:")

    print("/name YourName       → Save your name")

    print("/remember Something  → Save a memory")

    print("/memory              → Show memory")

    print("/forget Number       → Delete memory")

    print("/clear               → Clear memory")

    print("/history             → Show chat history")

    print("/help                → Show help")

    print("/exit                → Exit")

    print()


# ==========================================================
# اختيار اللغة
# ==========================================================

def choose_language():

    print()

    print("=" * 55)

    print("                 RAI AI 🤖")

    print("=" * 55)

    print()

    print("اختر اللغة / Choose language:")

    print()

    print("1. عربي 🇮🇶")

    print("2. English 🇬🇧")

    print()


    while True:

        language = input("اختيارك / Your choice: ").strip().lower()


        # ------------------------------------------
        # اللغة العربية
        # ------------------------------------------

        if language in [
            "1",
            "عربي",
            "عربية",
            "عربيه",
            "العربية",
            "arabic"
        ]:

            return "arabic"


        # ------------------------------------------
        # اللغة الإنجليزية
        # ------------------------------------------

        elif language in [
            "2",
            "english",
            "انكليزي",
            "إنكليزي",
            "انجليزي",
            "إنجليزي"
        ]:

            return "english"


        else:

            print()

            print("RAI: اكتب عربي أو English")

            print()


# ==========================================================
# تشغيل البرنامج
# ==========================================================

language = choose_language()


# ==========================================================
# إذا اختار العربية
# ==========================================================

if language == "arabic":

    show_arabic_header()


# ==========================================================
# إذا اختار الإنجليزية
# ==========================================================

elif language == "english":

    show_english_header()


# ==========================================================
# البرنامج الرئيسي
# ==========================================================

while True:

    # ------------------------------------------
    # إدخال المستخدم
    # ------------------------------------------

    if language == "arabic":

        user = input("أنت: ").strip()

    else:

        user = input("You: ").strip()


    # ------------------------------------------
    # تجاهل الإدخال الفارغ
    # ------------------------------------------

    if not user:

        continue


    # ======================================================
    # EXIT
    # ======================================================

    if user.lower() == "/exit":

        print()

        if language == "arabic":

            print(f"RAI:{name}إلى اللقاء يا  👋")

        else:

            print("RAI: Goodbye! See you later 👋")

        break


    # ======================================================
    # HELP
    # ======================================================

    if user.lower() == "/help":

        if language == "arabic":

            show_arabic_header()

        else:

            show_english_header()

        continue


    # ======================================================
    # حفظ الاسم
    # ======================================================

    if user.lower().startswith("/name "):

        name = user[6:].strip()


        if name:

            memory["name"] = name

            save_memory(memory)


            if language == "arabic":

                print(f"RAI: حفظت اسمك: {name} 🧠")

            else:

                print(f"RAI: I saved your name: {name} 🧠")


        continue


    # ======================================================
    # حفظ الذاكرة
    # ======================================================

    if user.lower().startswith("/remember "):

        information = user[10:].strip()


        if information:

            memory["memories"].append(information)

            save_memory(memory)


            if language == "arabic":

                print("RAI: تم حفظ المعلومة في ذاكرتي 🧠")

            else:

                print("RAI: Memory saved successfully 🧠")


        continue


    # ======================================================
    # عرض الذاكرة
    # ======================================================

    if user.lower() == "/memory":

        if not memory["memories"]:

            if language == "arabic":

                print("RAI: الذاكرة فارغة.")

            else:

                print("RAI: Memory is empty.")


        else:

            if language == "arabic":

                print("\nRAI - الذاكرة:")

            else:

                print("\nRAI - Memory:")


            for i, item in enumerate(memory["memories"], 1):

                print(f"{i}. {item}")


        continue


    # ======================================================
    # حذف ذاكرة
    # ======================================================

    if user.lower().startswith("/forget "):

        number = user[8:].strip()


        if number.isdigit():

            index = int(number) - 1


            if 0 <= index < len(memory["memories"]):

                deleted = memory["memories"].pop(index)

                save_memory(memory)


                if language == "arabic":

                    print(
                        f"RAI: تم حذف الذاكرة: {deleted} 🗑️"
                    )

                else:

                    print(
                        f"RAI: Memory deleted: {deleted} 🗑️"
                    )


            else:

                if language == "arabic":

                    print("RAI: رقم الذاكرة غير صحيح.")

                else:

                    print("RAI: Invalid memory number.")


        else:

            if language == "arabic":

                print("RAI: اكتب رقم الذاكرة، مثال: /forget 2")

            else:

                print("RAI: Enter the memory number, example: /forget 2")


        continue


    # ======================================================
    # مسح الذاكرة
    # ======================================================

    if user.lower() == "/clear":

        memory["memories"] = []

        save_memory(memory)


        if language == "arabic":

            print("RAI: تم مسح الذاكرة 🗑️")

        else:

            print("RAI: Memory has been cleared 🗑️")


        continue


    # ======================================================
    # سجل المحادثة
    # ======================================================

    if user.lower() == "/history":

        if not chat:

            if language == "arabic":

                print("RAI: لا توجد محادثات محفوظة.")

            else:

                print("RAI: There are no saved conversations.")


        else:

            if language == "arabic":

                print("\n===== سجل المحادثة =====")

            else:

                print("\n===== Chat History =====")


            for item in chat[-10:]:

                print()

                if language == "arabic":

                    print("أنت:", item["user"])

                    print("RAI:", item["rai"])

                else:

                    print("You:", item["user"])

                    print("RAI:", item["rai"])


                print("-" * 30)


        continue


    # ======================================================
    # الذكاء البسيط
    # ======================================================

    if language == "arabic":

        answer = rai_response_arabic(user)


    else:

        answer = rai_response_english(user)


    # ======================================================
    # عرض الإجابة
    # ======================================================

    print()

    print("RAI:", answer)

    print()


    # ======================================================

    # حفظ المحادثة

    # ======================================================

    save_message(user, answer)
