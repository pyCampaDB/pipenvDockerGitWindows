from subprocess import CalledProcessError, run as runSubprocess
from os import getenv
from requests import post as reqPost, put as reqPut


def git_user_email():
    try:
        email = getenv("GITHUB_EMAIL", default='default_email')
        runSubprocess(f'git config --global user.email "{email}"',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_user_name():
    name = getenv("GITHUB_USERNAME", default='default_name')
    try:
        runSubprocess(f'git config --global user.name "{name}"',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_user_password():
    pwd = getenv("GITHUB_PASSWORD", default='default_password')
    try:
        runSubprocess(f'git config --global user.password "{pwd}"',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_init():
    try:
        runSubprocess(
            'git init', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_rm_cached():
    try:
        file = input('Input the file: ')
        runSubprocess(
            f'git rm --cached {file}',
            check=True,
            shell = True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_commit():
    commit = input('Input the commit message: ')
    try:
        runSubprocess(
            f'git commit -m "{commit}"', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_remote_v():
    try:
        runSubprocess(
            'git remote -v', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_remove():
    remote = input(
        'Input the remote name: '
    )
    try:
        runSubprocess(
            f'git remote remove {remote}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_clone():
    url = input(
        'Input the url of the repository: '
    )
    try:
        runSubprocess(
            f'git clone {url}',
            shell= True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_push():

    remote = input(
        'Input the remote name: '
    )
    branch = input(
        'Input the branch name: '
    )

    first_commit = input('Input if is your first commit [Y/n]: ')
    
    try:
        runSubprocess(
            f'git push {remote} {branch}',
            shell=True,
            check=True
        )
        if first_commit in ['Y, y']:
            my_git = input('Input your repository name: ')
            username = getenv('GITHUB_USERNAME')
            runSubprocess(
                f'git remote add {remote} https://github.com/{username}/{my_git}.git',
                shell=True, check=True, capture_output=True)
            
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_branch():
    try:
        runSubprocess(
            'git branch',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_checkout():
    try:
        branch = input('Input the branch name: ')
        runSubprocess(
            f'git checkout {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_merge():
    try:
        branch = input('Input the branch name: ')
        runSubprocess(
            f'git merge {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_checkout_b():
    try:
        branch = input('Input the branch name: ')
        runSubprocess(
            f'git checkout -b {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_pull(remote=None, branch=None):
    if remote == None:
        remote = input('Input the remote name: ')
    if branch == None:
        branch = input('Input the branch name: ')
    try:
        runSubprocess(
            f'git pull {remote} {branch}',
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_add():
    f = input('Input the file name: ')
    try:
        runSubprocess(
            f'git add {f}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_status():
    try:
        runSubprocess(
            'git status',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_log():
    try:
        runSubprocess(
            'git log', check=True, shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_branch_vv():
    try:
        runSubprocess(
            'git branch -vv',
            check=True,
            shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_config():
    try:
        runSubprocess(
            'git config', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_config_l():
    try:
        runSubprocess(
            'git config -l', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_restore_staged():
    file = input('Input the file name: ')
    try:
        runSubprocess(
            f'git restore --staged {file}', 
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_reset_commit():
    commit = input('Input the HEAD: ')
    try:
        runSubprocess(
            f'git reset {commit}', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_fsck_lost_found():
    try:
        runSubprocess(
            'git fsck --lost-found',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_revert():
    try:
        runSubprocess(
            'git revert HEAD',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_fetch():
    try:
        runSubprocess(
            'git fetch', check=True, shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_diff():
    try:
        runSubprocess(
            'git diff', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_blame():
    file = input(
        'Enter the file name:'
    )
    try:
        runSubprocess(
            f'git blame {file}', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_cherry_pick():
    hash = input('Input the hash commit')
    try:
        runSubprocess(
            f'git cherry-pick {hash}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_reflog():
    try: 
        runSubprocess(
            'git reflog',
            check=True,
            shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_stash():
    try:
        runSubprocess(
            'git stash',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_stash_pop():
    try:
        runSubprocess(
            'git stash pop',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_stash_apply():
    try:
        runSubprocess(
            'git stash apply',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_stash_clear():
    try:
        runSubprocess(
            'git stash clear',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_rebase():
    commit = input('Input the commit or branch: ')
    try:
        runSubprocess(
            f'git rebase {commit}',
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_rebase_abort():
    try:
        runSubprocess(
            'git rebase --abort',
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_rm_file():
    file = input('Input the file name: ')
    try:
        runSubprocess(
            f'git rm {file}', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_branch_d():
    branch = input('Input the branch name: ')
    try:
        runSubprocess(
            f'git branch -d {branch}', 
            check=True, shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_branch_D():
    branch = input('Input the branch name: ')
    try:
        runSubprocess(
            f'git branch -D {branch}', 
            check=True, shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_tag():
    tag = input('Input the tag: ')
    try:
        runSubprocess(
            f'git tag {tag}',
            check=True, shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def create_release():
    owner = getenv('GITHUB_USERNAME')
    repo = input('Input the repository name: ')
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    tag_name = input('Input the tag name: ')
    name = input('Enter the release name: ')
    body = input('Input a description: ')
    target_commitish = input('Input the branch or commit: ')

    payload={
        'tag_name': tag_name,
        'target_commitish': target_commitish,
        'name': name,
        'body': body
    }
    token = getenv('GITHUB_ACCESS_TOKEN')
    response = reqPost(
        url, json=payload,
        headers={'Authorization': f'token {token}'}
    )
    if response.status_code == 201:
        print('\nRelease created successfully!\n')
    else:
        print(f'\nFailed to create release: {response.text}\n')

def create_issue():
    owner = getenv('GITHUB_USERNAME')
    repo = input('Input the repository name: ')
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    title = input('Input the issue title: ')
    body = input('Input a description: ')
    payload = {
        'title': title,
        'body': body
    }
    token = getenv('GITHUB_ACCESS_TOKEN')
    response = reqPost(
        url, 
        json=payload, 
        headers={'Authorization': f'token {token}'}
    )

    if response.status_code == 201:
        print('\nIssue created successfully!\n')
    else:
        print(f'\nFailed to create issue: {response.text}\n')

def create_pull_request():
    owner = getenv('GITHUB_USERNAME')
    repo = input('Input the repository name: ')
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    title = input('Input the pull request title: ')
    body = input('Input a description: ')
    head_branch = input('Input the head branch: ')
    base_branch = input('Input a base branch: ')
    payload = {
        'title': title,
        'head': head_branch,
        'base': base_branch,
        'body': body
    }
    token = getenv('GITHUB_ACCESS_TOKEN')
    response = reqPost(
        url, 
        json=payload, 
        headers={'Authorization': f'token {token}',
                 'Accept': 'application/vnd.github.v3+json'}
    )

    if response.status_code == 201:
        print('\nPull request created successfully!\n')
    else:
        print(f'\nFailed to create pull request: {response.text}\n')

def squash_and_merge():
    owner = getenv('GITHUB_USERNAME')
    repo = input('Input the repository name: ')
    pull_number = input('Input the pull request number: ')
    token = getenv('GITHUB_ACCESS_TOKEN')
    url = f"https://app.github.com/repos/{owner}/{repo}/pulls/{pull_number}/merge"
    commit_title = input('Enter the commit title: ')
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    payload = {
        'commit_title': commit_title,
        'merge_method': 'squash'
    }

    response = reqPut(
        url, headers=headers, json=payload
    )
    if response.status_code == 200:
        print('\nPull request squashed and merged successfully!\n')
    else:
        print(f'\nFailed to squash and merge pull request: {response.text}\n')


##################################################################################################################################################################################################3
def manage_git():
    git_option = '1'
    while git_option in ['1', '2', '3', '4', '5', '6', 
                         '7', '8', '9', '10', '11', '12',
                         '13', '14', '15', '16', '17', '18',
                         '19', '20', '21', '22', '23', '24',
                         '25', '26', '27', '28', '29', '30',
                         '31', '32', '33', '34', '35', '36',
                         '37', '38', '39', '40', '41', '42',
                         '43', '44']:
        git_option = input(
                        '\n******************** GIT ********************\n\n'
                        '1. git init\n'
                        '2. git status\n'
                        '3. git add\n'
                        '4. git commit\n'
                        '5. git push\n'
                        '6. git pull\n'
                        '7. git merge\n'
                        '8. Display the availables local branches of the repository\n'
                        '9. git checkout "branch"\n'
                        '10. git checkout -b "branch"\n'
                        '11.git remote remove "remote"\n'
                        '12.git remote -v\n'
                        '13.git branch -vv\n'
                        '14. git rm --cached "file"\n'
                        '15. git config\n'
                        '16. git config -l\n'
                        '17. git restore --staged "file"\n'
                        '18. git reset --[hard, soft, mixed] "commit"\n'
                        '19. git email\n'
                        '20. git username\n'
                        '21. git password\n'
                        '22. git log\n'
                        '23. git revert\n'
                        '24. git fetch\n'
                        '25. git diff\n'
                        '26. git blame "file"\n'
                        '27. git fsck --lost-found\n'
                        '28. git clone\n'
                        '39. git cherry-pick "hash_commit"\n'
                        '30. git reflog\n'
                        '31. git stash\n'
                        '32. git stash pop\n'
                        '33. git stash apply\n'
                        '34. git stash clear\n'
                        '35. git rebase "..."\n'
                        '36. git rebase --abort\n'
                        '37. git rm file\n'
                        '38. git branch -d "branch"\n'
                        '39. git branch -D "branch"\n'
                        '40. git tag "tag_name"\n'
                        '41. New release\n'
                        '42. New issue\n'
                        '43. New pull request\n'
                        '44. Squash and merge\n'
                        '(Other) Exit GIT\n\n'
                        'Input your choice: '
                    )

        if git_option == '1':git_init()
        elif git_option == '2': git_status()
        elif git_option == '3': git_add()
        elif git_option == '4': git_commit()
        elif git_option == '5': git_push()
        elif git_option == '6': git_pull()
        elif git_option == '7': git_merge()
        elif git_option == '8': git_branch()
        elif git_option == '9': git_checkout()
        elif git_option == '10': git_checkout_b()
        elif git_option == '11':git_remove()
        elif git_option == '12':git_remote_v()
        elif git_option == '13': git_branch_vv()
        elif git_option == '14': git_rm_cached()
        elif git_option == '15': git_config()
        elif git_option == '16': git_config_l()
        elif git_option == '17': git_restore_staged()
        elif git_option == '18': git_reset_commit()
        elif git_option == '19': git_user_email()
        elif git_option == '20': git_user_name()
        elif git_option == '21': git_user_password()
        elif git_option == '22': git_log()
        elif git_option == '23': git_revert()
        elif git_option == '24': git_fetch()
        elif git_option == '25': git_diff()
        elif git_option == '26': git_blame()
        elif git_option == '27': git_fsck_lost_found()
        elif git_option == '28': git_clone()
        elif git_option == '29': git_cherry_pick()
        elif git_option == '30': git_reflog()
        elif git_option == '31': git_stash()
        elif git_option == '32': git_stash_pop()
        elif git_option == '33': git_stash_apply()
        elif git_option == '34': git_stash_clear()
        elif git_option == '35': git_rebase()
        elif git_option == '36': git_rebase_abort()
        elif git_option == '37': git_rm_file()
        elif git_option == '38': git_branch_d()
        elif git_option == '39': git_branch_D()
        elif git_option == '40': git_tag()
        elif git_option == '41': create_release()
        elif git_option == '42': create_issue()
        elif git_option == '43': create_pull_request()
        elif git_option == '44': squash_and_merge()
        else: print('\n******************** EXIT GIT ********************\n\n')

######################################################## COMMENTS ##################################################################################




"""def upload_github():
    try:
        #email = getenv("GITHUB_EMAIL", default='default_email')
        #runSubprocess(f'git config --global user.email "{email}"',
        #              shell=True, check=True)
        #print('\nname')
        #username = getenv("GITHUB_USERNAME", default='default_username')
        #runSubprocess(f'git config --global user.name "{username}"',
        #              shell=True, check=True)
        runSubprocess('git init', shell=True, check=True)
        #print('\nInitializing Github & git status\n')
        runSubprocess('git status', shell=True, check=True)
        f = input("git add... your_file = ")
        runSubprocess(f'git add {f}', shell=True, check=True)
        commit = input('Input commit message: ')
        runSubprocess(f'git commit -m "{commit}"', shell=True, check=True)

        first_upload = ''
        while first_upload not in ['Y', 'y', 'N', 'n']:
            first_upload = input('Input if it is your first commit [Y/N]: ')
            if first_upload not in ['Y', 'y', 'N', 'n']:
                print('\nInvalid option\n')
        branch = 'main'
        remote = 'origin'
        if first_upload in ['Y', 'y']:
            remote = input('Input the remote name: ') #Default: origin
            branch = input('Input your branch: ')
            runSubprocess(f'git branch -M {branch}', shell=True, check=True)           
            my_git = input('Input repository name: ')
            print('\nremote add origin\n')
            runSubprocess(f'git remote add {remote} https://github.com/pyCampaDB/{my_git}.git',
                shell=True, check=True, capture_output=True)
        
        pull = input('Do you want to make a pull? [Y/N]: ')
        if pull in ['Y', 'y']:
            print('\npull\n')
            git_pull(remote, branch)
        print('\npush\n')
        runSubprocess(f'git push -u {remote} {branch}', 
                      shell=True, check=True)
        print('\nProject uploaded to GitHub\n')
    except CalledProcessError as cp:
        print(f'\nCalledProcessError: {cp.returncode}\n')
    except Exception as e:
        print(f'Exeption: {e.__str__}')"""