class Translation(object):
    START_TEXT = """Hello,
This is a Telegram URL Upload Bot!

<b>Please send me any direct download URL Link, i can upload to telegram as File/Video</b>

/help for more details..

Support Group : @wordpress_uzb
© @wordpress_uzb , @excellend_boy & @CWProjects"""
    RENAME_403_ERR = "Kechirasiz. Sizga ushbu fayl nomini o'zgartirishga ruxsat berilmagan."
    ABS_TEXT = " Iltimos, xudbin bo'lmang"
    UPGRADE_TEXT = "<b>👉 botimiz sizga yoqsa hursandman </b>  /help for Details"
    FORMAT_SELECTION = "kerakli farmatni tanlang: <a href='{}'>fayl hajmi taxminiy bo'lishi mumkin</a> \nIf siz maxsus eskizni o'rnatmoqchisiz, quyidagi tugmachalardan birini bosgandan oldin yoki tezda fotosurat yuboring. \ nAvtomobil ravishda yaratilgan eskizni o'chirish uchun / o'chirish rasmini ishlatishingiz mumkin."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. iltimos foydalaning https://shrtz.me/PtsVnf6 va tezkor URL-manzilni oling, shunda men Telegram-ga yuklashim mumkin, boshqa foydalanuvchilar uchun sekinlashmasdan."
    DOWNLOAD_START = "yuklab olinmoqda"
    UPLOAD_START = "jo'natilmoqda"
    RCHD_BOT_API_LIMIT = "ruxsat etilgan maksimal kattalikdan kattaroq (50MB). Shunga qaramay, yuklashga harakat qilmoqda."
    RCHD_TG_API_LIMIT = "Yuklandi in {} soniya\nDetected fayl o'lchami: {}\nSorry. Ammo Telegram API cheklovlari tufayli 2 Gb dan katta fayllarni yuklay olmayman."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Iltimos, menga foydali deb topsangiz, menga baho bering. Qo'shilingn : @wordpress_uzb"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nJoin : @wordpress_uzb \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Bepul foydalanuvchilar faqatgina yuklashlari mumkin: {}\nPlease /upgrade sizning obunangiz..\nIf bu xato deb o'ylaysiz, iltimos murojaat qiling <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Maxsus video / fayl eskizi saqlandi. Ushbu rasm videoda ishlatiladi/ file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Maxsus eskiz muvaffaqiyatli bajarildi"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media muvaffaqiyatli o'chirildi."
    SAVED_RECVD_DOC_FILE = "Hujjat muvaffaqiyatli yuklab olindi."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Maxsus ThumbNail topilmadi.."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: URL uploader
Expires on: 31/12/2020"""
    HELP_USER = """Hai am URL Uploader bot..
    
1. Send url (Link|New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
   

Support Group : @wordpress_uzgroup
© @wordpress_uzb"""
    REPLY_TO_DOC_GET_LINK = "Yuqori tezlikdagi to'g'ridan-to'g'ri yuklab olish havolasini olish uchun Telegram-ga xabar yuboring"
    REPLY_TO_DOC_FOR_C2V = "Konvertatsiya qilish uchun Telegram-ga javob bering"
    REPLY_TO_DOC_FOR_SCSS = "Skrinshotlarni olish uchun Telegram-dagi ommaviy axborot vositalariga javob bering"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Telegram-ga maxsus eskizni qo'llab-quvvatlash bilan nomini o'zgartirish / o'zgartirish uchun javob bering"
    AFTER_GET_DL_LINK = "To'g'ridan-to'g'ri bog'lanish <a href='{}'>Generated</a> uchun amal qiladi {} days.\n© @AnyDLBot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Avval yuboring /downloadmedia har qanday ommaviy axborot vositasiga yuklab oling, shunda uni mahalliy tilimga yuklab olishim mumkin. \nSend /storageinfo hozirda yuklab olinayotgan ommaviy axborot vositalarini bilish."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video davomiyligi: {}\nSend /clearffmpegmedia ushbu vositani mening xotiramdan o'chirish uchun.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, yuqoridagi ommaviy axborot vositalaridan."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Saqlangan media allaqachon mavjud. Iltimos, jo'nating /storageinfo mavjud ommaviy axborot vositalarining tafsilotlarini bilish."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> DataBase-dan o'chirildi
"
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Telegramdagi ommaviy axborot vositasiga javob bering (MKV), o'rnatilgan oqimlarni chiqarish uchun"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Javob /generatecustomthumbnail media albomiga, maxsus thumbail yaratish uchun"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media albomda faqat ikkita rasm bo'lishi kerak. Iltimos, media albomni qayta yuboring, keyin qayta urinib ko'ring yoki albomga faqat ikkita rasm yuboring."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL formati noto'g'ri. urlingiz ikkalasidan ham boshlanishiga ishonch hosil qiling http:// or https://. Format havolasi yordamida maxsus fayl nomini o'rnatishingiz mumkin | file_name.extension"
    ABUSIVE_USERS = "Sizga ushbu botdan foydalanishga ruxsat berilmagan. Agar buni xato deb hisoblasangiz, iltimos, ushbu cheklovni olib tashlash uchun / meni tekshiring."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Avval siqilgan faylni yuboring, so'ngra faylga javob berish / ochish buyrug'i."
    EXTRACT_ZIP_INTRO_THREE = "Qabul qilingan faylni tahlil qilish ⚠️Bu biroz vaqt talab qilishi mumkin. Iltimos, sabr qiling. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Kechirasiz. Siqilgan faylni qayta ishlash paytida xatolar yuz berdi. Iltimos, hamma narsani yana ikki marta tekshiring va agar muammo hal etilmasa, bu haqda xabar bering <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Tanlang file_name quyidagi variantlardan yuklash uchun
Faylni olganingizdan so'ng uni nomini o'zgartirish uchun buyruqni foydalanishingiz mumkin."""
    CANCEL_STR = "Jarayon bekor qilindi"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """qayta ishlash mumkin emas.
BEpul foydalanuvchilar 30 daqiqada 1 ta so'rov jo'natisha oladi
/upgrade yoki 1800 soniyadan keyin harakat qilib ko'ring."""
    SLOW_URL_DECED = "Bu juda sekin URL kabi ko'rinadi. Siz mening uyimni buzib tashlaganingiz uchun, men ushbu faylni yuklab olishga kayfiyatim yo'q. Ayni paytda, nega buni sinab ko'rmaysiz this:==> https://shrtz.me/PtsVnf6 va tezkor URL-manzilni oling, shunda men Telegram-ga yuklashim mumkin, boshqalari uchun sekinlashmasdan."
