import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!add_role'):
        # Replace "ROLE NAME" with the name of the role you want to give to all members
        role_name = "ROLE NAME"
        role = discord.utils.get(message.guild.roles, name=role_name)
        for member in message.guild.members:
            await member.add_roles(role)
        await message.channel.send("All members have been given the {} role.".format(role_name))

# Replace "TOKEN" with your bot's token
client.run('TOKEN')
