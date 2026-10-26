"""Start server.py over stdio like a real MCP client and call each tool once."""
import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).parent


async def main() -> None:
    params = StdioServerParameters(command=sys.executable, args=[str(HERE / "server.py")])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("tools:", [t.name for t in tools.tools])
            calls = [
                ("search_grants", {"theme": "fuel poverty", "limit": 3}),
                ("search_grants", {"theme": "community energy", "year_from": 2020, "limit": 3}),
                ("get_funder_summary", {"funder": "Nesta"}),
                ("get_recipient", {"name_or_id": "GB-CHC-1135192", "limit": 2}),
                ("get_recipient", {"name_or_id": "Age"}),
            ]
            for name, args in calls:
                res = await session.call_tool(name, args)
                text = res.content[0].text
                print(f"\n== {name} {args}  ({len(text)} chars)\n{text[:700]}")


asyncio.run(main())
