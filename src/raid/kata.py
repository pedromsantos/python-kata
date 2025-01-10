namespace RaidKata;

class RaidService:
    def get_raids_by_guild_member(self, other):
        player = GuildDao.find_active_player()

        if player is None:
            raise ValueError("Player not found")

        if player in other.get_friends():
            return RaidDao.find_raids_by(other)

        return []

class GuildMember:
    def __init__(self):
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
    def find_active_player():
        raise NotImplementedError("Method not implemented")

class RaidDao:
    @staticmethod
    def find_raids_by(guild_member):
        raise NotImplementedError("Method not implemented")

class Raid:
    pass