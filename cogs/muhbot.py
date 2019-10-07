import requests
import json
import random
import discord
from discord.ext import commands
from discord.utils import get
import asyncio

class Muhbot(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('muhbot: online')
        print('arbi: online')
        time1=''

        global faction
        faction=''
        data={
            "Mercury":"https://vignette.wikia.nocookie.net/warframe/images/4/41/Mercury.png/revision/latest/scale-to-width-down/350?cb=20161016165617",
            "Venus":"https://vignette.wikia.nocookie.net/warframe/images/d/dc/Venus.png/revision/latest/scale-to-width-down/350?cb=20161013035729",
            "Earth":"https://vignette.wikia.nocookie.net/warframe/images/1/1e/Earth.png/revision/latest/scale-to-width-down/350?cb=20161016212227",
            "Mars":"https://vignette.wikia.nocookie.net/warframe/images/d/de/Mars.png/revision/latest/scale-to-width-down/350?cb=20161016192350",
            "Phobos":"https://vignette.wikia.nocookie.net/warframe/images/b/bf/Phobos.png/revision/latest/scale-to-width-down/350?cb=20161016180047",
            "Ceres":"https://vignette.wikia.nocookie.net/warframe/images/2/24/Ceres.png/revision/latest/scale-to-width-down/350?cb=20161016192352",
            "Jupiter":"https://vignette.wikia.nocookie.net/warframe/images/6/68/Jupiter.png/revision/latest/scale-to-width-down/350?cb=20161016193837",
            "Europa":"https://vignette.wikia.nocookie.net/warframe/images/6/63/Europa.png/revision/latest/scale-to-width-down/350?cb=20161016193842",
            "Saturn":"https://vignette.wikia.nocookie.net/warframe/images/2/28/Saturn.png/revision/latest/scale-to-width-down/350?cb=20161014034807",
            "Uranus":"https://vignette.wikia.nocookie.net/warframe/images/4/42/UranusCutout.png/revision/latest/scale-to-width-down/70?cb=20161016041655",
            "Neptune":"https://vignette.wikia.nocookie.net/warframe/images/1/15/Neptune.png/revision/latest/scale-to-width-down/350?cb=20161016195815",
            "Pluto":"https://vignette.wikia.nocookie.net/warframe/images/3/35/Pluto.png/revision/latest/scale-to-width-down/350?cb=20161016195904",
            "Sedna":"https://vignette.wikia.nocookie.net/warframe/images/4/48/Sedna.png/revision/latest/scale-to-width-down/350?cb=20161016202602",
            "Eris":"https://vignette.wikia.nocookie.net/warframe/images/b/b3/Eris.png/revision/latest/scale-to-width-down/350?cb=20161016204513",
            "Void":"https://vignette.wikia.nocookie.net/warframe/images/4/46/Void.png/revision/latest/scale-to-width-down/350?cb=20161016211233",
            "Lua":"https://vignette.wikia.nocookie.net/warframe/images/9/91/Lua.png/revision/latest/scale-to-width-down/350?cb=20161016180034"
        }

        emojiList={
            "Infested":self.bot.get_emoji(626796876292816896),
            "Grineer":self.bot.get_emoji(626796876049678356),
            "Corpus":self.bot.get_emoji(626796875822923807),
            "Orokin":self.bot.get_emoji(626796876049678356)
        }

        channel_list=[
            624999751674232869,
            626807390460969019
        ]

        while True:
            req2=requests.get('https://ws.warframestat.us/pc')
            arbi=req2.json()['arbitration']
            time2=arbi['expiry']
            if time1==time2:
                await asyncio.sleep(120)
            else:
                print(time1 + time2)
                time1=time2
                node=arbi['node']
                enemy=arbi['enemy']
                _type=arbi['type']
                planet=arbi['planet']
                
                def emojislc(emj):
                    return emojiList[emj]
                
                def solNode(plt):
                    embed=discord.Embed(
                        title=node, 
                        description=f"{str(_type)} against {str(enemy)} {emojislc(enemy)}", 
                        color=0xfafbf9
                    )
                    embed.set_author(name="New Arbitration has Started on")
                    embed.set_thumbnail(url=plt)
                    return embed

                for ch in channel_list:
                    channel=self.bot.get_channel(ch)
                    await channel.send(embed=solNode(data[planet]), delete_after=60.0)
                await asyncio.sleep(120)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if 'arcane acceleration' in message.content.lower():
            embed=discord.Embed(color=0x5ff1f1)
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/3/3d/ArcaneAcceleration.png/revision/latest?cb=20181225172053")
            embed.add_field(
                name='Arcane Acceleration', 
                value='On Critical Hit: 5% / 10% / 15% / 20% chance to give 15% / 30% / 45% / 60% Fire Rate to Primary Weapons for 2 / 3 / 5 / 6 seconds', 
                inline=True
            )
            await message.channel.send(embed=embed)
        
        if 'arcane aegis' in message.content.lower():
            embed=discord.Embed(color=0x5ff1f1)
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/3/3e/ArcaneAegis.png/revision/latest?cb=20181225172055")
            embed.add_field(
                name='Arcane Aegis', 
                value='On Damaged: 2% / 3% / 5% / 6% chance for 15 / 30 / 45 / 60 Shields Regen/sec for 5 / 10 / 15 / 20 Seconds', 
                inline=True
            )
            await message.channel.send(embed=embed)

        if 'arcane agility' in message.content.lower():
            embed=discord.Embed(color=0x5ff1f1)
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/0/0d/ArcaneAgility.png/revision/latest?cb=20181225172056")
            embed.add_field(
                name='Arcane Agility', 
                value='On Damaged: 3% / 6% / 9% / 12% chance for 10% / 20% / 30% / 40% Parkour Velocity for 2 / 4 / 6 / 8 Seconds', 
                inline=True
            )
            await message.channel.send(embed=embed)

        if 'arcane arachne' in message.content.lower():
            embed=discord.Embed(color=0x5ff1f1)
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/4/43/ArcaneArachne.png/revision/latest?cb=20181225172057")
            embed.add_field(
                name='Arcane Arachne', 
                value='On Wall Latch for 2s: 100% chance for 25% / 50% / 75% / 100% Bonus Damage for 5s / 10s / 15s / 20s', 
                inline=True
            )
            await message.channel.send(embed=embed)

        if 'arcane avenger' in message.content.lower():
            embed=discord.Embed(color=0x5ff1f1)
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/a/ab/ArcaneAvenger.png/revision/latest?cb=20181225172059")
            embed.add_field(
                name='Arcane Avenger', 
                value='On Damaged: 4% / 7% / 11% / 14% chance for 7.5% / 15% / 22.5% / 30% Critical Chance for 2 / 4 / 6 / 8 Seconds', 
                inline=True
            )
            await message.channel.send(embed=embed)

        if 'arcane awakening' in message.content.lower():
            embed=discord.Embed(color=0x5ff1f1)
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/warframe/images/a/ae/ArcaneAwakening.png/revision/latest?cb=20181225172058")
            embed.add_field(
                name='Arcane Awakening', 
                value='On Reload: 10% / 20% / 30% / 40% chance for 25% / 50% / 75% / 100% Damage to Pistols for 4 / 8 / 12 / 16 Seconds', 
                inline=True
            )
            await message.channel.send(embed=embed)

        profanity=['fuck', 'shit', 'ass', 'pussy', 'bitch', 'slut']

        def profanity_check(string, _list):
            for items in _list:
                if items in string:
                    return True
            return False

        if profanity_check(message.content.lower(), profanity):
            await message.delete()
            await message.channel.send(f'{message.author.mention} using profanity is prohibited here.', delete_after=7.0)

def setup(bot):
    bot.add_cog(Muhbot(bot))