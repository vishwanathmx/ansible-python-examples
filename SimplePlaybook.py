from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.module_utils.common.collections import ImmutableDict
from ansible import context

playbook_path = '/home/centos/xpvishwanath/ansible-workspace/project-lemp/test.yml'

loader = DataLoader()

inventory = InventoryManager(loader=loader, sources='localhost')
variable_manager = VariableManager(loader=loader, inventory=inventory)

passwords = {}

# context.CLIARGS = ImmutableDict(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
#       become_method=None, become_user=None, check=False, diff=False, syntax=False)

context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                                module_path=None, forks=100, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method='sudo',
                                become_user='root', verbosity=None, check=False, diff=False, start_at_task=None,
                                tags='test1')

playbook = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory,
                            variable_manager=variable_manager,
                            loader=loader, passwords=passwords)
res = playbook.run()

print(res)
print('The End')
