import config
from defs import *
from structures import Structures
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

class Spawner:
    def __init__(self, bot):
        self.b = bot
        self.spawn = None
        self.builder_called = 0

    def get_count(self, role):
        count = 0
        creeps = [c for c in Object.keys(Game.creeps)]
        for n in creeps:
            creep = Game.creeps[n]
            if creep.memory['role'] == role:
                count += 1
        return count
    
    def repairers(self, st):
        m = {"repairing": False, "role": "repairer"}
        name = m['role'] + Game.time
        for spawn in st:
            if spawn.store.getUsedCapacity(RESOURCE_ENERGY) >= 210:
                if not spawn.spawning:
                    if not self.b.is_sleeping:
                        print("SPAWNING:", name)
                        spawn.createCreep([WORK, CARRY, MOVE], m['role'] + Game.time, m)
                        self.b.sleep(1)
    
    def builders(self, st):
        m = {"building": False, "role": "builder"}
        name = m['role'] + Game.time
        for spawn in st:
            if spawn.store.getUsedCapacity(RESOURCE_ENERGY) >= 210:
                if not spawn.spawning:
                    if not self.b.is_sleeping:
                        print("SPAWNING:", name)
                        spawn.createCreep([WORK, CARRY, MOVE], m['role'] + Game.time, m)
                        self.b.sleep(1)

    def harvesters(self, st):
        m = {"role": 'harvester'}
        name = m['role'] + Game.time
        for spawn in st:
            if spawn.store.getUsedCapacity(RESOURCE_ENERGY) >= 210:
                if not spawn.spawning:
                    if not self.b.is_sleeping:
                        print("SPAWNING:", name)
                        spawn.createCreep([WORK, CARRY, MOVE], m['role'] + Game.time, m)
                        self.b.sleep(1)


    def upgraders(self, st):
        m = {"upgrading": False, "role": 'upgrader'}
        name = m['role'] + Game.time
        for spawn in st:
            if spawn.store.getUsedCapacity(RESOURCE_ENERGY) >= 210:
                if not spawn.spawning: 
                    if not self.b.is_sleeping:
                        print("SPAWNING:", name)
                        spawn.createCreep([WORK, CARRY, MOVE], m['role'] + Game.time, m)
                        self.b.sleep(1)
    
    def healers(self, st):
        m = {"busy": False, "role": 'attack_heal'}
        name = m['role'] + Game.time
        for spawn in st:
            if spawn.store.getUsedCapacity(RESOURCE_ENERGY) >= 300:
                if not spawn.spawning: 
                    if not self.b.is_sleeping:
                        print("SPAWNING:", name)
                        spawn.createCreep([MOVE, HEAL, ATTACK], m['role'] + Game.time, m)
                        self.b.sleep(1)
    
    def spawnPritorize(self, st, creep):
        if creep:
            struct = Structures(None, creep)
        #print(len(st) * getattr(config, config.priortize_order[0]), len(st) * getattr(config, config.priortize_order[1]), len(st) * getattr(config, config.priortize_order[2]))
        if self.get_count(config.priortize_order[0]) < (len(st) * getattr(config, config.priortize_order[0])):
            getattr(self, config.priortize_order[0] + 's')(st)
            #print(config.priortize_order[0] + ':', self.get_count(config.priortize_order[0]))
        elif self.get_count(config.priortize_order[1]) < (len(st) * getattr(config, config.priortize_order[1])):
            getattr(self, config.priortize_order[1] + 's')(st)
            #print(config.priortize_order[1] + ':', self.get_count(config.priortize_order[1]))
        elif self.get_count(config.priortize_order[2]) < (len(st) * getattr(config, config.priortize_order[2])):
            getattr(self, config.priortize_order[2] + 's')(st)
            #print(config.priortize_order[2] + ':', self.get_count(config.priortize_order[2]))
        elif self.get_count(config.priortize_order[3]) < (len(st) * getattr(config, config.priortize_order[3])):
            if creep:
                if struct.targets_need_repair() > 0:
                    getattr(self, config.priortize_order[3] + 's')(st)
                #print(config.priortize_order[3] + ':', self.get_count(config.priortize_order[3]))
        