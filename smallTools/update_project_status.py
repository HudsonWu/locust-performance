# -*- coding: utf-8 -*-

import requests


authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM4ZDk4NWUzOTEyNDkzMWI1NTBhY2I2MTE1YTZjMjQxZDlhOWM4Zjk4NDZmYjFhNjRiYWEwM2MwZjMxOGJmYTBmYzY4MjBkNzYyZWFhNjRkIn0.eyJhdWQiOiIyIiwianRpIjoiYzhkOTg1ZTM5MTI0OTMxYjU1MGFjYjYxMTVhNmMyNDFkOWE5YzhmOTg0NmZiMWE2NGJhYTAzYzBmMzE4YmZhMGZjNjgyMGQ3NjJlYWE2NGQiLCJpYXQiOjE1MzE5NjM4NjQsIm5iZiI6MTUzMTk2Mzg2NCwiZXhwIjoxODQ3MzIzODY0LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.iOPJVrKoYqTs55_1rS_OAU5ZlDjoVrvzuBgtY-3QjMKmUARoUOJKuKdgnE1Cmq4gj2jlBi2cuPfStRZEMlEwM7TuCU4PXYSYD4wb5hDDFqvrdgvkc6kPA3cq5bemJKQC6CeTP3PmCQ_ILyATPZAOMsMzThAvh-FCLns5W_82hNG1bn-g410KGAbH_YgiqW6VNzNE0wom4DK7niqsiL8T31mV_-FG2P7r0-lejEXEViOWhAn1zcNmEpMFjPrijfmsfH50BA0WPXP9T3SYxEYlOnD-0zP13RIx4w4NHKOpho-w4udIFmlUBL2TR0CRhN8QeY2zmqGN8uKx7rRyDBiUV-lM3BaQK3L4LAYZQ_lkgTcXnCFlYjN5rZSVxnkUUFMyW4VHUzMVK3VEzTRuYaBQb4nbxYz7zFQPVjg1BRhAVyHmRIi4mnCwMPfiRGXOQxcTfJVZKOW4bFL68Dqp6hzmkdT-iDBzPlxIScXR1tLTUgKA8XMvNHUYZbkgO1E-XHkD2Oc35HxmTC1oP1K_FR_TsNSTy-wKiKXYJ1u5OMU6o8ZAMwnxWs-3q94TC0swh--ktW9GXr_HUIIlSTeE_tBUTkV0vcLFfwTlg789ncVbr-CuP1hTCU27sleacn8SoIx9rLqkobtodTB7Hc2EaHBRL--dRDPcHfDYUQfmbG_9iQM"
headers = {'Accept': "application/json", 'Authorization': authorization}
consulting_id = "omx8kwrgl5aep3nv"

num = 1

while num < 2:
    
    # 获取项目
    r1 = requests.get(headers=headers, \
                      url="http://api.zwphp.test/v1/self/project/list?limit=10&page=1&status=1&consulting_id=%s"% consulting_id)
    if not r1.ok:
        print("r1-status_code: %s"% r1.status_code)
        print(r1.json())
    else:
        receive = r1.json()
        projects = receive['data']
        
        print(u"第 %d 轮项目状态变更: "% num)
        
        i = 4
        
        for project in projects:
            id1 = project['id']
            # 1-未启动  2-进行中  3-暂停  4-已完成  5-终止
            data = {"id": id1, "project_status": i}
            # 更改项目状态
            r3 = requests.put(url="http://api.zwphp.test/v1/project/%s?consulting_id=%s"\
                              % (id1, consulting_id), headers=headers, json=data)
            if not r3.ok:
                print("r3-status:%s"% r3.status_code)
                print(r3.json())
            else:
                print(u"status更改为 %d"% i)
                i = i + 1
                if i > 5:
                    i = 4
        num = num + 1