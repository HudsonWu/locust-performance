# -*- coding: utf-8 -*-

import requests

authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImU5ZWEyMGM4ZmJjYWU1OTI5ODUyYTc2NDliZmM4OTdhNGExMmEyYTBhY2UzNzhjOGMwZDViZDViNDU2MzA4MGQ0OTNiYzg1NjgyYzBhNGVmIn0.eyJhdWQiOiIyIiwianRpIjoiZTllYTIwYzhmYmNhZTU5Mjk4NTJhNzY0OWJmYzg5N2E0YTEyYTJhMGFjZTM3OGM4YzBkNWJkNWI0NTYzMDgwZDQ5M2JjODU2ODJjMGE0ZWYiLCJpYXQiOjE1MzE3OTkzNDUsIm5iZiI6MTUzMTc5OTM0NSwiZXhwIjoxODQ3MTU5MzQ1LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.OwAxmy5laJ2YGj8vGd05TgtZTClzhr6Zv06GbE8FzTR8m4_OmrY_8i886LwFJVOku0xHYotTZ9FFaEufSFgw6z_IbYFBbJS1sPFgRkKE_ZqjNGA5hN2ec6QxKPdeYDZiUMUt5N0Q--WSIBuVXNs4H-IFQz5DNXmvPEnpJNRtLjMkG32LcuYWFpg3JGtBXk4c_Ddo92DfpiUAWXrz4P5K_I8pKSV7KKgk9X5QdWSLlKrO9mT5cDYXQdOPgut6H33BULiv6kgm3KFohTOgpuVHlsMd9cNSbspTpjf5QW72_9ZPtDSJhI194h1WoAXHPXubincnO_IIWzbHdJx-57GHuKSc29RF3X4zdVBEpG1uSi8lgEaFP9Eik-2VlRyx7uXkjOG7xQZ-bj7YPppT5OoR6xu4fnahGiE1OM3VCn_eAOGKqRuHoyhI_a7RhcK900P55-WRhroWUG-njZoAr_9bL2atJJ8jkm2yhdeWl73G8E9DLxPrakTvEgphy2i2v2s3xyLDIVFv5fV4nvR8_A03y2c6SbybLeWhzuF7G8vMi-ZSon8x1wqVlvTjZGlZsew0vlY7-zv1T4HBGHRaYsL1ZQDcySJ_xQAyJsIh8vBMHuughAY0Wo0FfX_oABoBP2rn110C7L8wAWOwlXM_WK5UbIVpwnZdGKF2GBd8FuRP7UY"
headers = {'Accept': "application/json", 'Authorization': authorization}
consulting_id = "omx8kwrgl5aep3nv"

project_name = "测试项目0718-000"
project_types = ["e4q30krxwp5p6voy","d48qz65wdv9komvp","lw7ykqr40l56ob84","dkb4m6rymdrowny7","v37nz49eyzr8g0ma", \
                "vk3nw69nxb5axog7","0n8lay5j4o54vopk", "d48qz65wg69komvp","dby8lj5vjb563qv0","0wqvk397dq9d6a8x"]
contract_id = "803wk5p3qp94mg6d"

num = 19

while num < 21:
    # 获取合同
    r1 = requests.get(headers=headers, url="http://api.zwphp.test/v1/my/contracts?limit=10&page=1&consulting_id=%s"% consulting_id)
    if not r1.ok:
        print("r1-status_code: %s"% r1.status_code)
    else:
        print(u"开始第 %d 轮项目创建"% num)
        i = 0
        receive = r1.json()
        contracts = receive['data']
        for contract in contracts:
            project_name = "测试项目-"+str(num)+"-"+str(i)
            contract_id = contract['id']
            project_type = project_types[i]
            # 创建项目
            post_data = {"project_name":project_name, \
                         "project_type":project_type, \
                         "start_time":"2018-07-11","end_time":"2018-08-23", \
                         "description":"123456", \
                         "signed_money":5.67,"review_auth":2, \
                         "contract_id":contract_id}            
            r2 = requests.post(headers=headers, json=post_data, \
                               url="http://api.zwphp.test/v1/project?consulting_id=%s"% consulting_id)
            if not r2.ok:
                print("r2-status_code: %s"% r2.status_code)
                continue
            print(u"  创建第 %d 个项目"% i)
            i = i + 1
            if i > 9:
                i = 0
        
        num = num + 1
            
