import config
import re

from pyrogram import Client, enums, types
from plugins import Database, Helper

async def talent_handler(client: Client, msg: types.Message):
    db = Database(msg.from_user.id)
    talent = db.get_data_bot(client.id_bot).talent
    top_rate = [] # total rate talent
    top_id = [] # id talent
    if len(talent) == 0:
        return await msg.reply('<b>Saat ini tidak ada talent yang tersedia.</b>', True, enums.ParseMode.HTML)
    else:
        for uid in talent:
            rate = talent[str(uid)]['rate']
            if rate >= 0:
                top_rate.append(rate)
                top_id.append(uid)
        top_rate.sort(reverse=True)
        pesan = "<b>Daftar Talent Fwb</b>\n\n"
        pesan += "No — Talent — Rating\n"
        index = 1
        for i in top_rate:
            if index > config.batas_talent:
                break
            for j in top_id:
                if talent[j]['rate'] == i:
                    pesan += f"<b> {str(index)}.</b> {talent[j]['username']} ➜ {str(talent[j]['rate'])} 🍓\n"
                    top_id.remove(j)
                    index += 1
                    
        pesan += f"\nmenampilkan {config.batas_talent} talent dengan rating tertinggi\n"
        pesan += "berikan rating untuk talent favoritmu dengan perintah <code>/rate id</code>\n"
        pesan += "contoh <code>/rate 37339222</code>"
        await msg.reply(pesan, True, enums.ParseMode.HTML)

async def tambah_talent_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addtalent(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah talent</b>\n\n<code>/addtalent id_user</code>\n\nContoh :\n<code>/addtalent 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addtalent(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan user admin", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if await db.cek_user_didatabase():
            status = [
                'admin', 'owner', 'talent', 'daddy sugar', 'moans girl',
                'moans boy', 'girlfriend rent', 'boyfriend rent'
            ]
            member = db.get_data_pelanggan()
            if member.status in status:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat menjadikan talent</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            try:
                a = await client.get_chat(target)
                nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                await client.send_message(
                    int(target),
                    text=f"<i>Kamu telah menjadi talent bot</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                    parse_mode=enums.ParseMode.HTML
                )
                await db.tambah_talent(int(target), client.id_bot, nama)
                return await msg.reply_text(
                    text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi talent bot</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            except Exception as e:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
        else:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tamabh talent</b>\n\n<code>/addtalent id_user</code>\n\nContoh :\n<code>/addtalent 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def hapus_talent_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]hapus(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan hapus talent</b>\n\n<code>/hapus id_user</code>\n\nContoh :\n<code>/hapus 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    x = re.search(r"^[\/]hapus(\s|\n)*(\d+)$", msg.text or msg.caption)
    if x:
        target = x.group(2)
        db = Database(int(target))
        if await db.cek_user_didatabase():
            member = db.get_data_pelanggan()
            if member.status == 'owner' or member.status == 'admin':
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()}</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            if member.status == 'talent':
                try:
                    await db.hapus_talent(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            elif member.status == 'daddy sugar':
                try:
                    await db.hapus_sugar_daddy(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            elif member.status == 'moans girl':
                try:
                    await db.hapus_moans_girl(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            elif member.status == 'moans boy':
                try:
                    await db.hapus_moans_boy(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            elif member.status == 'girlfriend rent':
                try:
                    await db.hapus_gf_rent(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            elif member.status == 'boyfriend rent':
                try:
                    await db.hapus_bf_rent(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            else:
                return await msg.reply_text(
                    text=f"<i><a href='tg://openmessage?user_id={str(target)}'>User</a> bukan seorang talent</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
        else:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan hapus talent</b>\n\n<code>/hapus id_user</code>\n\nContoh :\n<code>/hapus 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def rate_talent_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]rate(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="perintah salah, gunakan perintah /rate id untuk memberikan rating kepada talent", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    x = re.search(r"^[\/]rate(\s|\n)*(\d+)$", msg.text)
    if x:
        target = x.group(2)
        db = Database(msg.from_user.id)
        user = db.get_data_pelanggan()
        db_bot = db.get_data_bot(client.id_bot)
        my_coin = user.coin
        if msg.from_user.id == int(target):
            return await msg.reply('tidak dapat memberi rating kepada diri sendiri', True)
        
        if target in db_bot.talent:
            if my_coin <= config.biaya_talent:
                return await msg.reply(f'coin kamu kurang untuk memberikan rating ke talent fwb. biaya rate adalah {str(config.biaya_talent)} coin', True)  
            to_talent = my_coin - config.biaya_talent
            await db.rate_talent(target, client.id_bot, to_talent)
            return await msg.reply(f'kamu berhasil memberikan 1 🍓 kepada {target}', True)
        
        elif target in db_bot.daddy_sugar:
            if my_coin <= config.biaya_daddy_sugar:
                return await msg.reply(f'coin kamu kurang untuk memberikan rating ke talent fwb. biaya rate adalah {str(config.biaya_daddy_sugar)} coin', True)
            to_talent = my_coin - config.biaya_daddy_sugar
            await db.rate_sugar_daddy(target, client.id_bot, to_talent)
            return await msg.reply(f'kamu berhasil memberikan 1 🥂 kepada {target}', True)
        
        elif target in db_bot.moansgirl:
            if my_coin <= config.biaya_moansgirl:
                return await msg.reply(f'coin kamu kurang untuk memberikan rating ke talent fwb. biaya rate adalah {str(config.biaya_moansgirl)} coin', True)
            to_talent = my_coin - config.biaya_moansgirl
            await db.rate_moans_girl(target, client.id_bot, to_talent)
            return await msg.reply(f'kamu berhasil memberikan 1 🍬 kepada {target}', True)
        
        elif target in db_bot.moansboy:
            if my_coin <= config.biaya_moansboy:
                return await msg.reply(f'coin kamu kurang untuk memberikan rating ke talent fwb. biaya rate adalah {str(config.biaya_moansboy)} coin', True)
            to_talent = my_coin - config.biaya_moansboy
            await db.rate_moans_boy(target, client.id_bot, to_talent)
            return await msg.reply(f'kamu berhasil memberikan 1 🍥 kepada {target}', True)
        
        elif target in db_bot.gfrent:
            if my_coin <= config.biaya_gfrent:
                return await msg.reply(f'coin kamu kurang untuk memberikan rating ke talent fwb. biaya rate adalah {str(config.biaya_gfrent)} coin', True)
            to_talent = my_coin - config.biaya_gfrent
            await db.rate_gf_rent(target, client.id_bot, to_talent)
            return await msg.reply(f'kamu berhasil memberikan 1 🌸 kepada {target}', True)
        
        elif target in db_bot.bfrent:
            if my_coin <= config.biaya_bfrent:
                return await msg.reply(f'coin kamu kurang untuk memberikan rating ke talent fwb. biaya rate adalah {str(config.biaya_bfrent)} coin', True)
            to_talent = my_coin - config.biaya_bfrent
            await db.rate_bf_rent(target, client.id_bot, to_talent)
            return await msg.reply(f'kamu berhasil memberikan 1 👓 kepada {target}', True)
        
        else:
            await msg.reply(f'{target} bukan seorang talent fwb.', True)
