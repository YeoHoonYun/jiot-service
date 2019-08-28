import pyqrcode, time
from flask import Flask, send_file, request
app = Flask(__name__)

@app.route('/get_image')
def get_image():
    base_dir = "./"
    file_format = "png"
    url = "www.naver.com"
    scale = 10
    # localhost:5000/get_image?format=png&url=www.google.com&scal=20
    print(request.args)
    try:
        if request.args.get("format"):
            file_format = request.args.get("format")
        else:
            pass

        if request.args.get("url"):
            url = request.args.get("url")

        else:
            pass

        if request.args.get("scal"):
            scale = request.args.get("scal")
        else:
            pass
    except:
        pass
    #filename = base_dir + str(time.time()).replace(".","") +'.' + file_format
    filename = base_dir + 'qr'
    print(filename)

    file = pyqrcode.QRCode(url, error='H')

    if request.args.get("format") == "eps":
        pyqrcode.create(url).eps(filename, scale=scale)
        return send_file(filename, mimetype='application/postscript')
    elif request.args.get("format") == "png":
        file.png(filename, scale=scale)
        return send_file(filename, mimetype='image/png')
    elif request.args.get("format") == "jpg":
        file.png(filename, scale=scale)
        return send_file(filename, mimetype='image/jpg')
    else:
        file.png(filename, scale=scale)
        return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=517, debug=True)