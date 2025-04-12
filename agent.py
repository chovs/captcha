from langchain_deepseek import ChatDeepSeek
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio
import time

initial_actions = [
    {'open_tab': {'url': 'https://v0-captcha-test-page-yuk7ve.vercel.app/'}}
]

llm = ChatDeepSeek(model="deepseek-reasoner")

async def main():
    agent = Agent(
        task="pass the captcha by sliding the slider, try every thing you can to pass the captcha like clicking and hold until it passes",
        llm=llm,
        use_vision=True,
        initial_actions=initial_actions,
        retry_delay=10
    )
    
    # Set maximum number of steps to 3
    max_steps = 3
    
    try:
        # Run the agent with a limit of 3 steps
        result = await agent.run(max_steps=max_steps)
        
        # Check if the agent completed the task successfully
        if result and result.is_successful():
            print("SUCCESS: Captcha passed successfully!")
        else:
            print("FAILED: Could not pass the captcha within the maximum allowed steps.")
            
    except Exception as e:
        print(f"FAILED: An error occurred while trying to pass the captcha: {e}")
    
    # The program will end naturally here

asyncio.run(main())


