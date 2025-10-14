from fastapi import FastAPI  # Header, Cookie
from .config import settings

app = FastAPI()

# 이미지 받기. 여기서 선언하고 Sub 클래스로 쓰는거임
# class Image(BaseModel):
#     url: str = Field(..., example = "http://example.com/image.jpg")
#     name: str = Field(..., example = "Product Image")

# Field 사용(example로 타입 구체화)
# class Item(BaseModel):
#     name: str = Field(..., example = "게이밍 마우스")
#     description: str | None = Field(default=None, example="버티컬 마우스.")
#     price: float = Field(..., example = 59.99)
#     tax: float = Field(default = None, ge=0, example=0.1)
#
#     tags: list[str] = Field(default=[], example = ["전자제품", "게이밍 마우스", "PC 주변기기"])
#
#     image: Image | None = Field(default=None)

# Field 랑 Config 사용 (json_schema_extra로 예시 구체화)
# class Item(BaseModel):
#     name: str = Field(..., min_length=2, max_length=50)
#     description: str | None = Field(default=None, max_length=500)
#     price: float = Field(..., gt=0)
#     tax: float | None = Field(default=None, ge=0)
#     tags: list[str] = Field(default = [])
#     image: Image | None = Field(default=None)
#
#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "name": "버티컬 마우스",
#                 "description": "손목이 편안한 마우스",
#                 "price": 59.99,
#                 "tax": 0.1,
#                 "tags": ["버티컬", "PC 부품", "마우스"],
#                 "image": {
#                     "url": "http://example.com/image.jpg",
#                     "name": "Product Image",
#                 }
#             }
#         }

# 단일 아이템 받을 때
# @app.post("/items/")
# def create_item(item: Item):
#     return item

# 다중 아이템 받을 때
# @app.post("/items/bulk/")
# def create_bulk_item(items: list[Item]):
#     return {"message": f"{len(items)} items created.", "data": items}

# 헤더 받는 방법 확인
# @app.get("/items/protected/")
# def get_protected_items(
#         authorization: str = Header(
#             ...,
#             description = "Bearer 토큰 포함"
#     ),
#         accept_language: str | None = Header(
#             default="en-US",
#             description = "사용자 언어"
#     ),
#         x_request_id: str | None = Header(
#             default = None,
#             alias = "X-Request-Id",
#             description = "요청 추적을 위한 고유 ID"
#     )
# ):
#     return {
#         "message": "보호된 아이템 목록입니다",
#         "auth_token_type": authorization.split(" ")[0] if " " in authorization else "Unknown",
#         "preferred_language": accept_language,
#         "request_id": x_request_id
#     }
#
# # 쿠키 받기 실습
# @app.get("/cookies")
# def get_cookies(ads_id: str | None = Cookie(default=None)):
#     return{"ads_id": ads_id}


# Response Model 실습
# class UserIn(BaseModel):
#     username: str = Field(..., example="john_doe")
#     email: str = Field(..., example="john.doe@example.com")
#     password: str = Field(..., example="asdf")
#
# class UserDB(UserIn):
#     hashed_password: str = Field(..., example="#@##")
#
# class UserOut(BaseModel):
#     id: int = Field(..., example=123)
#     username: str = Field(..., example="john_doe")
#     email: str = Field(..., example="john.doe@example.com")
#
# fake_user_db ={}
# user_counter = 0
#
# @app.post("/users/", response_model=UserOut)
# def create_user(user_in: UserIn):
#     global user_counter
#     user_counter += 1
#
#     hashed_password = "hashed_" + user_in.password
#
#     user_in_db=UserDB(
#         **user_in.model_dump(),
#         hashed_password=hashed_password
#     )
#
#
#
#     user_id = user_counter
#     fake_user_db[user_id] = user_in_db.model_dump()
#
#     response_data = {"id": user_id, **user_in.model_dump()}
#
#     return response_data

# os 사용 .env 불러오기
# @app.get("/info")
# def get_info():
#     return {
#         "app_name": config.APP_NAME,
#         "debug_mode": config.DEBUG_MODEL,
#         "secrete_key_prefix": config.SECRET_KEY[:5] + "...",
#     }

# pydentic-settings 사용 .env 불러오기
@app.get("/info/")
def get_info():
    return {
        "app_name": settings.APP_NAME,
        "debug_mode": settings.DEBUG_MODEL,
        "secrete_key_prefix": settings.SECRETE_KEY[:5] + "..."
    }