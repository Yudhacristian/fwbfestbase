import os
from dotenv import load_dotenv

load_dotenv("fwb.env")


api_id = int(os.environ.get("API_ID", "WAJIB DIISI"))
api_hash = os.environ.get("API_HASH", "WAJIB DIISI")
bot_token = os.environ.get("BOT_TOKEN", "WAJIB DIISI")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://username:password@cluster0.d9fwl.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "WAJIB DIISI"))
channel_log = int(os.environ.get("CHANNEL_LOG", "WAJIB DIISI"))
# =========================================================== #
owner = os.environ.get("OWNER")
id_admin = int(os.environ.get("ID_ADMIN", "WAJIB DIISI"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "50"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "20"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "20"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "20"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "20"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "20"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "20"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "100"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "50"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "50"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "50"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "50"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#fwbgirl #fwbboy #fwbadlt #fwbspill #fwbstory #ask").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY")
pic_girl = os.environ.get("PIC_GIRL")
start_img = os.environ.get("START_IMG")
# =========================================================== #
group = os.environ.get("GROUP")
pesan_join = os.environ.get("PESAN_JOIN", "Kamu tidak dapat menggunakan bot silahkan beli coin melalui /beli atau join channel terlebih dahulu")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", "{mention}, pesan mu gagal terkirim silahkan klik /start lalu pilih menu menfes")

menu_msg = os.environ.get("PESAN_MENU", "#fwbgirl Untuk cewe\n#fwbboy Untuk cowo\n#fwbadlt Untuk 18+\n#fwbspill Untuk pamer\n#fwbstory Untuk bercerita / curhat\n#ask Untuk bertanya\n\n🗣️ Wajib username ya fewbess")
