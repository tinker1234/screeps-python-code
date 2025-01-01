from defs import *
import structures
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

class Mem:
    def clear(self):
        m = Object.keys(Memory.creeps)
        for name in m:
            del Memory.creeps[name]
        for name in Object.keys(Game.creeps):
            creep = Game.creeps[name]
            creep.suicide()
        print("CLEARED ALL", len(m), "CREEPS FROM MEMORY AND KILLED CREEPS")


    def clear_unused(self):
        m = Object.keys(Memory.creeps)
        for name in m:
            if not Game.creeps[name]:
                del Memory.creeps[name]
                print(f"CLEARED {name} FROM MEMORY..")
