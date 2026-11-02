import discord, os, aiohttp
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API_KEY")
SERVER_ID = "98bc3d3d"
PANEL_URL = "https://panel.azureclouds.xyz"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ ONLINE: {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Eternal SMP | !start"))

@bot.command(name="status")
async def status(ctx):
    embed = discord.Embed(title="⚡ ETERNAL SMP", color=0x00ff00)
    embed.add_field(name="IP", value="`cloud.azureclouds.xyz:25613`", inline=False)
    embed.add_field(name="Start Karne ke liye", value="`!start` likho", inline=False)
    await ctx.send(embed=embed)

@bot.command(name="start")
async def start(ctx):
    await ctx.send("🚀 Server ON kar raha hu... 30 sec ruko")
    url = f"{PANEL_URL}/api/client/servers/{SERVER_ID}/power"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    try:
        async with aiohttp.ClientSession() as s:
            async with s.post(url, json={"signal": "start"}, headers=headers) as r:
                if r.status in [200,202,204]:
                    await ctx.send("✅ **Ho gaya!** 1 min me join kar sakte ho `cloud.azureclouds.xyz:25613` pe")
                else:
                    await ctx.send(f"❌ Error {r.status} - API Key galat hai")
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@bot.event
async def on_message(msg):
    if msg.author.bot: return
    if msg.content.lower() in ["start","server start"]:
        ctx = await bot.get_context(msg)
        await start(ctx)
    await bot.process_commands(msg)

bot.run(TOKEN)
