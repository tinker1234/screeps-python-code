from defs import *
import structures
import config

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

class Harvester:
    def __init__(self, creep: Creep):
        self.creep = creep
        self.structure = structures.Structures(None, creep)
    
    def run(self):
        creep = self.creep
        if creep.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
            if config.creep_say: creep.say("Harvest..")
            source = self.creep.pos.findClosestByPath(FIND_SOURCES)
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)
        else:
            for target in self.structure.targets_need_filling():
                if config.creep_say: creep.say(f"filling {target.name}...")
                if creep.transfer(target, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                    creep.moveTo(target)


class Upgrader:
    def __init__(self, creep: Creep):
        self.creep = creep
        self.structure = structures.Structures(None, creep)
    
    def run(self):
        creep = self.creep
        if creep.memory.upgrading and creep.store[RESOURCE_ENERGY] == 0:
            creep.memory.upgrading = False
        if not creep.memory.upgrading and creep.store.getFreeCapacity(RESOURCE_ENERGY) == 0:
            creep.memory.upgrading = True
        if creep.memory.upgrading and creep.room.controller:
            if config.creep_say: creep.say("upgrading..")
            if creep.upgradeController(creep.room.controller) == ERR_NOT_IN_RANGE:
                creep.moveTo(creep.room.controller)
        else:
            if config.creep_say: creep.say("Harvest..")
            source = creep.pos.findClosestByPath(FIND_SOURCES)
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)

class Builder:
    def __init__(self, creep: Creep):
        self.creep = creep
        self.structure = structures.Structures(None, creep)
    
    def run(self):
        creep = self.creep
        if creep.memory.building and creep.store[RESOURCE_ENERGY] == 0:
            creep.memory.building = False
        if not creep.memory.building and creep.store.getFreeCapacity(RESOURCE_ENERGY) == 0:
            creep.memory.building = True
        if creep.memory.building:
            targets = creep.room.find(FIND_CONSTRUCTION_SITES)
            if config.creep_say: creep.say("building..")
            if len(targets):
                if creep.build(targets[0]) == ERR_NOT_IN_RANGE:
                    creep.moveTo(targets[0])

        else:
            if config.creep_say: creep.say("Harvest..")
            source = creep.pos.findClosestByPath(FIND_SOURCES)
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)

class Repair:
    def __init__(self, creep: Creep):
        self.creep = creep
        self.structure = structures.Structures(None, creep)
    
    def run(self):    
        creep = self.creep
        st = self.structure
        if creep.store[RESOURCE_ENERGY] == 0:
            creep.memory.repairing = False
        if not creep.memory.repairing and creep.store.getFreeCapacity(RESOURCE_ENERGY) == 0:
            creep.memory.repairing = True
        if creep.memory.repairing:
            targets = st.targets_need_repair()
            if len(targets) > 0:
                if config.creep_say: creep.say("repairing...")
                target = targets[0]
                if creep.repair(target) == ERR_NOT_IN_RANGE:
                    creep.moveTo(target)
        else:
            if config.creep_say: creep.say("harvesting...")
            source = creep.pos.findClosestByPath(FIND_SOURCES)
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)
class Healer:
    def __init__(self, creep: Creep):
        self.creep = creep

    def get_targets(self):
        return filter(lambda creep: creep.hits < (creep.hitsMax/4), self.creep.room.find(FIND_MY_CREEPS))
    
    def targets_in_range(self):
        targets = self.get_targets()
        inRange = []
        for target in targets:
            if self.creep.heal(target) != ERR_NOT_IN_RANGE:
                inRange.append(target)
        return inRange


    def run(self):
        creep = self.creep
        targets = self.targets_in_range()
        if len(targets) > 0:
            if config.creep_say: creep.say("healing...")
            creep.memory.busy = True
            target = targets[0]
            if target.hits == target.hitsMax:
                creep.memory.busy = False
            if creep.heal(target) == ERR_NOT_IN_RANGE:
                creep.moveTo(target)
        else:
            targets = self.get_targets()
            if len(targets) > 0:
                if creep.heal(targets[0]) == ERR_NOT_IN_RANGE:
                    creep.moveTo(target[0])

class Attaker:
    def __init__(self, creep: Creep):
        self.creep = creep
    
    def get_targets(self)
        targets = self.creep.room.find(FIND_HOSTILE_CREEPS)
        if len(targets) > 0:
            return targets