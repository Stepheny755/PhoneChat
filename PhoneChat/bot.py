import discord


class Bot():

    def __init__(self):
        pass

    #TODO: Formatting
    def getChannels(self,client,server):
        temp = []
        s = ""
        desc = "List of Channels in " + str(server)
        embed = discord.Embed(title="Channels", description="desc", color=0x00ff00)
        for channel in server.channels:
            temp.append(channel.name)
            s += channel.name + " \n"
        embed.add_field(name="List", value=s, inline=False)
        return embed

    #def joinVoice(self)
