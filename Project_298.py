import paho mqtt
import time
import flask

app = Flask(__name__)

broker = 'broker.emqx.io'
port = 1883
topic = "topicName/pir"

client_id = 'test_29'
username = 'emqx'
password = ''


def on_message(client, userdata, msg):

detection = msg.payload.decode('utf8')

@app.route('/', methods=['GET'])

for i in range(0, 10):
	