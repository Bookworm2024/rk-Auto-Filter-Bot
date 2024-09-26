from motor.motor_asyncio import AsyncIOMotorClient
from info import (
    DATABASE_NAME_SECOND,
    DATABASE_URL_SECOND,
    IMDB_TEMPLATE,
    WELCOME_TEXT,
    AUTH_CHANNEL,
    LINK_MODE,
    TUTORIAL,
    SHORTLINK_URL,
    SHORTLINK_API,
    SHORTLINK,
    FILE_CAPTION,
    IMDB,
    WELCOME,
    SPELL_CHECK,
    PROTECT_CONTENT,
    AUTO_FILTER,
    AUTO_DELETE,
    IS_STREAM,
)
import time
import datetime

second_client = AsyncIOMotorClient(DATABASE_NAME_SECOND)
second_mydb = second_client[DATABASE_NAME_SECOND]


class SecondDatabase:
    default_setgs = {
        "auto_filter": AUTO_FILTER,
        "file_secure": PROTECT_CONTENT,
        "imdb": IMDB,
        "spell_check": SPELL_CHECK,
        "auto_delete": AUTO_DELETE,
        "welcome": WELCOME,
        "welcome_text": WELCOME_TEXT,
        "template": IMDB_TEMPLATE,
        "caption": FILE_CAPTION,
        "url": SHORTLINK_URL,
        "api": SHORTLINK_API,
        "shortlink": SHORTLINK,
        "tutorial": TUTORIAL,
        "links": LINK_MODE,
        "fsub": AUTH_CHANNEL,
        "is_stream": IS_STREAM,
    }

    default_verify = {
        "is_verified": False,
        "verified_time": 0,
        "verify_token": "",
        "link": "",
    }

    def __init__(self):
        self.col = second_mydb.Users
        self.grp = second_mydb.Groups
        self.users = second_mydb.uersz

    def new_user_second_db(self, id, name):
        return dict(
            id=id,
            name=name,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
            verify_status=self.default_verify,
        )

    def new_group_second_db(self, id, title):
        return dict(
            id=id,
            title=title,
            chat_status=dict(
                is_disabled=False,
                reason="",
            ),
            settings=self.default_setgs,
        )

    async def add_user_second_db(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)

    async def is_user_exist_second_db(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count_second_db(self):
        count = await self.col.count_documents({})
        return count

    async def remove_ban_second_db(self, id):
        ban_status = dict(is_banned=False, ban_reason="")
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def ban_user_second_db(self, user_id, ban_reason="No Reason"):
        ban_status = dict(is_banned=True, ban_reason=ban_reason)
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status_second_db(self, id):
        default = dict(is_banned=False, ban_reason="")
        user = await self.col.find_one({"id": int(id)})
        if not user:
            return default
        return user.get("ban_status", default)

    async def get_all_users_second_db(self):
        return self.col.find({})

    async def delete_user_second_db(self, user_id):
        await self.col.delete_many({"id": int(user_id)})

    async def delete_chat_second_db(self, grp_id):
        await self.grp.delete_many({"id": int(grp_id)})

    async def get_banned_second_db(self):
        users = self.col.find({"ban_status.is_banned": True})
        chats = self.grp.find({"chat_status.is_disabled": True})
        b_chats = [chat["id"] async for chat in chats]
        b_users = [user["id"] async for user in users]
        return b_users, b_chats

    async def add_chat_second_db(self, chat, title):
        chat = self.new_group(chat, title)
        await self.grp.insert_one(chat)

    async def get_chat_second_db(self, chat):
        chat = await self.grp.find_one({"id": int(chat)})
        return False if not chat else chat.get("chat_status")

    async def re_enable_chat_second_db(self, id):
        chat_status = dict(
            is_disabled=False,
            reason="",
        )
        await self.grp.update_one(
            {"id": int(id)}, {"$set": {"chat_status": chat_status}}
        )

    async def update_settings_second_db(self, id, settings):
        await self.grp.update_one({"id": int(id)}, {"$set": {"settings": settings}})

    async def get_settings_second_db(self, id):
        chat = await self.grp.find_one({"id": int(id)})
        if chat:
            return chat.get("settings", self.default_setgs)
        return self.default_setgs

    async def disable_chat_second_db(self, chat, reason="No Reason"):
        chat_status = dict(
            is_disabled=True,
            reason=reason,
        )
        await self.grp.update_one(
            {"id": int(chat)}, {"$set": {"chat_status": chat_status}}
        )

    async def get_verify_status_second_db(self, user_id):
        user = await self.col.find_one({"id": int(user_id)})
        if user:
            return user.get("verify_status", self.default_verify)
        return self.default_verify

    async def update_verify_status_second_db(self, user_id, verify):
        await self.col.update_one(
            {"id": int(user_id)}, {"$set": {"verify_status": verify}}
        )

    async def total_chat_count_second_db(self):
        count = await self.grp.count_documents({})
        return count

    async def get_all_chats_second_db(self):
        return self.grp.find({})

    async def get_db_size_second_db(self):
        return (await mydb.command("dbstats"))["dataSize"]

    async def get_user_second_db(self, user_id):
        user_data = await self.users.find_one({"id": user_id})
        return user_data

    async def update_user_second_db(self, user_data):
        await self.users.update_one(
            {"id": user_data["id"]}, {"$set": user_data}, upsert=True
        )

    async def has_premium_access_second_db(self, user_id):
        user_data = await self.get_user(user_id)
        if user_data:
            expiry_time = user_data.get("expiry_time")
            if expiry_time is None:
                # User previously used the free trial, but it has ended.
                return False
            elif (
                isinstance(expiry_time, datetime.datetime)
                and datetime.datetime.now() <= expiry_time
            ):
                return True
            else:
                await self.users.update_one(
                    {"id": user_id}, {"$set": {"expiry_time": None}}
                )
        return False

    async def check_remaining_uasge_second_db(self, userid):
        user_id = userid
        user_data = await self.get_user(user_id)
        expiry_time = user_data.get("expiry_time")
        # Calculate remaining time
        remaining_time = expiry_time - datetime.datetime.now()
        return remaining_time

    async def get_free_trial_status_second_db(self, user_id):
        user_data = await self.get_user(user_id)
        if user_data:
            return user_data.get("has_free_trial", False)
        return False

    async def give_free_trail_second_db(self, userid):
        user_id = userid
        seconds = 5 * 60
        expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        user_data = {"id": user_id, "expiry_time": expiry_time, "has_free_trial": True}
        await self.users.update_one({"id": user_id}, {"$set": user_data}, upsert=True)


second_db = SecondDatabase()
