import uuid
import re

def get_uuid():
    '''
    获取32为uuid
    :return:
    '''
    return str(uuid.uuid1()).replace('-','')

def remove_js_css(content):
    """
    #删除web中的head,jss,注释、Css和空行等标签
    """
    r = re.compile(r'''<script.*?</script>''', re.I | re.M | re.S)
    sc = r.sub('', content)
    r = re.compile(r'''<style.*?</style>''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''<!--.*?-->''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    # 这一段保留，要不下载文件后，字符集会出问题
    # r = re.compile(r'''<meta.*?>''', re.I | re.M | re.S)
    # sc = r.sub('', sc)
    # r = re.compile(r'''<a.*?</a>''', re.I | re.M | re.S)
    # sc = r.sub('', sc)
    r = re.compile(r'''<ins.*?</ins>''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''^\s+$''', re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''\n+''', re.M | re.S)
    sc = r.sub('\n', sc)
    ##转化为byte形式存储
    # sc = str.encode(sc)
    # sc = zlib.compress(sc)
    # return sc.strip()
    return sc