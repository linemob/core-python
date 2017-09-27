from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from src.receiver import Receiver
app = Flask(__name__)


handler = WebhookHandler('cc19d3de5e1f7201cdbff7f0e8dfbf3e')


@app.route('/')
def index():
    return "<h1>Hello I'm fine!</h1>"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('receiver here!')
    receiver = Receiver(event)


if __name__ == "__main__":
    app.run()
