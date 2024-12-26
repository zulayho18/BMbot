from telegram import InlineKeyboardButton

inline_buttons = [
    [InlineKeyboardButton(text="Buxoro maktabi", callback_data="buxoro_maktabi"),
     InlineKeyboardButton(text="Muhammad MTM", callback_data="Muhammad_MTM")],
    [InlineKeyboardButton(text="OTMga tayyorlov kurslar", callback_data="otmga_tayyorlov_kurslar")],
    [InlineKeyboardButton(text="Biz ijtimoiy tarmoqda", callback_data="biz_ijtimoiy_tarmoqda")],
    [InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")],
]

maktab_inline_keyboard = [
    [InlineKeyboardButton(text="0-11 sinflar", callback_data="0-11_sinflar"),
     InlineKeyboardButton(text="PM va ixtisoslashtirilgan maktabga tayyorlov", callback_data="PM_va_ixtisoslashtirilgan_maktabga_tayyorlov")],
    [InlineKeyboardButton(text="Malakali tibbiy xizmat", callback_data="Malakali_tibbiy_xizmat"),
     InlineKeyboardButton(text="Maktab oshxonasi", callback_data="maktab_oshxonasi")],
    [InlineKeyboardButton(text="Maktab yotoqxonasi", callback_data="maktab_yotoqxonasi"),
     InlineKeyboardButton(text="Avtobus xizmati", callback_data="avtobus_xizmati")],
    [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]
]

kurslar_inline_keyboard = [
    [InlineKeyboardButton(text="Barcha aniq fanlar", callback_data="barcha_aniq_fanlar"),
     InlineKeyboardButton(text="Barcha gumanitar fanlar", callback_data="barcha_gumanitar_fanlar")],
    [InlineKeyboardButton(text="CEFR va IELTS", callback_data="CEFR_va_IELTS"),
     InlineKeyboardButton(text="SAT", callback_data="SAT")],
    [InlineKeyboardButton(text="Arab tili", callback_data="arab_tili"),
     InlineKeyboardButton(text="Turk tili", callback_data="turk_tili")],
    [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]
]

ijtimoiy_tarmoq_keyboard = [
    [InlineKeyboardButton(text="Rasmiy kanal", url="https://t.me/buxoro_maktabi"),
     InlineKeyboardButton(text="Telegram", url="https://t.me/buxoro_maktabi")],
    [InlineKeyboardButton(text="Instagram", url="forms.gle/GNGKcMrKv6j4TK42A"),
     InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]
]
