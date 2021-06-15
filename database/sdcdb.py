# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

db_y = db_x["D_CMDS"]


async def add_cmd(cmd_name):
    cd = await db_y.find_one({"_id": "DISABLED_CMDS"})
    if cd:
        await db_y.update_one({"_id": "DISABLED_CMDS"}, {"$push": {"cmd_name": str(cmd_name)}})
    elif not cd:
        cmd_namec = [str(cmd_name)]
        await db_y.insert_one({"_id": "DISABLED_CMDS", "cmd_name": cmd_namec})


async def rm_cmd(cmd_name):
    await db_y.update_one({"_id": "DISABLED_CMDS"}, {"$pull": {"cmd_name": str(cmd_name)}})


async def is_cmd_in_db(cmd_name):
    sm = await db_y.find_one({"_id": "DISABLED_CMDS"})
    if sm:
        kek = list(sm.get("cmd_name"))
        if cmd_name in kek:
            return True
        else:
            return False
    else:
        return False


async def disabled_cmd_list():
    sm = await db_y.find_one({"_id": "DISABLED_CMDS"})
    if sm:
        return [str(i) for i in sm.get("cmd_name")]
    else:
        return []
