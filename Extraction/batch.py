from subprocess import call
import os,sys

def create_udb(repo_):
    repo_name = os.path.basename((repo_))
    udb_name = repo_name + '.udb'
    print(repo_name,udb_name)
    call('und create -languages python c++ java ' + udb_name ,shell = True)
    call('und add -db '+ udb_name + ' ' + repo_ ,shell = True)
    call('und analyze -all ' + udb_name, shell = True)
    return udb_name

# python c++ java