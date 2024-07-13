import discord


async def user_welcome_embed(user, server):
    embed = discord.Embed(title=f"**Welcome in {user.name}!**",
                          description=f"*Croak* <:GordoBeanie:1185829164020936776> Welcome to {server.name} {user.mention}! Please make sure "
                                      f"to review the rules! This server has {len([m for m in server.members if not m.bot])} members!",
                          color=discord.Color.green())
    embed.set_thumbnail(url=user.display_avatar.url)
    return embed


async def user_goodbye_embed(user, server):
    embed = discord.Embed(title="**Goodbye**",
                          description=f"*Sad ribbit* <:GordoBeanie:1185829164020936776> Goodbye {user.name}.",
                          color=discord.Color.green())
    embed.set_thumbnail(url=server.icon.url)
    return embed


async def command_center_embed(bot, user):
    embed = discord.Embed(title="**Command Center**",
                          description=f"*Happy Ribbit* <:GordoBeanie:1185829164020936776> Welcome to the Command Center {user.mention}! Here you can toggle my features on and off!\n\n All options are off when you first invite the me to your server!",
                          color=discord.Color.green())
    embed.set_thumbnail(url=bot.user.avatar.url)
    return embed


async def user_warning_embed(user, reasons):
    embed = discord.Embed(title=f"**{user.name}'s Warnings**",
                          color=discord.Color.green())
    embed.set_thumbnail(url=user.guild.icon.url)
    if len(reasons) > 25:
        embed.add_field(name=f"Warning Message",
                        value=f"The number of warnings that you gave this member exceeds 25, which is the max number of fields that discord allows in an embed.")
        return embed
    for index, value in enumerate(reasons):
        embed.add_field(name=f"Warning {index + 1}", value=value[0])
    return embed


async def user_warned_embed(user, reason, number):
    embed = discord.Embed(title=f"**{user.guild.name} Warning**",
                          color=discord.Color.green())
    embed.set_thumbnail(url=user.guild.icon.url)
    embed.add_field(name=f"Reason for warning", value=reason)
    if number:
        embed.add_field(name=f"Warning Number", value=number)
    return embed


async def log_embed(logname, logdata, bot):
    embed = discord.Embed(
        title=f"{logname}", color=discord.Color.green())
    for index, value in enumerate(logdata):
        embed.add_field(name=logdata[index][0], value=logdata[index][1])
    embed.set_thumbnail(url=bot.user.avatar)
    return embed
