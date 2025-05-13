# # utils.py

# import openai
# from django.conf import settings

# print("OpenAI API Key:", settings.OPENAI_API_KEY)
# # Configura la clave de API de OpenAI
# openai.api_key = settings.OPENAI_API_KEY

# def summarize_news(news_list):
#     summarized_news = []  # Lista para almacenar los resúmenes
#     for news in news_list:
#         # Construye el prompt para resumir una sola noticia
#         prompt = f"Resumen de la noticia: {news.title}\n\n{news.content}\n\nGenera un resumen breve y conciso:"
        
#         try:
#             # Llama a la API de OpenAI para generar el resumen
#             response = openai.ChatCompletion.create(
#                 model=settings.OPENAI_MODEL,
#                 messages=[
#                     {"role": "system", "content": "Eres un asistente que resume noticias."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 max_tokens=100,  # Limita el número de tokens para el resumen
#                 temperature=0.7  # Ajusta la creatividad de la respuesta
#             )
#             # Extrae el texto del resumen
#             summary = response['choices'][0]['message']['content'].strip()
#             summarized_news.append({
#                 'title': news.title,
#                 'summary': summary,
#             })
#         except Exception as e:
#             print(f"Error al generar el resumen: {e}")
#             summarized_news.append({
#                 'title': news.title,
#                 'summary': "No se pudo generar el resumen."
#             })
    
#     return summarized_news
