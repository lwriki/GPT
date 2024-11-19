import requests
# Ваш API ключ OpenAI
API_KEY = 'API'  # Замените на ваш API ключ
# URL для доступа к API OpenAI
API_URL = 'https://api.openai.com/v1/chat/completions'
# Прокси-сервер
PROXY = {
    "http": "http://34.111.135.19:80",
    "http": "http://172.67.171.233:80",

}

def chat_with_ai(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data, proxies=PROXY)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Ошибка: {response.status_code}, {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при подключении к API: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("Пользователь: ")
        if user_input.lower() in ['EXIT', 'exit']:
            break
        ai_response = chat_with_ai(user_input)
        print(f"ИИ: {ai_response}")
