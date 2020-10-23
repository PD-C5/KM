@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == "request_location":
        line_bot_api.repuly_message(event.reply_token,TextSendMessage(text="{}\n{}".format("クリック","https://line.me/R/nv/location/")))