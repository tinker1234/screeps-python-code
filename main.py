from roles import *
from defs import *
import config
import culling
from structures import Structures
from spawner import Spawner
from memory import Mem
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')
class Bot:
    def __init__(self):
        self.start = 0
        self.is_sleeping = False
        self.spawner = Spawner(self)
        self.memory = Mem()
    
    def sleep(self, seconds):
        if self.start == 0:
            self.start = Game.time
            self.is_sleeping = True
        if (Game.time - self.start) % 60 == seconds:
            print((Game.time - self.start) % 60)
            self.is_sleeping = False
            self.start = 0
    
    def main(self):
        spawner = self.spawner
        self.memory.clear_unused()
        if config.clear_memory:
            self.memory.clear()
        for name in list(Object.keys(Game.creeps)):
            creep = Game.creeps[name]
            structure = Structures(None, creep)
            st = structure.find_all_spawns()
            if creep.memory['role'] == 'harvester':
                Harvester(creep).run()
            elif creep.memory['role'] == 'upgrader':
                Upgrader(creep).run()
            elif creep.memory['role'] == 'builder':
                Builder(creep).run()
            elif creep.memory['role'] == 'repairer':
                Repair(creep).run()

            
            spawner.spawnPritorize(st)
            culling.run(creep, st)
        if len(Object.keys(Game.creeps)) == 0:
            spawner.spawnPritorize([Game.spawns['Spawn1'], None])
b = Bot()
def main():
    b.main()

if __name__=="__main__":
    module.exports.loop = main()
