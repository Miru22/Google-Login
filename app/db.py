
import os

from dotenv import load_dotenv
from gspread_models.service import SpreadsheetService
from gspread_models.base import BaseModel

load_dotenv()

# GOOGLE CREDENTIALS JSON FILE:
DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)

# GOOGLE SHEET DOCUMENT IDENTIFIER:
GOOGLE_SHEETS_DOCUMENT_ID = os.getenv("GOOGLE_SHEETS_DOCUMENT_ID", default="OOPS, Please get the spreadsheet identifier from its URL, and set the 'GOOGLE_SHEETS_DOCUMENT_ID' environment variable accordingly...")

# ONE TIME CONFIGURATION OF THE BASE MODEL:
service = SpreadsheetService(
    credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH,
    document_id=GOOGLE_SHEETS_DOCUMENT_ID
)
BaseModel.service = service

# NOW YOU CAN IMPORT THE BASE MODEL FROM HERE AND ANY CHILD MODELS WILL USE THIS CONFIG
