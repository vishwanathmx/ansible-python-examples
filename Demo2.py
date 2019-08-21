#!/usr/bin/env python

import os
import sys
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play import Play
from ansible.module_utils.common.collections import ImmutableDict
from ansible import context

'''This file is to demostrate use of PlayBookExecutor class'''


print ('The Start')

# 1.create Inventory
# 2.create Variable Manager
# 3.create Loader
# 4.create Passwords
# 5.create Play Object
# 6.crete PlaybookExecutor using above parameters
loader = DataLoader()

#inventory = InventoryManager(loader=loader, sources='/home/centos/XPPAS/PythonWorkspace/project-lemp/hosts')
inventory = InventoryManager(loader=loader, sources='localhost')
variable_manager = VariableManager(loader=loader, inventory=inventory)
playbook_path = '/home/centos/XPPAS/PythonWorkspace/project-lemp/site.yml'

if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist')
    sys.exit()

# This can accomodate various other command line arguments.`
#variable_manager.extra_vars = {'hosts': 'webservers'}
#variable_manager._options_vars=options
passwords = {}

#play_source = {"name": "Ansible Ad-Hoc", "hosts": "localhost", "gather_facts": "no","tasks": [{"action": {"module": "shell", "args": "ls />>/NINAD2.txt"}}]}


context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                                module_path=None, forks=100, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method='sudo',
                                become_user='root', verbosity=None, check=False, diff=False, start_at_task=None,
                                tags='test1')

pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory,
                        variable_manager=variable_manager, loader=loader, passwords=passwords)
print ('Running Playbook')
res = pbex.run()
print(res)
print ('The end')