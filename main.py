from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# статика
app.mount("/images/A_B", StaticFiles(directory="images/A_B"), name="static")

# функция для чтение JSON 
def read_ticket(id: int):
    try:
        with open(f'questions/A_B/tickets/Билет {id}.json', 'r', encoding='utf-8') as files:
            return json.load(files)
    except FileNotFoundError:
        return None
    except Exception as error:      
        return {"error": f"An error occurred: {str(error)}"}


@app.get("/api/ticket/{id}")
async def get_ticket(id: int):
    """
    Получить информацию о билете по его идентификатору.

    :param id: Идентификатор билета.
    :type id: int

    :return: JSON-данные о билете.
    :rtype: dict
    """
    ticket_data = read_ticket(id)
    if ticket_data: # проверка что данные получены
        return JSONResponse(content=ticket_data)
    else:
        return JSONResponse(content={"error": "Ticket not found"}, status_code=404)

@app.get('/api/ticket/{id}/{title}')
async def get_answer(id: int, title: int):
    """
    Получить вопрос в билете индентификатору билета и вопроса.

    :param id: Идентификатор билета.
    :type id: int

    :param title: Идентификатор вопроса.
    :type title: int

    :return: JSON-данные ответа на билет.
    :rtype: dict
    """
    ticket_data = read_ticket(id)
    if ticket_data: # проверка что данные получены
        if title <= len(ticket_data):
            return JSONResponse(content=ticket_data[title - 1])
        else:
            return JSONResponse(content={"error": "Answer title not found"}, status_code=404)
    else:
        return JSONResponse(content={"error": "Ticket not found"}, status_code=404)
