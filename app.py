import logging
import subprocess

from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


# saasv3自动获取
@app.route('/incoming', methods=['POST'])
def hello_world():
    # logging.info('ready to pull')
    subprocess.run(args=['/root/xubobo/gittest/githook/autopull.sh'])
    return 'Hello World!'


# 新电商自动获取
@app.route('/newds', methods=['POST'])
def new_mall():
    # logging.info('ready to pull')
    subprocess.run(args=['/root/xubobo/gittest/githook/mall_pull.sh'])
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
