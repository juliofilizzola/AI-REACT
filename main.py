from langchain.chat_models import init_chat_model
from src.chat.chat import Chat
llm = init_chat_model("google_genai:gemini-2.5-flash")

def main():
    chat_service = Chat(llm)

    response = chat_service.send_message("Olá, como vai?")
    print(response)


if __name__ == "__main__":
    main()