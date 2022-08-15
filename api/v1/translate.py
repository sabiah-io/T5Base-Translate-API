import pickle

from fastapi import APIRouter, status
from transformers import T5ForConditionalGeneration

from schemes.translate import DestinationEnum, SourceEnum

translate_router = APIRouter(tags=["Translate"])


# load model and tokenizer on app start
@translate_router.on_event("startup")
def load_model_tokenizer():
    # global values necessary to utilize model and tokenizer
    # variables outside function
    global model
    global tokenizer
    model = T5ForConditionalGeneration.from_pretrained("static/t5base_model")
    with open("static/tokenizer.pickle", "rb") as f:
        tokenizer = pickle.load(f)


@translate_router.post("/translate", status_code=status.HTTP_200_OK)
async def translate(
    source_language: SourceEnum, destination_language: DestinationEnum, input_text: str
):
    """
    Translate text across four (4) different languages

    - **source_language**: language to translate from
    - **destination_language**: language to translate to
    - **input_text**: text to translate

    returns **translated_text**: text translation from input text
    """

    input_ids = tokenizer(
        "translate {} to {}: {}".format(
            source_language.value, destination_language.value, input_text
        ),
        return_tensors="pt",
    ).input_ids
    # generate vector from input ids
    outputs = model.generate(input_ids)
    # decode vector to retrieve translated text
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"translated_text": translated_text}
