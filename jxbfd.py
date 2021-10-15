# -*- coding: utf-8 -*-
import datetime
import time
from urllib import parse

import requests

cookie = ""
useragent = "jdpingou;iPad;4.9.0;12.2;43ea11349cf97b3fef79a9bfe8672d23b2e70650;network/wifi;model/iPad11,1;appBuild/100567;ADID/4C75127C-E2AE-4256-98EE-AF1B62189651;supportApplePay/1;hasUPPay/0;pushNoticeIsOpen/1;hasOCPay/0;supportBestPay/0;session/120;pap/JA2019_3111789;brand/apple;supportJDSHWK/1;Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
strPhoneID = '43ea11349cf96b3f4f79a9bfe9672d23b2e70650'
strPgUUNum = 'ffe7528423bc7ad1gd185c5f8bd6b17f'

timestamp = int(
    round(
        (datetime.datetime.now() + datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0).timestamp()
    )
    * 1000
)
print(f'下一次整点兑换时间为: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp / 1000))}')
while True:
    if int(round(time.time() * 1000)) >= timestamp:
        timestamp = int(
            round(
                (datetime.datetime.now() + datetime.timedelta(hours=1))
                    .replace(minute=0, second=0, microsecond=0)
                    .timestamp()
            )
            * 1000
        )
        headers = {
            "Host": "m.jingxi.com",
            "Cookie": cookie,
            "accept": "*/*",
            "accept-language": "zh-CN,zh-Hans;q=0.9",
            "referer": "https://st.jingxi.com/fortune_island/index2.html?ptag=7155.9.47",
            "User-Agent": useragent
        }
        url = 'https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&' \
              'bizCode=jxbfd&' \
              'source=jxbfd&' \
              'dwEnv=7&' \
              f'_cfd_t={timestamp}&' \
              'ptag=7155.9.47&' \
              'dwType=3&' \
              'dwLvl=3&' \
              'ddwPaperMoney=100000&' \
              'strPoolName=jxcfd2_exchange_hb_202110&' \
              f'strPgtimestamp={timestamp}&' \
              f'strPhoneID={strPhoneID}&' \
              f'strPgUUNum={strPgUUNum}&' \
              '_stk=_cfd_t%2CbizCode%2CddwPaperMoney%2CdwEnv%2CdwLvl%2CdwType%2Cptag%2Csource%2CstrPgUUNum%2CstrPgtimestamp%2CstrPhoneID%2CstrPoolName%2CstrZone&' \
              '_ste=1&' \
              'h5st=20210831155019626%3B0696188391171162%3B10032%3Btk01wbb571ceb30nxNlPVr%2FhYoGp9Ucs0oo%2BBNpXVETMdFjGbI1Z%2FMYmQah7jQvvvQB7rzFVzlmKo2qeJNz%2FIdmnDu1v%3B31b551902066d81fbf5d3b13f5a5f17f669c746a5083b6916cf7b81e0e33ee7f' \
              f'&_={timestamp}&' \
              'sceneval=2&' \
              'g_login_type=1&' \
              'callback=jsonpCBKL&' \
              'g_ty=ls'

        response = requests.get(url=url, headers=headers)
        print(response.text)
        print(f'下一次整点兑换时间为: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp / 1000))}')
    else:
        time.sleep(0.3)
