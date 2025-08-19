from typing import Never


class RaidService:
    def get_raids_by_guild_member(self, other):
        player = GuildDao.find_active_player()

        if player is None:
            msg = "Player not found"
            raise ValueError(msg)

        if player in other.get_friends():
            return RaidDao.find_raids_by(other)

        return []


class GuildMember:
    def __init__(self) -> None:
        self.raids = []
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, member):
        self.friends.append(member)

    def add_raid(self, raid):
        self.raids.append(raid)

    def get_raids(self):
        return self.raids


class GuildDao:
    @staticmethod
    def find_active_player() -> Never:
        msg = "Method not implemented"
        raise NotImplementedError(msg)


class RaidDao:
    @staticmethod
    def find_raids_by(guild_member) -> Never:
        msg = "Method not implemented"
        raise NotImplementedError(msg)


class Raid:
    pass
