import os
import sys

playbook_path = '/home/centos/XPPAS/PythonWorkspace/project-lemp/site.yml'
if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist')
    sys.exit()
