from ansible.plugins.callback import CallbackBase

class ResultCallback1(CallbackBase):
    
    def __init__(self, *args, **kwargs):
        super(ResultCallback1, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}
        self.on_play_start = {}
        self.on_play_stats = {}

    def v2_runner_on_ok(self, result, **kwargs):
        print("Inside v2_runner_on_ok()")
        host = result._host
        self.host_ok[result._host.get_name()] = result
        #print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_on_unreachable(self, result):
        host = result._host
        print("Inside v2_runner_on_unreachable()")
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        host = result._host
        print("Inside v2_runner_on_failed()")
        self.host_failed[result._host.get_name()] = result

    def v2_playbook_on_play_start(self, play):
        print('v2_playbook_on_play_start',play)

    def v2_playbook_on_stats(self, stats):
        print('v2_playbook_on_stats',stats.processed,stats.ignored,stats.rescued,stats.skipped,stats.changed,stats.dark,stats.failures,stats.processed,stats.ok)
    
    # FIXME: not called
    def v2_playbook_on_cleanup_task_start(self, task):
        print('v2_playbook_on_cleanup_task_start',task)

    def v2_playbook_on_handler_task_start(self, task):
        print('v2_playbook_on_handler_task_start',task)


# Create a callback object so we can capture the output
class ResultsCollector(CallbackBase):

    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        for res in result._result:
            print(res)
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        for res in result._result:
            print(res)
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        for res in result._result:
            print(res)
        self.host_failed[result._host.get_name()] = result


# Create a callback object so we can capture the output
class ResultsCollector1(CallbackBase):

    def __init__(self, *args, **kwargs):
        super(ResultsCollector1, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        print("v2_runner_on_unreachable",result._task, result._host)   
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        print("v2_runner_on_ok",result._task, result._host)        
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs): 
        print("v2_runner_on_failed",result._task, result._host)       
        self.host_failed[result._host.get_name()] = result        