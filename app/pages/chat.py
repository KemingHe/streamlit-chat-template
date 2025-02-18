from components.page_ui import setup_page
from components.chat_ui import setup_simple_chat

# from chains.web_search_chain import get_web_search_response_stream
from agents.web_search_agent import get_agent_response_stream

setup_page(
    page_title="Web Search Chatbot",
    page_description="This chatbot can perform a single-step web search and provide relevant information to the user.",
)

# setup_simple_chat(get_web_search_response_stream)
setup_simple_chat(get_agent_response_stream)
