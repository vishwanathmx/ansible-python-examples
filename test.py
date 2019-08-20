#!/usr/bin/env python

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
inventory = InventoryManager(loader=loader, sources='./inventory',)

variable_manager = VariableManager(loader=loader, inventory=inventory)

playbook_path = '/home/centos/xpshital/runsetup.yml'

if not os.path.exists(playbook_path):
    print('[INFO] The playbook does not exist')
    sys.exit()

#context.CLIARGS = ImmutableDict(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False, syntax=False)

context.CLIARGS = ImmutableDict(syntax=False,connection='ssh',
                                private_key_file=sys.argv[1],
                                ssh_extra_args='-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ProxyCommand="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -W %h:%p centos@13.52.102.200"',
                                become=True, become_method='sudo',remote_user='ubuntu',
                                become_user='root',verbosity=3, start_at_task=None)


passwords = {}

pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)

results = pbex.run()
