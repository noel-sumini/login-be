from fastapi import Request, APIRouter
from schemas import UserInfoModel

router = APIRouter()


members = [
    {'userid': 'sumin111', 'password' : '1234'},
    {'userid': 'sumin222', 'password': '5678'}
]


@router.get("/ping", status_code = 200)
def ping(request:Request):
    return {"msg" : "pong"}

@router.post("/login", status_code = 200)
def login(request: Request, user_info:UserInfoModel):
    
    userid = user_info.userid
    password = user_info.password

    member = [m for m in members if m['userid'] == userid]
    if len(member) == 0:
        return {"msg" : "회원이 아닙니다."}
    elif member[0]['password'] != password:
        return {"msg" : "패스워드를 확인해주세요."}
    else:
        return {"msg" : "로그인에 성공하였습니다. 환영합니다."}