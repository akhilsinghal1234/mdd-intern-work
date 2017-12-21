from batch import create_udb
from projectMetrics import projectMetric
from subprocess import call
import git
import sys
import datetime
import os
import shutil
import time

def main():
    git_repo = sys.argv[1]      # git repo is the relative path from the folder
    all_sha1 = []
    sha_dtime = []
    repo = git.Repo(git_repo)

    for commit in repo.iter_commits('master'):        
        sha = commit.hexsha
        get_sha = repo.git.rev_parse(sha)
        all_sha1.append(get_sha)
        sha_dtime.append(datetime.datetime.fromtimestamp(commit.committed_date))
    start_time = time.time()
    print(len(all_sha1))
    exit()
    g = git.Git(git_repo) 

    for i in range(len(all_sha1)):
        sha = all_sha1[i]
        d_time = sha_dtime[i] 
        g.checkout(sha)
        db_name = create_udb(git_repo)
        projectMetric(db_name,sha,d_time)
        call('rm -f ' + db_name)

    print("--- %s minutes ---" % round((time.time() - start_time) / 60,5))

if __name__ == '__main__':
    main()