from pyrogram import Client, filters
import config
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query(filters.regex("rules"))
async def cbrules(bot: Client, callback_query: CallbackQuery):
    aku = await bot.get_me()
    await callback_query.message.edit(
            text=f"🗣️ RULES {aku.first_name}\n\n❌ PROMOSI TANPA IZIN\n❌ UP 18+ TANPA IZIN\n❌ JUALAN TANPA IZIN\n❌ UP LINK TANPA IZIN\n\n🗣️ RESIKO AUTO GBAN",
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                 InlineKeyboardButton("Kembali ⬅️", callback_data="startt"),
                ]
                ]
                )
        
        )

@Client.on_callback_query(filters.regex("penjelasan"))
async def cbpenjelasan(bot: Client, callback_query: CallbackQuery):
    aku = await bot.get_me()
    join = await bot.get_chat(config.channel_1)
    await callback_query.message.edit(
            text=f"**Apa itu MENFESS?**\n\n📝 Dikutip dari **Urbandictionary**, kata **menfess** merupakan akronim atau singkatan dari dua kata, yakni **Mention** dan **Confess**. Menfess biasa digunakan untuk __curhat, mengomel, atau mengungkapkan sesuatu.__\n\n📝 Dalam bahasa Inggris, **Mention** artinya menyebutkan, menandai atau semacamnya. Sementara **Confess** artinya pengakuan, mengakui dan lain-lain. Sehingga jika diterjemahkan **menfess** kurang lebih artinya sebagai __sebutan mengaku atau sebutan pengakuan__\n\n📝 Berdasarkan penelusuran di **media sosial**, istilah **menfess** kerap digunakan ketika seseorang ingin mengungkapkan sesuatu kepada orang lain atau semua orang secara anonim\n\nApa itu **{aku.first_name}**\n\n📝 **{aku.first_name}** adalah sarana yang akan membantumu untuk menyampaikan pesan secara anonim kepada seseorang atau semua orang di telegram yang tergabung ke dalam Channel @{join.username} Kamu hanya perlu mengirimkan pesan sesuai aturan bot ini, dan kamu dapat menikmati berbagai fiturnya!.",
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                 InlineKeyboardButton("Kembali ⬅️", callback_data="startt"),
                ]
                ]
                )
        
        )

@Client.on_callback_query(filters.regex("startt"))
async def cbstart(bot: Client, callback_query: CallbackQuery):
    aku = await bot.get_me()
    join = await bot.get_chat(config.channel_1)
    await callback_query.message.edit(
            text=f"Hallo! {aku.mention} akan membantumu untuk mengirimkan pesan secara anonim ke channel @{join.username}. Silakan sampaikan pesanmu atau pap cute atau video konten positif kamu\n\nSebelum menggunakan silakan baca rules terlebih dahulu ya😉",
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                 InlineKeyboardButton("📌 Rules", callback_data="rules"),
                 InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan")
                 ],
                 [
                 InlineKeyboardButton("💬 Group", url=f"t.me/{config.group}"),
                 InlineKeyboardButton("Channel 📢", url=f"t.me/{join.username}")
                 ],
                 [
                 InlineKeyboardButton("🎁 DONASI 🎁 ", url=f"https://saweria.co/DonasiBuatFwbsssBot"),
                 InlineKeyboardButton("🌟 MENU MENFESS 🌟", callback_data="menu")
                 ]
                ]
                )
        
        )

@Client.on_callback_query(filters.regex("menu"))
async def cbmenuuu(bot: Client, callback_query: CallbackQuery):
    await callback_query.message.edit(
                text=config.menu_msg,
                reply_markup=InlineKeyboardMarkup(
                    [
                    [
                    InlineKeyboardButton("Kembali ⬅️", callback_data="startt")
                    ]
                    ]
                    )
            
            )
