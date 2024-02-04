import os, sys
from openai import OpenAI
from tools import tools
from tool_executor import ToolExecutor

client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))

def run_conversation():
    question = sys.argv[1]
    messages = [{"role": "user", "content": question}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  
    )
    response_message = response.choices[0].message
    calls = response_message.tool_calls
    print('calls', calls)

run_conversation()
