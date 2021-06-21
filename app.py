from flask import Flask, render_template, request, session, redirect

from test import idpw_ck
import adb

app = Flask(__name__)

# 세션처리를 위한 키
app.secret_key = b'aaa!111/'

@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/circus')
def circus():
    return render_template('circus.html')

@app.route('/galaga')
def galaga():
    return render_template('galaga.html')

@app.route('/tower')
def tower():
    return render_template('tower.html')

@app.route('/haxelg')
def haxelg():
    return render_template('haxelg.html')
       


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        name = request.form['username']
        userid = request.form['userid']
        pwd = request.form['pwd']
        # 회원정보를 데이터베이스에 넣기
        adb.insert_user(userid, name, pwd)
        return '<b>{}, {}, {}</b> 님 회원가입 되었습니다.'.format(name, userid, pwd)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        # 로그인이 맞는 체크해서 데이터가 있으면 성공 없으면 실패
        ret = adb.get_user(userid, pwd)
        if ret != None:
            print(ret[1])
            session['name'] = ret[1]  # 세션에 정보 넣기
            return redirect('/')
        else:
            return redirect('/signin')
        # return idpw_ck(userid, pwd)

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect('/')


@app.route('/search')
def search():
    # 만약에 로그인 상태이면 검색 페이지 나오고
    if 'name' in session:
        return render_template('search.html')
    # 아니면 로그인 페이지로 이동
    else:
        return redirect("/signin")

@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.method == "GET":
        return '그냥 넘어옴(GET)'
    else:
        name = request.form['fname']
        return '<b>{}</b> 로 검색한 결과입니다. 리스트 쫙~~(POST)'.format(name)



# if __name__ == '__main__':
#    app.run(debug=True)