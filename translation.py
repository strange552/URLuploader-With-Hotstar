class Translation(object):

    START_TEXT = """Hi, This is a Itachi❤️ <b>[Telegram Upload Bot]</b>

<i>Send Me Any Direct Download URL Link, I Will Upload To Telegram As File/Video</i>

<i>For more details send /help</i>

<b>Made In India 🇮🇳</b?>
"""

    HELP_USER = """Hai I'am Telegram URL Uploader bot..
    
<b>1. Send url [Link | New Name with Extension(mkv,mp4,avi etc)].</b>

<b>2. Send Custom Thumbnail (Optional).</b>

<b>3. Select the button.</b>
   
   <b>SVideo - Give File as video with Screenshots</b>
   
   <b>DFile  - Give File with Screenshots</b>
   
   <b>Video  - Give File as video without Screenshots</b>
   
   <b>File  - Give File without Screenshots</b>

<b>Support Group : @AnimeBotSupportGroup</b>
"""

    FORMAT_SELECTION = """Select the desired format: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "I Thank @PrgOfficial for his <a href='https://github.com/prgofficial/URLuploader-With-Hotstar'>Open source Code</a>"
    
    DOWNLOAD_START = "<code>Downloading..📥</code>"
    
    UPLOAD_START = "<code>Uploading..📤</code>"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "<b>Thumbnail Permanently saved✔️</b> \n\nSend /Deletethumbnail to delete"

    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>Thumbnail cleared ✔️</b>"

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    
