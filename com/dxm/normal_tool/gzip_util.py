import gzip

from com.dxm.normal_tool.str_util import is_empty


def gzip_decode(str1:str):
    if is_empty(str1):
        return '请输入非空字符串!!!'
    else:
       return  gzip.decompress(str1.encode("utf-8")).decode("utf-8")