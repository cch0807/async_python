# ASGI
- ASGI는 어플리케이션 프로그램(FastAPI)의 실행 결과를 웹 서버에 전달해주며, 웹 서버는 ASGI로부터 전달받은 결과를 웹 클라이언트(브라우저)에 전송한다.
    - 서버 게이트웨이 : 서버로 들어가는 입구 역할

# Uvicorn
- uvloop, httptools를 사용하는 ASGI 웹 서버(프로세스 관리자, 실행기)
    - uvicorn : ASGI 웹 어플리케이션을 실행하는 서버
    - starlette : 웹 어플리케이션 프레임워크

    