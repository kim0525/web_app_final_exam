# 여기에 숫자를 넣으면 어떻게 되는지 알려주는 함수


def idpw_ck(userid, pwd):
    if userid == 'aaa' and pwd == '1234':
        return "로그인 되었습니다. {}님 반갑습니다".format(userid)
    else:
        return "로그인 실패. 아이디가 없거나 패스워드가 틀렸습니다"