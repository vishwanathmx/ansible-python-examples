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


print ('The Start')
loader = DataLoader()

#inventory = InventoryManager(loader=loader, sources='/home/centos/XPPAS/PythonWorkspace/project-lemp/hosts')
inventory = InventoryManager(loader=loader, sources='localhost')
variable_manager = VariableManager(loader=loader, inventory=inventory)
playbook_path = '/home/centos/XPPAS/PythonWorkspace/project-lemp/site.yml'

if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist')
    sys.exit()

Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts',  'connection', 'module_path', 'forks', 'remote_user', 'private_key_file',
                                 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check', 'diff'])
options = Options(listtags=False, listtasks=False, listhosts=False, connection='ssh', module_path=None, forks=100, remote_user='slotlocker', private_key_file=None,
                  ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method='sudo', become_user='root', verbosity=None, check=False, diff=False)

# This can accomodate various other command line arguments.`
#variable_manager.extra_vars = {'hosts': 'webservers'}
#variable_manager._options_vars=options
passwords = {}

play_source = {"name": "Ansible Ad-Hoc", "hosts": "localhost", "gather_facts": "no",
               "tasks": [{"action": {"module": "shell", "args": "ls />>/NINAD2.txt"}}]}

pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory,
                        variable_manager=variable_manager, loader=loader, passwords=passwords)

res = pbex.run()
print(res)
print ('The end')
