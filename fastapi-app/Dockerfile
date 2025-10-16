# Dockerfile (가상환경 없는 최종 버전)

FROM python:3.13

WORKDIR /code

# 1. requirements.txt 파일을 먼저 복사합니다.
COPY requirements.txt /code/

# 2. pip을 사용해서 라이브러리를 '글로벌' 환경에 설치합니다.
RUN pip install -r requirements.txt

# 3. 우리 앱 코드를 복사합니다.
COPY ./app /code/app

# 4. 가상환경 경로 없이 uvicorn을 직접 실행합니다.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]