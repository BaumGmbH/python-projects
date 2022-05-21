import asyncio
import discord
from discord import Member

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Among Us'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('mein cooler bot'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(content):
    if content.author.bot:
        return
    if content.content.startswith('!'):
        await content.delete()

    if '!help' in content.content:
        await content.channel.send('**Hilfe zum Discord.py**\r\n'
                                   '!help - Zeigt diese Hilfe an')

    if content.content.startswith('!userinfo'):
        args = content.content.split(' ')

        if len(args) == 2:
            member: Member = content.mentions[0]

            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten',
                                value=member.joined_at.strftime('%d.%m.%Y %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten',
                                value=member.created_at.strftime('%d.%m.%Y %H:%M:%S'),
                                inline=True)

                roles = ''
                for role in member.roles:
                    if not role.is_default():
                        roles += '{} \r\n'.format(role.mention)

                if roles:
                    embed.add_field(name='Rollen',
                                    value=roles,
                                    inline=True)

                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Angefragt von {}'.format(content.author.name))

                message = await content.channel.send(embed=embed)
                await message.add_reaction(':potato:688712726138060810')


client.run('NjkwODU4NjczNTM0NDAyNjAx.XnXiRw.uofzNxmI6JNBIXQQ5DGzgkCHRaM')
