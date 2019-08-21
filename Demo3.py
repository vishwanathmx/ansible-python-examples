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

''' Running given playbook on given hosts '''

context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                                module_path=None, forks=100, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method='sudo',
                                become_user='root', verbosity=4, check=False, diff=False, start_at_task=None,
                                tags='test1')
print ('The Start')




#get playbook in json
jsonString = str({"name":"Ansible Ad-Hoc","hosts":"all","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"ls />>/NINAD2.txt"}}]})
jsonString2 = str({"name":"Ansible Ad-Hoc","hosts":"all","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"ls />>/home/centos/xpninad/PythonWorkspace/NINAD2.txt"}}]})
playbook3=str([
	{
		"hosts": "all",
		"become": True,
		"tasks": [
			{
				"name": "Ansible create file if it doesn't exist example",
				"file": {
					"path": "/home/NINAD.txt",
					"state": "touch"
				}
			}
		]
	}
])

#parse it using loader
loader = DataLoader()
play_source=loader.load(playbook3)
print("play_source ",play_source)
#get list of hosts
host_list = ['localhost', '13.52.102.200']
sources = ','.join(host_list)
if len(host_list) == 1:
    sources += ','
#create inventory
inventory = InventoryManager(loader=loader, sources=sources)
#create variable manager
variable_manager = VariableManager(loader=loader, inventory=inventory)
passwords = {}
#Create play
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
# 6.Crete TQM and run play
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


