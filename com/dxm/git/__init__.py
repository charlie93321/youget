import git


r = git.Git(r"E:\charliespace\git\bigseller")


class BranchInfo:
    current_branch = None
    other_branch_local = []
    other_branch_online = []
    branch_size = 0

    def __init__(self):
        self.branch_size = 0

    def current_branch(self, curbranch):
        self.current_branch = curbranch

    def append_branch(self, branch):
        if branch.startswith("remotes"):
            newbranch = branch.replace("remotes/origin/", "")
            if self.find_branch(newbranch):
                self.other_branch_online.append(branch.replace("remotes/",""))
        else:
            self.other_branch_local.append(branch)

    def find_branch(self, newbranch):
        for b in self.other_branch_local:
            if newbranch == b:
                return True
        if newbranch == self.current_branch:
            return True
        return False
    def print_branches(self):
        print("*{}".format(self.current_branch))
        for branch in self.other_branch_local:
            print(" {}".format(branch))
        for branch in self.other_branch_online:
            print(" {}".format(branch))

def look_local_branch():
    rs = r.execute('git branch')
    return rs


def look_all_branch():
    rs = r.execute('git branch -avv')
    return rs


def look_local_online_branch():
    rs = r.execute('git branch -avv')
    branchInfo = BranchInfo()
    for line in rs.strip().split("\n"):
        if line.startswith("*"):
            branchInfo.current_branch(line.split(" ")[1])
        else:
            branch = line.strip().split(" ")[0]
            branchInfo.append_branch(branch)
    return branchInfo

branchs = look_local_online_branch()

#branchs.print_branches()
'''
r.execute('git branch -d {}'.format('wip-generateInventorySku-hzf'))
r.execute('git branch -r -d  origin/wip-draftbatchSaveAndPublish-zxy')
r.execute('git push origin :{}'.format('wip-draftbatchSaveAndPublish-zxy'))



wip-batchEditSendoProduct-zxy                    
wip-shopeeMyExpressPrintLable-zxy                 
wip-shopeeMyPoslajuQrcode-zxy                    
  '''
branch_del='wip-shopeeMyExpressPrintLable-zxy'
#r.execute('git branch -d {}'.format(branch_del))
#r.execute('git push origin --delete  {}'.format(branch_del))
#print(look_all_branch())

bs = look_all_branch()
for line in  bs.split("\n"):
    if '-zxy' in line:
        print(line)


