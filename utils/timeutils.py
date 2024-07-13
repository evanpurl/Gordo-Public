from time import mktime


async def timetounix(inputdate):

    return f'<t:{int(mktime(inputdate.timetuple()))}:R>'
