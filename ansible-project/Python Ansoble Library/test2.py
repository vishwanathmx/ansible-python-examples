import os
import sys
from collections import namedtuple

 

from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.module_utils.common.collections import ImmutableDict
from ansible import context

loader = DataLoader()
# List of Hosts
host_list =[]
if len(host_list) == 0:
    print("Host list is Empty")
else:
    sources =','.join(host_list)
    if len(host_list) == 1:
        sources += ','
try:
    inventory = InventoryManager(loader=loader, sources=sources)
except NameError:
    print("Host list not defind")
else:
    print(inventory._inventory.hosts)
    print(inventory._inventory.groups)
    
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    playbook_path = '/home/centos/xpjotiram/ansible-project/site.yml'

    if not os.path.exists(playbook_path):
        print('[INFO] The playbook does not exist')
        sys.exit()
    
    context.CLIARGS = ImmutableDict(connection='local', module_path=['/to/mymodules'], forks=10, become=True, become_method='sudo', check=False, diff=False, syntax=False,
    start_at_task=None, verbosity = 4)

    passwords = {}

    pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)

    results = pbex.run()
 