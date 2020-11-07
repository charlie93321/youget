from com.dxm.normal_tool import gzip_util

if __name__ == '__main__':
    rs = gzip_util.gzip_decode(
        '!H4sIAAAAAAAAAG1Qu27DMAz8FcNzDNhJX86WLR2yNB8gMBJtE6ZEQVbSBkX/vTSKog4aQQNxdzwe+Vm+4YTpgu6YxY7ltqzLVWms+AiZTozmAom0lGCUPFDQShUTMoPSyy6x9hzp1sklidNAMVLol/gU0RKwyeTRdJI8ZGWu+qrDoXKu2O+33qswgh2hR00UMoZZ1HwUI0WYVsVcwQm5sAOkHpPKuzN3xF6Vy2lWWJLpwBNfl1sECfcW+TH55/KbuUvijYOMiq/rpq1q/Q8qOI7nV6dg+7h5bp7al2bOn1CSw7Q02jGL1X539yLy572uq6auNrPPO+VhEHY3d/z6BigSani/AQAA')
    print(rs)
