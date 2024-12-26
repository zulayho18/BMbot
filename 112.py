

def inline_messages(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'buxoro_maktabi':
        reply_markup = InlineKeyboardMarkup(maktab_inline_keyboard)
        query.message.edit_text(text="Maktab bo'limlarini tanlang:", reply_markup=reply_markup)
    elif query.data == 'Muhammad_MTM':
        query.message.reply_video(video=open (url='https://t.me/buxoro_maktabi, sirk MOV', 'rb'))
        row = [InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]
        keyboard = [row]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text(text="Orqaga tugmasini tanlang:", reply_markup=reply_markup)