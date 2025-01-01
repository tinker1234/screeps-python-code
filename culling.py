from defs import *
import config, spawner
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run(creep:Creep, st):
    sp = spawner.Spawner(None)
    count = sp.get_count(creep.memory['role'])
    v = getattr(config, creep.memory['role'])
    if count > len(st) * v:
        if config.cull_overage:
            print(creep.name, 'was culled')
            creep.suicide()
    if config.cull_all:
        print(creep.name, 'was culled')
        creep.suicide()