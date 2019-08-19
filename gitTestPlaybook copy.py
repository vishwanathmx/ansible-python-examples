from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.module_utils.common.collections import ImmutableDict
from ansible import context
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.logdna import CallbackModule
from ResultCallback import ResultCallback1
import json

git_playbook_path = '/home/centos/xpvishwanath/ansible-workspace/project-lemp/gitTest.yml'
playbook_path = '/home/centos/xpvishwanath/gitFolder1/site.yml'

loader = DataLoader()

host_list = ['localhost']
#, '13.52.102.200'
sources = ','.join(host_list)
if len(host_list) == 1:
    sources += ','

inventory = InventoryManager(loader=loader,sources=sources)


variable_manager = VariableManager(loader=loader, inventory=inventory)

passwords = {}

"""
context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                                module_path=None, forks=100, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method='sudo',
                                become_user='root', verbosity=4, check=False, diff=False, start_at_task=None)
"""

context.CLIARGS = ImmutableDict(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='local',
                                forks=100, private_key_file=None, become=True, become_method='sudo', become_user='root',
                                check=False, diff=False)



callback = ResultCallback1()

try:
    executor = PlaybookExecutor(
        playbooks=[git_playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,        
        passwords=passwords)

    #executor._tqm._stdout_callback = callback
    print('------------------->',inventory.get_hosts())
    executor.run()

    print("UP ***********")

    for host, result in callback.host_failed.items():
        print('{0} >>> {1}'.format(host, result._result.keys()))
        for key in result._result.keys():
            print("Key: {0} Val : {1}".format(key, result._result[key]))
        
    print('<-----------------------------Execution completed------------------------>')
except Exception as e:
    print(e)
