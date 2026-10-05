from datetime import date
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Riderboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rider = {
    "name": "Riley",
    "initials": "RK",
    "online": True,
    "date": date.today().strftime("%A, %d %B"),
    "stats": {
        "deliveries": 12,
        "earned": 86.40,
        "rating": 4.9,
        "average_time": "18 min",
    },
    "selected_order": "#1042",
}

orders: list[dict[str, Any]] = [
    {
        "id": "#1042",
        "customer": "Bela Kovacs",
        "restaurant": "Green Bowl",
        "address": "Bartok Bela ut 12",
        "status": "Ready",
        "position": [47.501, 19.034],
    },
    {
        "id": "#1041",
        "customer": "Anna Nagy",
        "restaurant": "Mamma Mia",
        "address": "Kinizsi utca 8",
        "status": "Delivering",
        "position": [47.492, 19.057],
    },
    {
        "id": "#1040",
        "customer": "Mark Toth",
        "restaurant": "Urban Wok",
        "address": "Raday utca 22",
        "status": "Picked up",
        "position": [47.485, 19.066],
    },
]


class RiderStatus(BaseModel):
    online: bool


@app.get("/api/dashboard")
def get_dashboard() -> dict[str, Any]:
    return {"rider": rider, "orders": orders, "center": [47.4979, 19.0402]}


@app.patch("/api/rider/status")
def update_rider_status(status: RiderStatus) -> dict[str, bool]:
    rider["online"] = status.online
    return {"online": rider["online"]}


@app.patch("/api/orders/{order_id}/select")
def select_order(order_id: str) -> dict[str, str]:
    if not any(order["id"] == order_id for order in orders):
        raise HTTPException(status_code=404, detail="Order not found")
    rider["selected_order"] = order_id
    return {"selected_order": rider["selected_order"]}
