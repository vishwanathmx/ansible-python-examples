#!/usr/bin/env python

import os
import sys
from collections import namedtuple

from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play import Play
from ansible import context

''' This file is to demostrate use of TaskQueManager class '''
print ('The Start')
# 1.create Inventory
# 2.create Variable Manager
# 3.create Loader
# 4.create Passwords
# 5.create Play Object
# 6.crete TQM using above parameters


playbook_path = '/home/centos/xpninad/PythonWorkspace/project-lemp/site.yml'
host_path='/home/centos/xpninad/PythonWorkspace/project-lemp/hosts'
if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist')
    sys.exit()



context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                                module_path=None, forks=100, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method='sudo',
                                become_user='root', verbosity=4, check=False, diff=False, start_at_task=None,
                                tags='test1')




# 1.create Loader
loader = DataLoader()
#loader.load_from_file()
jsonString = str({"name":"Ansible Ad-Hoc","hosts":"localhost","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"ls />>/NINAD2.txt"}}]})
jsonString2 = str({"name":"Ansible Ad-Hoc","hosts":"all","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"ls >>/home/centos/xpninad/PythonWorkspace/NINAD2.txt"}}]})

datafromjson=loader.load(jsonString2)
datafromymlfile=loader.load_from_file(playbook_path)
print("data from file ",datafromymlfile)
# 2.create Inventory
inventory = InventoryManager(loader=loader, sources=host_path)
#inventory2 = InventoryManager(loader=loader, sources='localhost')
# 3.create Variable Manager
variable_manager = VariableManager(loader=loader, inventory=inventory)
# 4.create Passwords
passwords = {}
# 5.Create Play Object
play_source = {"name":"Ansible Ad-Hoc","hosts":"localhost","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"ls />>/NINAD3.txt"}}]}
play = Play().load(datafromymlfile.pop(), variable_manager=variable_manager, loader=loader)
# 6.Crete TQM using above parameters
print ('TQM start')
tqm = None
try:
         tqm = TaskQueueManager(
         inventory=inventory,
         variable_manager=variable_manager,
         loader=loader,
         passwords=None,
         stdout_callback='minimal',
         run_tree=False,
         )
         result = tqm.run(play)
         print (result)
finally:
         if tqm is not None:
             tqm.cleanup() 

print ('The end')


