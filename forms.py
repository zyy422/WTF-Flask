from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import *


class QueForm(Form):
    remember = BooleanField('ALL')
    remember0 = BooleanField('GENER-1300')
    remember1 = BooleanField('OTFC-1300D/C')
    remember2 = BooleanField('OTFC-1300D(特')
    remember3 = BooleanField('OTFC-1550D/C')
    remember4 = BooleanField('OTFC-1800D')
    remember5 = BooleanField('OTFC-1800C')
    remember6 = BooleanField('AR-1300D')
    remember7 = BooleanField('OTFC-900D')
    remember8 = BooleanField('OTFC-1100DA/CA')
    remember9 = BooleanField('OTFC-1100DB/CB')
    remember10 = BooleanField('OTFC-600C(S014)')
    remember11 = BooleanField('LED-600')
    remember12 = BooleanField('STAR-1300')
    remember13 = BooleanField('OTFC-2350')
    remember14 = BooleanField('MTFC-900CAI')
    file = FileField("upload")
    submit = SubmitField("excel数据上传",validators=[FileRequired(),FileAllowed(['xlsx'],'只接收.xlsx格式的文件')])

    def add_mac_no(self, mac_no):  # add machine serial
        che_mac_no = BooleanField(mac_no)



