from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import inline_buttons, maktab_inline_keyboard, kurslar_inline_keyboard, ijtimoiy_tarmoq_keyboard

def start_func(update, context):
    main_button = [KeyboardButton(text="Ma'lumotlar")]
    reply_markup = ReplyKeyboardMarkup([main_button], resize_keyboard=True)
    update.message.reply_text(text="Assalomu alaykum. <<Buxoro maktabi>> botiga xush kelibsiz.", reply_markup=reply_markup)

def message_handler(update, context):
    message = update.message.text

    if message == "Ma'lumotlar":
        reply_markup = InlineKeyboardMarkup(inline_buttons)
        update.message.reply_text(text="Ma'lumotlarni tanlang:", reply_markup=reply_markup)
    else:
        words = context.user_data.get('matn', [])
        words.append(update.message.text)
        context.user_data['matn'] = words
        print(f"{update.message.from_user.username}: {words}")

def inline_messages(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'buxoro_maktabi':
        reply_markup = InlineKeyboardMarkup(maktab_inline_keyboard)
        query.message.edit_text(text="Maktab bo'limlarini tanlang:", reply_markup=reply_markup)
    elif query.data == 'Muhammad_MTM':
        query.message.reply_video(video='https://t.me/buxoro_maktabi/IMG_1482.mp4')
        row = [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]
        keyboard = [row]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text(text="Orqaga tugmasini tanlang:", reply_markup=reply_markup)
    elif query.data == 'otmga_tayyorlov_kurslar':
        reply_markup = InlineKeyboardMarkup(kurslar_inline_keyboard)
        query.message.edit_text(text="Kurslarni tanlang:", reply_markup=reply_markup)
    elif query.data == 'biz_ijtimoiy_tarmoqda':
        reply_markup = InlineKeyboardMarkup(ijtimoiy_tarmoq_keyboard)
        query.message.edit_text(text="Ijtimoiy tarmoqlarimizni tanlang:", reply_markup=reply_markup)
    elif query.data == "ro'yxatdan_o'tish":
        text = ("Farzandingizni ro'yxatdan o'tkazish uchun +998-94-851-66-66, +998-94-852-66-66 va +998-90-715-60-06 raqamlariga qo'ng'iroq qiling.")
        keyboard = [[InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)
    elif query.data == 'orqaga':
        query.message.edit_text(text="Ma'lumotlarni tanlang:", reply_markup=InlineKeyboardMarkup(inline_buttons))
    elif query.data == "0-11_sinflar":
        text = ("Bizning xususiy maktabda <<maktabga tayyorlov>> sinflari rus va o'zbek guruhlari mavjud. 1 sinfdan 11 sinfgacha farzandingiz qobiliyati va istagiga ko'ra chuqurlashtirilgan sinflarda tahsil olishlari mumkin.")
        keyboard = [[InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)
    elif query.data == "PM_va_ixtisoslashtirilgan_maktabga_tayyorlov":
        text = ("Bizning xususiy maktabda farzandingizni kelajakda PM, M.Ulug'bek, Ibn Sino va hududdagi ixtisoslashtirilgan maktab o'quvchisi bo'lishiga imkon beruvchi chuqurlashtirilgan sinflarda tahsil olishi mumkin.")
        keyboard = [[InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)
    elif query.data == "Malakali_tibbiy_xizmat":
        text = ("Bizning xususiy maktabda farzandingiz salomatligi  malakali tibbiy xodimlarimiz nazorati ostida.")
        keyboard = [[InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)
    elif query.data == "maktab_oshxonasi":
        query.message.edit_text(text="BM Oshxonasi:", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="BM Oshxonasi", url="https://t.me/bm_oshxonasi")],
             [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]))
    elif query.data == "maktab_yotoqxonasi":
        text = ("Bizning xususiy maktabda shaxardan tashqarida istiqomat qiluvchi o'quvchilar uchun zamonaviy, barcha qulayliklarga ega maktab yotoqxonasi mavjud.")
        keyboard = [[InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)
    elif query.data == "avtobus_xizmati":
        text = ("Bizning xususiy maktabda farzandingizni o'z vaqtida maktabga yetib kelishi va darslardan so'ng uyingizga eltib qo'yish uchun shaxar ichi va shaxar tashqarisi bo'lgan qo'shni Piskent va Oxangaron tumanlariga avtobus xizmati qo'yilgan.")
        keyboard = [[InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)
    elif query.data == "Rasmiy_kanal":
        query.message.edit_text(text="rasmiy_kanal:", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="rasmiy_kanal", url="https://t.me/buxoro_maktabi")],
             [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]))
    elif query.data == "Telegram":
        query.message.edit_text(text="telegram:", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="telegram", url="https://t.me/buxoro_maktabi")],
             [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]))
    elif query.data == "Instagram":
        query.message.edit_text(text="instagram:", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="instagram", url="forms.gle/GNGKcMrKv6j4TK42A")],
             [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]]))
