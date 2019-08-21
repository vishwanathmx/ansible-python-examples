import ansible_runner
from ansible.parsing.dataloader import DataLoader


loader = DataLoader()

inv = loader.load(str({ "all": { "hosts": "localhost" }}))
inv1 = str({
   "all": {
      "hosts": {
         "10.20.2.98": ''}
   }
})
extravars = {'ansible_connection': 'local'}
extravars1=   {
              'ansible_ssh_common_args':'-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ProxyCommand="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -W %h:%p centos@13.52.102.200"',
              'become':True, 
              'become_method':'sudo',
              'ansible_user':'ubuntu', 
              'become_user':'root'}
with open('/home/centos/poc/abc.pem', 'r') as file:
    ssh_data = file.read()   
         


playbiik_path = '/home/centos/xpvishwanath/ansible-workspace/project-lemp/hello.yml'
r = ansible_runner.run(extravars=extravars1,private_data_dir='/home/centos/xpvishwanath/ansible-workspace', playbook=playbiik_path,
                        inventory=inv1,ssh_key=ssh_data)

print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)