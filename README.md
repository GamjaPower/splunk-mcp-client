# splunk-mcp-client

Splunk MCP 엔드포인트를 JSON-RPC 2.0으로 호출하는 최소한의 예제 모음(curl + Python).

## 준비물
- Python 3.10+ (`pip install -r requirements.txt`로 requests, python-dotenv 설치)
- 프로젝트 루트에 `.env` 파일
  - `MCP_ENDPOINT` 예: `https://splunk-server-ip:8089/services/mcp`
  - `SPLUNK_MCP_TOKEN` : MCP 인증 토큰
- 각 파이썬 스크립트는 `verify=False`로 TLS 검증을 끄므로 신뢰할 수 있는 환경에서만 사용하세요.

## 사용 방법 (추천 순서)
1) `mcp_ping.sh`  
   - curl로 `/services/mcp`에 `ping` 호출. 원격/로컬 두 블록이 있음.  
   - 토큰이 하드코딩되어 있으니 실행 전 교체 필수.  
   - 실행: `sh mcp_ping.sh`
   - 만약 에러가 발생하면 Splunk 서버에서 localhost로 직접 호출해서 정상 동작하면 중간에 방화벽을 의심해봐야 함 
   - 방화벽 문제가 있어도 SSL 에러가 발생하는 경우가 있으니 방화벽 설정을 확인 해야함 


2) `mcp_ping.py`  
   - 환경변수 기반 `ping` 호출 (랜덤 UUID id).  
   - 실행: `python mcp_ping.py`

3) 기타 파이썬 유틸  
   - `mcp_toollist.py`: `tools/list` 호출, 이용 가능한 MCP 도구 나열.
     실행: `python mcp_toollist.py`  
   - `mcp_get_indexes.py`: `tools/call` 로 `get_indexes` 실행, `row_limit`(기본 100, 1–1000)과 `offset`(기본 0) 전달.  
     실행: `python mcp_get_indexes.py --row-limit 200 --offset 5`

## 테스트
- 경로 문제를 피하기 위해 테스트에서 프로젝트 루트를 `sys.path`에 추가함.  
- 가상환경에서 `pytest` 설치 후 실행: `pytest -q`

## 팁
- `.env.example`를 복사해 `.env`를 만든 뒤 값을 채우세요.
- 사내망/VPN 등 신뢰 가능한 네트워크에서만 사용하세요.
- 인증서 검증이 필요하면 `mcp_client.py`의 `verify=False`를 제거하거나 `True`로 바꾸세요.
