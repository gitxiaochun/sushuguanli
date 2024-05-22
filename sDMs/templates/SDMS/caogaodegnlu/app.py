from flask import Flask, render_template, request, flash 
from flask import Flask 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Length, EqualTo 
app = Flask(__name__) 
# app.secret_key = 'Your_seccret_key&^52@!' 
# @app.route('/', methods=['GET', 'POST']) 
# def register(): 
# # 判断请求方式
#     if request.method == 'POST': 
# # 获取表单数据
#         username = request.form.get('username') 
#         password = request.form.get('password')
#         password2 = request.form.get('password2') 
#     # 验证数据的完整性
#         if not all([username, password, password2]): 
#             flash('请填入完整信息', category='message') 
#     # 验证输入的数据是否符合要求
#         elif len(username) < 3 and len(username) > 0 or len(username) > 15: 
#             flash('用户名长度应大于 3 且小于 15', category='info') 
# # 验证两次输入的密码是否一致
#         elif password != password2: 
#             flash('密码不一致', category='error') 
#         else: 
#             return '注册成功' 
#     return render_template('register.html') 
# if __name__ == '__main__': 
#     app.run() 





# app = Flask(__name__) 
# app.config['secert_key']='qwdwef'
app.secret_key = 'Your_seccret_key&^52@!' 
class RegisterForm(FlaskForm): 
    username = StringField(label='用户名：', validators=[DataRequired(message='用户名不能为空'), Length(3, 15, message='长度应该为 3～15 个字符')]) 
    password = PasswordField('密码：', validators=[DataRequired(message='密码不能为空')]) 
    password2 = PasswordField('确认密码：', 
    validators=[DataRequired(message='密码不能为空'), EqualTo('password', message='两次密码不一致')]) 
    submit = SubmitField('注册') 
@app.route('/register',methods=['GET','post'])
def register():
    form =RegisterForm()
    if request.method=='GET':
        # username = form.username.Data
        # password =form.password.data
        # password2 =form.password.data
        # print(username)
        # print(password)
        # print(password2)
        return render_template('register.html',form=form)
    if request.method=='post':
        if form.validators_on_submit():

            username = form.username.Data
            password =form.password.data
            password2 =form.password.data
            print(username)
            print(password)
            print(password2)
        else:
            print('验真失败')
        return render_template('register.html',form=form)
    return render_template('register.html')
if __name__ == '__main__': 
    app.run() 
