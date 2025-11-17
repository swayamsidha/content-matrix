import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
VECTOR_DB_DIR = os.path.join(DATA_DIR, "vectors")

os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
os.makedirs(VECTOR_DB_DIR, exist_ok=True)

# ============================================================
# MODEL NAMES (Hugging Face)
# ============================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "microsoft/phi-3-mini-4k-instruct"
SUMMARIZER_MODEL = "facebook/bart-large-cnn"

# ============================================================
# APP SETTINGS
# ============================================================

CHROMA_COLLECTION = "docs"

MAX_TOKENS = 250
TEMPERATURE = 0.7

# ============================================================
# ENVIRONMENT SWITCHES
# ============================================================

ENV = os.getenv("ENV", "dev")  # dev / prod

USE_GPU = os.getenv("USE_GPU", "false").lower() == "true"

HF_TOKEN = os.getenv("HF_TOKEN", None)

