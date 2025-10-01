

## 고유 URL 더미데이터 만드는데 필요한 파일 

```
# app/__init__.py 

from fastapi import FastAPI 
from fastapi.responses import ORJSONResponse 
# ORJSONResponse는 JSON응답을 처리하는 클래스 
# Rust로 작성된 고성능 JSON 라이브러리 

# FastAPI가 모든 JSON응답에 대해 ORJSONResponse를 사용하도록 설정
app = FastAPI( 
	default_response_class=ORJSONResponse )


```

```
# app/dtos/create_meeting_response.py 

# annotated: 타입 힌트와 메타데이터를 함께 사용 
# basemodel: pydantic의 기본 모델 클래스 
# Field: 핃르에 대한 추가 정보 정의 
# Frozen Config: 설정 상수 
from typing import Annotated
from pydantic import BaseModel, Field
from app.dtos.frozen_config import FROZEN_CONFIG

# pydantic 모델의 동작 방식을 설정한다 
# frozn 방식, 객체 생성 후 수정 불가능 
class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

# annotated: 타입과 메타데이터 함께 정의하는 방법 
# 필드 정의, 문자열은 str, Field 설명(API 문서에 표시됨), 
    url_code: Annotated[str, Field(description="미팅 URL 코드. unqiue 합니다.")]

```

```

#app/apis/v1/meeting_router.py

# api router를 활용하여 post 엔드포인트 만들기
# api router는 여러 api 엔드포인트를 논리적으로 그룹화하여 코드 구조를 모듈화하고 관리하기 쉽게 함 
from fastapi import APIRouter
from app.dtos.create_meeting_response import 

CreateMeetingResponse

# 실제에서는 블루프린트에 db 이름을 쓰면 안됨
# 각 라우터는 독립적으로 경로 및 메서드를 정의하고 FastAPI 앱에 포함됨 
# prefix: 라우터에 등록된 모든 엔드포인트 경로 앞에 사용될 기본 url 
# tags: API 문서에서 분류를 위해 사용됨 
# redirect_slashes=false: url이 슬래시로 끝나는 경우, 자동 리다이렉트를 비활성화 

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)

# 엔드포인트 등록
# @edgedb_router.post(""): post 방식으로 엔드포인트를 등록한다. 실제 URL은 prefix와 결합 (/v1/edgedb/meetings)
# description: API 문서에 설명을 추가 함
# async def: 비동기 함수로 정의 
# 반환 타입: createmeetingresponse 모델 반환 예시 코드는 url_code = "abc"
# mysqldb도 같은 방식 

@edgedb_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")

@mysql_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


#흐름 설명: 
#두 개의 독립된 router를 만들고, 각각 다른 DB에 맞는 meeting 생성 api 엔드포인트를 만든다. 
# 엔드포인트 함수는 요청을 받아 결과를 만들어 지정된 형태 (CreateMeetingResponse)로 반환한다. 

```