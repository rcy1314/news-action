import requests
import os

telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
report_date = os.environ['REPORT_DATE']
file_text = os.environ['FILE_TEXT']

message = f"今日新闻简报推送 ({report_date}):\n\n{file_text}"

url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
data = {
    'chat_id': telegram_channel_id,
    'text': message
}

response = requests.post(url, json=data)
response.raise_for_status()