from flask import Flask,render_template,request
from forms import QueForm
from read_excel import read_excel
from operate_db import ExeMysql

app = Flask(__name__)
app.secret_key = "optorun@1"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = QueForm()
    if request.method == 'GET':
        db = ExeMysql()
        mac = db.query()
        all_coa = []
        for ma in mac:
            all_coa.append(ma[0])
        return render_template('line-stack.html', form=form, mac=all_coa)
    else:
        f = request.files['file']
        exl_data = read_excel(f)
        db = ExeMysql()
        db.insert(exl_data)
        return render_template('line-stack.html', form=form)


if __name__ == '__main__':
    app.run()
