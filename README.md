## FastAPI MCP Todo Application

- Run the command `uv run uvicorn src.main:app --port 8000` to start the API/MCP Server.
- Run the command `uv run -m src.agent` to run the MCP client.
- The MCP client uses Pydantic AI agent as the client to run the queries. 
- You can change the queries in the main function to try out different tools.
    For example:
    1) `List all the tools you have.`
    2) `Show me all the tasks`
    3) `Delete the task (Give the task title)` 