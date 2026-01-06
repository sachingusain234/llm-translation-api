from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="moonshotai/kimi-k2-instruct",groq_api_key=groq_api_key)

# Creating the Prompt Template 
system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system',system_template),
        ('user','{text}')
    ]
)

# Creating the output parser
parser = StrOutputParser()

# Create Chain
chain = prompt_template|model|parser

# App definition
app = FastAPI(title="Langchain Server",
             version="1.0",
              description="A Simple API server using Langchain runnable interfaces"
             )

# Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)


