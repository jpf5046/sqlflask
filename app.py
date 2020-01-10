from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    UserName = ''
    OrderID = ''
    if request.method == 'POST' and 'UserName' in request.form:
        UserName = request.form.get('UserName')
        OrderID = int(request.form.get('OrderID'))

    return render_template("home.html", UserName=UserName, OrderID = OrderID)

if __name__ == '__main__':
    app.run(debug=True)
