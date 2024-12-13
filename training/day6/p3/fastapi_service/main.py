import os
from fastapi import FastAPI, BackgroundTasks, WebSocket, HTTPException
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import httpx
from dotenv import load_dotenv
import logging

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 587)),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME", "Your Application"),
    MAIL_STARTTLS=True,
    USE_CREDENTIALS=True
)

app = FastAPI()

DJANGO_API_URL = "http://127.0.0.1:8000/api"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_confirmation_email(user_email: str, event_name: str):
    message = MessageSchema(
        subject=f"Ticket Purchase Confirmation for {event_name}",
        recipients=[user_email],
        body=f"Dear User,\n\nThank you for purchasing a ticket for {event_name}.\n\nBest Regards,\nEvent Management Team",
        subtype="plain",
    )
    fm = FastMail(conf)
    try:
        await fm.send_message(message)
        logger.info(f"Confirmation email sent to {user_email} for event {event_name}.")
    except Exception as e:
        logger.error(f"Failed to send email to {user_email} for event {event_name}: {e}")

@app.get("/ticket-availability/")
async def get_ticket_availability(event_id: int, token: str):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}
        reponse = await client.get(f"{DJANGO_API_URL}/events/{event_id}/", headers=headers)
    
        if reponse.status_code != 200:
            raise HTTPException(status_code=reponse.status_code, detail="Event not found.")
        
        event_data = reponse.json()
        total_tickets = event_data.get("capacity", 0)
        booked_tickets = event_data.get("tickets", 0)
        available_tickets = total_tickets - booked_tickets
    return {"event_id": event_id, "available_tickets": available_tickets}

@app.post("/purchase-ticket/")
async def purchase_ticket(token: str, event_id: int, user_id: int, background_tasks: BackgroundTasks):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}
        availability_response = await client.get(f"{DJANGO_API_URL}/events/{event_id}/", headers=headers)

        if availability_response.status_code != 200:
            raise HTTPException(status_code=availability_response.status_code, detail="Event not found.")
        event_data = availability_response.json()
        total_tickets = event_data.get("capacity", 0)
        booked_tickets = event_data.get("tickets", 0)

        if booked_tickets >= total_tickets:
            raise HTTPException(status_code=400, detail="Cannot issue ticket: event is fully booked.")
        
        ticket_data = {
            "event": event_id,
            "user": user_id,
            "ticket_type": "Standard"
        }
        ticket_response = await client.post(f"{DJANGO_API_URL}/tickets/", json=ticket_data, headers=headers)

        if ticket_response.status_code != 201:
            raise HTTPException(status_code=ticket_response.status_code, detail="Failed to purchase ticket.")
    
        user_email = "autumn@yopmail.com"
        event_name = "Sample Event"

        background_tasks.add_task(send_confirmation_email, user_email, event_name)

        logger.info(f"Background task to send confirmation email added for {user_email}.")

        return JSONResponse(content={"message": "Ticket purchased successfully. A confirmation email will be sent shortly."})

@app.websocket("/ws/ticket-updates/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Update: {data}")

def send_confirmation_email(user_id: int, event_id:int):
    pass