import sublime
import sublime_plugin
import CloudFormationDebugger.CloudFormationChecker as Checker

class CloudFormationDebuggerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        checker = Checker.CloudFormationChecker(self.view.substr(sublime.Region(0, self.view.size())))
        errorList = checker.errorFound
        # print(errorList)
        sel = [s for s in self.view.sel()]
        print(sel)

        self.view.erase_regions("mark")
        self.view.set_status("status", "")
        mark = list()
        status_message = ""
        if len(errorList) == 0:
            return

        for error in errorList:
            a = error['index']-(error['index'] - self.view.line(sublime.Region(error['index'],error['index'])).a+1)
            mark.append(sublime.Region(a,a))
            # print(error['index'])
            # print(self.view.line(sublime.Region(error['index'],error['index'])).a)
            self.view.add_regions("mark", mark, "mark", "bookmark", sublime.HIDDEN | sublime.PERSISTENT)
            status_message += error['type'] + "at Line {}, Column {}; ".format(error["line"], error["column"])
        self.view.set_status("status", "")
        self.view.set_status("status", status_message)

class HelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello World!\n")

class CloudFormationDebugger(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        # print("checking")
        # print(view.substr(sublime.Region(0, view.size())))
        view.run_command('cloud_formation_debugger')