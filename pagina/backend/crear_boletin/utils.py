# utils.py
import requests
from django.conf import settings

def summarize_news(news_list):
    summarized_news = []
    api_url = "https://api.apyhub.com/ai/summarize-text"  # CORRECTO

    headers = {
        "Content-Type": "application/json",
        "apy-token": settings.APYHUB_API_KEY
    }

    for news in news_list:
        # Forzar español con instrucción inicial
        content = f"Resume el siguiente texto en español:\n{news.content}"

        payload = {
            "text": content,
            "summary_length": 'long',
            "output_language":'es'
        }

        try:
            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 200:
                data = response.json()
                summary = data.get("data", {}).get("summary", "Resumen no disponible.")
            else:
                print(f"Error en API ApyHub: {response.status_code} - {response.text}")
                summary = "No se pudo generar el resumen."

        except Exception as e:
            print(f"Error al generar el resumen: {e}")
            summary = "No se pudo generar el resumen."

        summarized_news.append({
            'title': news.title,
            'summary': summary,
        })

    return summarized_news
