import os
import pickle
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from transformers import T5ForConditionalGeneration, T5Tokenizer

from api.v1.translate import translate_router
from core.config import settings

app = FastAPI(title=settings.TITLE, version=settings.VERSION)

# mount static file location for model and tokenizer
current_file = Path(__file__)
current_file_dir = current_file.parent
project_root = current_file_dir.parent
project_root_absolute = project_root.resolve()
static_root_absolute = project_root_absolute / "static"


app.mount("/static", StaticFiles(directory=static_root_absolute), name="static")


# helper function to install and save model and tokenizer
def get_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=512)
    model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)

    # save model and tokenizer to static directory
    model.save_pretrained("static/t5base_model")
    with open("static/tokenizer.pickle", "wb") as f:
        pickle.dump(tokenizer, f)


# run the helper function on app start if t5base_model directory
# does not exist else don't run it
@app.on_event("startup")
def on_startup():
    if not os.path.isdir(static_root_absolute/"t5base_model"):
        get_model()


# redirect home page to docs page
@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


# include extra routers to application
app.include_router(translate_router, prefix=settings.API_PREFIX)
