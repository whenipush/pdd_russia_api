<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ПДД билеты 2023 API</title>
</head>
<body>
    <h1>ПДД билеты 2023 API</h1>

    <img src="https://example.com/logo.png" alt="Лого проекта">

    <p><strong>ПДД билеты 2023 API</strong> - это RESTful API для доступа к вопросам и ответам к экзамену по Правилам Дорожного Движения (ПДД) на 2023 год. Это API предоставляет возможность получения информации о билетах и ответах на вопросы, что может быть полезно для обучения и подготовки к экзамену.</p>

    <h2>Основные функции</h2>
    <ul>
        <li>Получение информации о билетах по идентификатору.</li>
        <li>Получение ответов на вопросы в билетах по идентификатору билета и вопроса.</li>
        <li>Документирование API с использованием Swagger UI.</li>
    </ul>

    <h2>Установка и запуск</h2>
    <ol>
        <li>Клонируйте репозиторий:</li>
        <pre><code>git clone https://github.com/yourusername/pdd-bilety-api.git</code></pre>
        <li>Установите зависимости:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Запустите приложение:</li>
        <pre><code>uvicorn main:app --host 0.0.0.0 --port 8000 --reload</code></pre>
        <li>Откройте документацию API в браузере:</li>
        <pre><code>http://localhost:8000/docs</code></pre>
    </ol>

    <h2>Использование API</h2>

    <h3>Получение информации о билете</h3>
    <ul>
        <li><strong>Метод:</strong> GET</li>
        <li><strong>Путь:</strong> /api/ticket/{id}</li>
        <li><strong>Параметры:</strong> id (int) - Идентификатор билета.</li>
        <li><strong>Пример запроса:</strong></li>
        <pre><code>GET /api/ticket/1</code></pre>
        <li><strong>Пример ответа:</strong></li>
        <pre><code>{
    "id": 1,
    "title": "Билет №1",
    "questions": [
        {
            "question": "Вопрос 1",
            "options": ["Ответ 1", "Ответ 2", "Ответ 3"],
            "correct_option": 1
        },
        {
            "question": "Вопрос 2",
            "options": ["Ответ 1", "Ответ 2", "Ответ 3"],
            "correct_option": 2
        }
    ]
}</code></pre>
    </ul>

    <h3>Получение ответа на вопрос в билете</h3>
    <ul>
        <li><strong>Метод:</strong> GET</li>
        <li><strong>Путь:</strong> /api/ticket/{id}/{title}</li>
        <li><strong>Параметры:</strong> id (int) - Идентификатор билета. title (int) - Номер вопроса.</li>
        <li><strong>Пример запроса:</strong></li>
        <pre><code>GET /api/ticket/1/1</code></pre>
        <li><strong>Пример ответа:</strong></li>
        <pre><code>{
    "question": "Вопрос 1",
    "options": ["Ответ 1", "Ответ 2", "Ответ 3"],
    "correct_option": 1
}</code></pre>
</body>
</html>
