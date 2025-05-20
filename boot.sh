# Для запуска в консоли для проверки
python3 boot.py


# Собираем докер образ - выполняем в директории с файлом Dockerfile
sudo docker build -t mms_ai_agent .
# Удаляем контейнер с именем mms_ai_agent
sudo docker rm mms_ai_agent
# Запускаем контейнер с именем mms_ai_agent
sudo docker run -it -p 8000:8000 --name mms_ai_agent mms_ai_agent

# Для запуска в консоли для отправки запроса
curl --user user:12345 -X POST "http://localhost:8000/sum" \
  -H "Content-Type: application/json" \
  -d '{"a": 5.2, "b": 3.8}'
