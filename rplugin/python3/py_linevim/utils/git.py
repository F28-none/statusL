#mengambil nama branch di direktori yg sedang di gunakan
import subprocess
def get_branch_name():
        branch_result = subprocess.run(['git', 'branch'], capture_output=True, text=True)
        branches = branch_result.stdout.splitlines()
        for line in branches:
            if line.startswith('*'):
                return line.strip('* ').strip()
        return False
#mengambil informasi branch yang sedanh di gunakan
def get_branch_info():
        info = subprocess.run(['git', 'status'], capture_output=True, text=True)
        info_file=info.stdout.splitlines()
        for line in info_file:
                if line.__contains__('modified') or 'Untracked'in line:
                        return '⚡'
        return ''
