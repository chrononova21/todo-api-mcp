import asyncio
import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import load_mcp_servers
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider
from pathlib import Path

script_dir = Path(__file__).parent
mcp_path = script_dir / "mcp_config.json"
servers = load_mcp_servers(config_path=mcp_path)
load_dotenv()

azure_model = OpenAIChatModel(
    model_name=os.getenv("DEPLOYMENT"),
    provider= AzureProvider (
        azure_endpoint= os.getenv("ENDPOINT"),
        api_version= os.getenv("OPENAI_API_VERSION"),
        api_key= os.getenv("OPENAI_API_TOKEN")
    ),
)


agent = Agent(
    model=azure_model,
    system_prompt=(
        "You are a helpful todo list manager assistant. "
        "You have access to tools for managing tasks. "
        "Always use the available tools to retrieve, add, update, or delete tasks. "
        "When the user asks about tasks, use the get_all_tasks tool to fetch them. "
        "Never respond without checking the actual task data using the tools."
    ),
    toolsets=servers
)

async def main():
    result = await agent.run('Show me all the tasks')
    print(result.output)

if __name__ == '__main__':
    asyncio.run(main())