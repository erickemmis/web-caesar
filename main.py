import cgi
from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE hmtl>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
	        <label for="rot">Rotate by:</label>
	        <input type="text" name="rot" id="rot" value="0"/>
	        <textarea name="text">
            {0}
	        </textarea>
	        <input type="submit">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    message = str(request.form['text'])
    ##errot check
    if rot:
        rot = rot.strip()
        rot = int(rot) % 26
    else:
        return form.format("Please enter valid rotation")

    if message:
        message = str(message)
    else:
        return form.format("Please enter valid message")



    #rotate string by n characters
    encrypted = rotate_string(message, rot)

    return form.format(encrypted)




app.run()
