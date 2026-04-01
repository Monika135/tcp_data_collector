import socket
import threading
import json
import os
from dotenv import load_dotenv
from api.db_session import ScopedSession
from models.device_model import DeviceCards

load_dotenv()

HOST = os.environ.get("TCP_SERVER_HOST", "0.0.0.0")
PORT = int(os.environ.get("TCP_SERVER_PORT", 5000))


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    local_session = None
    try:
        local_session = ScopedSession()
        buffer = ""
        while True:
            data = conn.recv(4096)
            if not data:
                break

            buffer += data.decode()

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                try:
                    payload = json.loads(line)
                    device_id = payload.get("device_id")
                    card_id = payload.get("card_id")

                    if not device_id or not card_id:
                        raise ValueError("Missing fields")

                    record = DeviceCards(device_id=device_id, card_id=card_id)
                    local_session.add(record)
                    local_session.commit()

                    response = {
                        "message": "Data stored successfully",
                        "status": True,
                        "client_ip_address": addr[0]
                    }

                except Exception as e:
                    local_session.rollback()
                    response = {
                        "message": "Invalid JSON or missing fields",
                        "status": "error",
                        "detail": str(e)
                    }

                conn.sendall((json.dumps(response) + "\n").encode())

    except Exception as e:
        print("Connection error:", e)
    finally:
        if local_session:
            local_session.close()
        conn.close()
        print(f"[DISCONNECTED] {addr}")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"TCP Server listening on {PORT}")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        )

        thread.start()


if __name__ == "__main__":
    start_server()