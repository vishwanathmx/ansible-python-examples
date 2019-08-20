import os
import sys
import json
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play import Play


print ('The Start')

loader = DataLoader()


""" Creates and manages inventory
    required parameter: loader : sources
 """

# Way 1
ips =['127.0.0.2','127.0.0.7']
#inventory = InventoryManager(loader=loader, sources=','.join(ips))

# Way 2

#inventory =InventoryManager(loader=loader,sources='localhost,127.0.0.2')
#inventory.add_host("127.28.23.09")
#inventory.add_group(ips)
#print(inventory._inventory.hosts)


# Way 3
#inventory = InventoryManager(loader=loader, sources='/home/centos/xpjotiram/ansible-project/hosts')

# way 4
#inventory = InventoryManager(loader, sources="127.0.0.1")

# Way 5
host_list =['127.0.0.2','127.0.0.3']

sources =','.join(host_list)
if len(host_list) == 1:
    sources += ','

inventory = InventoryManager(loader=loader, sources=sources)

print(inventory._inventory.hosts)

variable_manager = VariableManager(loader=loader, inventory=inventory)

playbook_path = '/home/centos/xpjotiram/ansible-project/site.yml'

if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist')
    sys.exit()

Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection', 'module_path', 'forks', 'remote_user', 'private_key_file',
                                'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check', 'diff'])
options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='slotlocker', private_key_file=None,
                 ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method='sudo', become_user='root', verbosity=None, check=False, diff=False)

# This can accomodate various other command line arguments.`
#variable_manager.extra_vars = {'hosts': 'webservers'}
#variable_manager._options_vars=options
passwords = {}


play = Play().load(playbook_path, variable_manager=variable_manager, loader=loader)

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