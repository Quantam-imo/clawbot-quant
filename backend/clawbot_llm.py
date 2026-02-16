# Lightweight LLM handler using llama-cpp-python
from llama_cpp import Llama
import os

MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "./models/tinyllama-1.1b-chat.ggmlv3.q4_0.bin")

# Load the model (ensure the model file exists at MODEL_PATH)
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def ask_llama(question: str) -> str:
    try:
        response = llm(
            question,
            max_tokens=256,
            stop=["</s>", "\n"],
            echo=False
        )
        text = response["choices"][0]["text"].strip()
        if not text:
            return "Clawbot: No answer generated. Please try again or check model file."
        return text
    except Exception as e:
        print(f"[Clawbot LLM Error] {e}")
        return f"Clawbot: LLM error ({e}). Please check model file or logs."
