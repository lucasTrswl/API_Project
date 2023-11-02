from enum import Enum

import psycopg2
import psycopg2.extras
from fastapi import FastAPI
from pydantic import BaseModel

conn = psycopg2.connect(
    dbname="popo",
    user="postgres",
    password="postgres",
)

# cursor will return data as dictionary for easier parsing.
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

app = FastAPI()


