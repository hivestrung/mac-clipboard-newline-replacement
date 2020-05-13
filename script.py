import subprocess
import sys

class Clipboard:
    def write_to_clipboard(self,output):
        process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(output.encode('utf-8'))
    def read_from_clipboard(self):
        return subprocess.check_output(
            'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
    def removeNewLines(self,s):
        return ' '.join(x for x in s.split('\n'))
    def dewIt(self):
        self.write_to_clipboard(self.removeNewLines(self.read_from_clipboard()))


if __name__ == '__main__':

    C = Clipboard()
    C.dewIt()
