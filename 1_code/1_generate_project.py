"""

"""

import os
import sys
import json

home_dir = os.path.isfile('config.json')
dev_dir = os.path.isfile('2_pipeline/0_generate_config_json/out/config.json')

if home_dir:
    config_exists=True
    with open('config.json') as json_config:
        config_data = json.load(json_config)
elif dev_dir:
    config_exists=True
    with open('2_pipeline/0_generate_config_json/out/config.json') as json_config:
        config_data = json.load(json_config)
else:
    config_exists=False
    print('"config.json" not in expected directory.\n Expected either in same directory as script or in development configuration.\n Running on blank config.')


class project_gen:
    def __init__(self, p_name='new_project', f_list=['main_code.py'], dev=False):
        self.project_name=p_name
        self.file_list=f_list
        self.in_development=dev

    def create_folders(self):
        if in_development:
            os.chdir('3_output')
        else:
            if os.path.isdir('python_projects'):
                os.chdir('python_projects')
            else:
                os.mkdir('python_projects')
                os.chdir('python_projects')
        os.mkdir(self.project_name)
        os.chdir(self.project_name)
        os.mkdir('0_data')
        os.mkdir('1_code')
        os.mkdir('2_pipeline')
        os.mkdir('3_output')
        for x in self.file_list:
            i = self.file_list.index(x)
            if x.split('.')[1] == 'ipynb':
                iPy = open(f'1_code/{i}_{x}', 'w+')
                if config_exists:
                    iPy.write(config_data['jup_nb_file'])
                iPy.close()
            # elif (x.split('.')[1] != 'R') or (x.split('.')[1] != 'py'):      # I thought the placeholder might be nice, but having a dummy-file is useful even if it cannot be properly opened: It opens the right program by default...
            #     filetype = x.split('.')[1]
            #     ph = open(f'1_code/{i}_placeholder_{filetype}_file.txt', 'w+')
            #     ph.write(f'Replace with a .{filetype} file.')
            #     ph.close()
            else:
                open(f'1_code/{i}_{x}', 'w+').close()
            folder_name = x.split('.')[0]
            os.mkdir(f'2_pipeline/{i}_{folder_name}')
            for y in ['tmp', 'store', 'out']:
                os.mkdir(f'2_pipeline/{i}_{folder_name}/{y}')

    def create_starting_files(self):
        read_me=open('README.md', 'w+')
        if config_exists:
            read_me.write(config_data['read_me_text'])
        read_me.close()
        structure_explanation=open('structure_README.md', 'w+')
        if config_exists:
            structure_explanation.write(config_data['structure_read_me_text'])
        structure_explanation.close()
        git_ig = open('.gitignore', 'w+')
#        git_ig.write('structure_README.md')        # Not necessary because it is now part of the project.
        git_ig.close()

#    def create_git(self):




if __name__ == '__main__':
    if len(sys.argv) > 2:
        project_name = sys.argv[1]
        if 'dev_mode' in sys.argv[2:]:
            param_list = sys.argv[2:]
            param_list.del('dev_mode')
            PROJ = project_gen(p_name=project_name, f_list=param_list, dev=True)
        else:
            param_list = sys.argv[2:]
            PROJ = project_gen(p_name=project_name, f_list=param_list)
    elif len(sys.argv) == 2:
        if 'dev_mode' == sys.argv[1]:
            PROJ = project_gen(dev=True)
        else:
            PROJ = project_gen(p_name=sys.argv[1])
    else:
        PROJ = project_gen()
    PROJ.create_folders()
    PROJ.create_starting_files()
