import requests
url='https://sellercenter.lazada.vn/product/newpublish/api.product.post.render.v1?_timezone=-7&__ARMS_PID__=giiryrcz16@65cb05a587d7ea3&userId=200163978075&optType=selectCategory&productId=947010999&catId=1462',

url='https://sellercenter.lazada.vn/product/newpublish/api.product.post.render.v1?_timezone=-8&__ARMS_PID__=giiryrcz16@65cb05a587d7ea3&userId=200163978075&optType=selectCategory&productId=947090429&catId=1462'
resp = requests.get(
    url=url,
    headers={
        'Cookie':'JSESSIONID=node0kojh0nka36v6sdoovn8y6b4p12309033.node0; c_csrf=480bbd93-376c-4bfd-969c-7b5c326eaf34; JSID=5159634cf32009196d4de37d630288e3; CSRFT=353e571b35f78; TID=42a056f2bddc42fb8037618aeb5d4692; _lang=zh_CN; _bl_uid=kykpOhUj6as05XfeL17kvCmiwj3y; t_fv=1604652081001; t_uid=TQWkq1kR2GHr4gwwiJFsUpiRXYlCGIsP; t_sid=HDMPv2uAxsgKzFLffFbimR6GlzoRwCiM; utm_channel=NA; cna=Af3VFwPuDgYCAbcvMjMMyWDo; _m_h5_tk=046fd108e7d9b61e38934525d4065df5_1604662521999; _m_h5_tk_enc=f89ff784689d94bd38a33c33b3e7dd9b; accountType=phone'
    })


print(resp.text)