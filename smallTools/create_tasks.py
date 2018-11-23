# -*- coding: utf-8 -*-

import requests

authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM4ZDk4NWUzOTEyNDkzMWI1NTBhY2I2MTE1YTZjMjQxZDlhOWM4Zjk4NDZmYjFhNjRiYWEwM2MwZjMxOGJmYTBmYzY4MjBkNzYyZWFhNjRkIn0.eyJhdWQiOiIyIiwianRpIjoiYzhkOTg1ZTM5MTI0OTMxYjU1MGFjYjYxMTVhNmMyNDFkOWE5YzhmOTg0NmZiMWE2NGJhYTAzYzBmMzE4YmZhMGZjNjgyMGQ3NjJlYWE2NGQiLCJpYXQiOjE1MzE5NjM4NjQsIm5iZiI6MTUzMTk2Mzg2NCwiZXhwIjoxODQ3MzIzODY0LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.iOPJVrKoYqTs55_1rS_OAU5ZlDjoVrvzuBgtY-3QjMKmUARoUOJKuKdgnE1Cmq4gj2jlBi2cuPfStRZEMlEwM7TuCU4PXYSYD4wb5hDDFqvrdgvkc6kPA3cq5bemJKQC6CeTP3PmCQ_ILyATPZAOMsMzThAvh-FCLns5W_82hNG1bn-g410KGAbH_YgiqW6VNzNE0wom4DK7niqsiL8T31mV_-FG2P7r0-lejEXEViOWhAn1zcNmEpMFjPrijfmsfH50BA0WPXP9T3SYxEYlOnD-0zP13RIx4w4NHKOpho-w4udIFmlUBL2TR0CRhN8QeY2zmqGN8uKx7rRyDBiUV-lM3BaQK3L4LAYZQ_lkgTcXnCFlYjN5rZSVxnkUUFMyW4VHUzMVK3VEzTRuYaBQb4nbxYz7zFQPVjg1BRhAVyHmRIi4mnCwMPfiRGXOQxcTfJVZKOW4bFL68Dqp6hzmkdT-iDBzPlxIScXR1tLTUgKA8XMvNHUYZbkgO1E-XHkD2Oc35HxmTC1oP1K_FR_TsNSTy-wKiKXYJ1u5OMU6o8ZAMwnxWs-3q94TC0swh--ktW9GXr_HUIIlSTeE_tBUTkV0vcLFfwTlg789ncVbr-CuP1hTCU27sleacn8SoIx9rLqkobtodTB7Hc2EaHBRL--dRDPcHfDYUQfmbG_9iQM"
headers = {'Accept': "application/json", 'Authorization': authorization}
consulting_id = "omx8kwrgl5aep3nv"

project_id = "mx8kwrgdokraep3n"
# 2-收集资料  3-现场勘查  12-采集样本 13-样本接收  4-编制评价报告
types = [12, 13]

num = 1

while num < 2:
    print(u"开始第%d个阶段任务的创建"% num)
    # 获取项目
    r1 = requests.get(headers=headers, \
                      url="http://api.zwphp.test/v1/self/project/list?limit=10&page=1&project_search=公司&consulting_id=%s" \
                      % consulting_id)
    if not r1.ok:
        print("r1-status_code: %s"% r1.status_code)
        print(r1.json())
    else:
        i = 0
        receive = r1.json()
        projects = receive['data']
        for project in projects:
            project_id = project['id']
            type1 = types[i]
            # 创建任务
            post_data = {"project_id":project_id,"start_time":"2018-07-18","end_time":"2018-07-20", \
             "executor_ids":["lw7ykqr4plr6ob84"],"description":"222", \
             "edition":"","editions":[],"signature":"","type":type1} 
            r2 = requests.post(headers=headers, json=post_data, \
                               url="http://api.zwphp.test/v1/consulting/task?consulting_id=%s"% consulting_id)
            if not r2.ok:
                print("r2-status_code: %s"% r2.status_code)
                continue
            print(u"  创建任务type[%d]"% i)
            i = i + 1
            if i > 1:
                i = 0
        
        num = num + 1

