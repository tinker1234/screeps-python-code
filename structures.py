from defs import *
from typing import Any
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

class Structures:
    def __init__(self, type: Any, creep: Creep):
        self.type = type
        self.creep = creep
    
    def find_structure(self):
        target = filter(lambda s: [self.type].includes(s.structureType), self.creep.room.find(FIND_STRUCTURES))
        return target
     
    def find_all_spawns(self):
        targets = filter(lambda s: [STRUCTURE_SPAWN].includes(s.structureType), self.creep.room.find(FIND_STRUCTURES))
        return targets
    
    def targets_need_filling(self):
        targets = filter(lambda s: [STRUCTURE_EXTENSION, STRUCTURE_SPAWN, STRUCTURE_STORAGE, STRUCTURE_TOWER].includes(s.structureType) and s.store.getFreeCapacity(RESOURCE_ENERGY) > 0, self.creep.room.find(FIND_STRUCTURES))
        return targets
    
    def find_controller(self):
        target = filter(lambda c: [STRUCTURE_CONTROLLER].includes(c.structureType), self.creep.room.find(FIND_STRUCTURES))
        return target
    
    def targets_need_repair(self):
        targets = filter(lambda obj: obj.hits < (obj.hitsMax/4), self.creep.room.find(FIND_MY_STRUCTURES))
        return targets 