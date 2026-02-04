# MCP Ping Script
curl -k -X POST https://splunk-server-ip:8089/services/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIGF3cy1wb2MiLCJzdWIiOiJhZG1pbiIsImF1ZCI6Im1jcCIsImlkcCI6IlNwbHVuayIsImp0aSI6IjJhMDMxMWFmNmUzOWZjOTlmMmQzZDI3YWIxMDU3M2ZmODI5ZjllZjkyZDBlYTRhZTFlMDAzYTJmNzRjNmUyM2YiLCJpYXQiOjE3NzAyMDU0NDAsImV4cCI6MTc3Mjc5NzQ0MCwibmJyIjoxNzcwMjA1NDQwfQ.NhJUTifr9WID4ZqQEFoXsCqK5C9ddvKZgEybvmI-ZsYv2svGVr5d-etqSNehq-uQQyyK0cbKfIBs7Wux4iKy1A" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "ping",
    "params": {}
  }'

# Alternative endpoint for localhost testing
# curl -k -X POST https://127.0.0.1:8089/services/mcp \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIGF3cy1wb2MiLCJzdWIiOiJhZG1pbiIsImF1ZCI6Im1jcCIsImlkcCI6IlNwbHVuayIsImp0aSI6IjJhMDMxMWFmNmUzOWZjOTlmMmQzZDI3YWIxMDU3M2ZmODI5ZjllZjkyZDBlYTRhZTFlMDAzYTJmNzRjNmUyM2YiLCJpYXQiOjE3NzAyMDU0NDAsImV4cCI6MTc3Mjc5NzQ0MCwibmJyIjoxNzcwMjA1NDQwfQ.NhJUTifr9WID4ZqQEFoXsCqK5C9ddvKZgEybvmI-ZsYv2svGVr5d-etqSNehq-uQQyyK0cbKfIBs7Wux4iKy1A" \
#   -d '{
#     "jsonrpc": "2.0",
#     "id": "1",
#     "method": "ping",
#     "params": {}
#   }'  

