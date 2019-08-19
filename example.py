from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.module_utils.common.collections import ImmutableDict
from ansible import context

playbook_path = '/home/centos/XPPAS/PythonWorkspace/project-lemp/site.yml'
host_path='/home/centos/XPPAS/PythonWorkspace/project-lemp/hosts'

loader = DataLoader()

host_list = ['localhost', '13.52.102.200']
#, '13.52.102.200'
sources = ','.join(host_list)
if len(host_list) == 1:
    sources += ','

#inventory1 = InventoryManager(loader=loader,sources=host_list)

inventoryManager2 = InventoryManager(loader=loader, sources="1.1.1.1.1, 12.2.4.5")
#inventoryManager2.add_host('12.12.111.420')

variable_manager = VariableManager(loader=loader, inventory=inventoryManager2)



passwords = {}

# context.CLIARGS = ImmutableDict(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
#       become_method=None, become_user=None, check=False, diff=False, syntax=False)

context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                                module_path=None, forks=100, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method='sudo',
                                become_user='root', verbosity=None, check=False, diff=False)

playbook = PlaybookExecutor(playbooks=[playbook_path], inventory=inventoryManager2,
                            variable_manager=variable_manager,
                            loader=loader, passwords=passwords)
res = playbook.run()

print(res)
print('The End')
