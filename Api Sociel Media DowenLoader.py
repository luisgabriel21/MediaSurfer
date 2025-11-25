import flask;from MediaSurfer import *
app = flask.Flask(__name__)
@app.route('/yt', methods=['POST'])
def yt():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data or not 'type' in data:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
        Url = data.get('url')
        Quality = data.get('quality', None)
        Type = data.get('type')
        x = Yt_ServIcE().Yt_DoWnlOaDeD(url=Url, quality=Quality, type=Type)
        if not x:
            return flask.jsonify({'status' : 'failed', 'reason' : 'Use Correct Data pLS'}), 400
        elif x.get('status') != 'success':
            return flask.jsonify(x), 500
        return flask.jsonify(x)
    except:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
@app.route('/insta', methods=['POST'])
def insta():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        x = InsTaGrAM_ServIcE().Insta_DoWnlOaDeD(Url)
        if not x:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        return flask.jsonify({'status':'success','ViDeO_LiNk_DeReCT':x})
    except:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
@app.route('/tiktok', methods=['POST'])
def tiktok():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        x = TiKToK_ServIcE().TiKToK_DoWnlOaDeD(Url)
        if not x:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        return flask.jsonify({'status':'success','ViDeO_LiNk_DeReCT':x, 'Quality':'Best'})
    except:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
@app.route('/spotify', methods=['POST'])
def spotify():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        x = SpOtIfY_ServIcE().SpOtIFy_DoWnlOaDeD(Url)
        print(x)
        if not x:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        return flask.jsonify({'status':'success','AuDiO_LiNk_DeReCT':x})
    except:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
@app.route('/facebook', methods=['POST'])
def Facebook():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        x = FaCeBoOk_ServIcE().FaCeBoOk_DoWnlOaDeD(Url)
        if not x:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        return flask.jsonify({'status':'success','ViDeO_LiNk_DeReCT':x,'Quality':'Normal'})
    except:
        return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
@app.route('/pinterest', methods=['POST'])
def Pinterest():
    data = flask.request.get_json()
    try:
        if not data or not 'url' in data:return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
        Url = data.get('url')
        if not Url:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        x = PiNteResT_ServIcE().PiNteResT_DoWnlOaDeD(Url)
        if not x:return flask.jsonify({'status':'Failed','reason':'Check Your Url !'}), 500
        return flask.jsonify({'status':'success','ViDeO_LiNk_DeReCT':x,'Quality':'Normal'})
    except:
        return flask.jsonify({'status' : 'failed', 'reason' : 'where data bro??'}), 401
app.run()
