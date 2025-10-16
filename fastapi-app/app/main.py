from contextlib import asynccontextmanager
from fastapi import FastAPI
from tortoise import Tortoise
from .tortoise_config import TORTOISE_ORM


# FastAPI의 lifespan 이벤트를 관리하는 함수
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션 시작 시 실행할 코드
    print("애플리케이션 시작...")
    await Tortoise.init(
        confg=TORTOISE_ORM
    )
    # await Tortoise.generate_schemas()  # DB에 테이블 자동 생성
    print("데이터베이스 초기화 완료.")

    yield  # 이 시점에서 애플리케이션이 실행됨

    # 애플리케이션 종료 시 실행할 코드
    print("애플리케이션 종료...")
    await Tortoise.close_connections()
    print("데이터베이스 연결 종료 완료.")


# FastAPI 앱을 생성할 때 lifespan 함수를 등록
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}