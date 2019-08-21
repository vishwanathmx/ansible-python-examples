from ansible.modules.source_control import git

git_remote_http_url = 'https://github.com/vishwanathmx/ansible-playbooks.git'
dest_folder_path = '/home/centos/xpvishwanath/gitFolder1'
version = 'test_br'

try:
    print('Start Git cloning---------------->')

    git.clone(repo=git_remote_http_url,dest=dest_folder_path,version=version,
        separate_git_dir=None,remote=None,bare='no',result=None,verify_commit='no',module=None,
        git_path=None,reference=None,refspec=None,depth=None)

    print('End Git cloning---------------->')
except Exception as e:
    print('Error occured during GIT operation', e)