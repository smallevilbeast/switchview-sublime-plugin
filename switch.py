import sublime_plugin                

class SwitchviewCommand(sublime_plugin.WindowCommand):
    
    def run(self, **args):
        direction = args.get('direction', 'left')
        if direction == "left":
            index = self.get_left_index()
        else:    
            index = self.get_right_index()
        param = dict(index=index)
        self.window.run_command('select_by_index', param)
        
    @property    
    def current_index(self):
        try:
            return self.window.get_view_index(self.window.active_view())[-1]
        except: return 0
        
    @property    
    def num_views(self):
        return len(self.window.views())
    
    def get_left_index(self):
        index = self.current_index - 1
        if index < 0:
            return self.num_views - 1
        return index
    
    def get_right_index(self):
        index = self.current_index + 1
        if index > self.num_views - 1:
            return 0
        return index
