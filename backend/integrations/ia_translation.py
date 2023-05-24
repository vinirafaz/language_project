#from config.config import GPT_SECRET
import openai


openai.api_key = "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"


async def translation(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Translate to Portuguese: " + text,
        temperature=0
    )
    return response["choices"][0]["text"].replace("\n", "")

