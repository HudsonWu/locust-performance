# -*- coding: utf-8 -*-

import requests

authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImU5ZWEyMGM4ZmJjYWU1OTI5ODUyYTc2NDliZmM4OTdhNGExMmEyYTBhY2UzNzhjOGMwZDViZDViNDU2MzA4MGQ0OTNiYzg1NjgyYzBhNGVmIn0.eyJhdWQiOiIyIiwianRpIjoiZTllYTIwYzhmYmNhZTU5Mjk4NTJhNzY0OWJmYzg5N2E0YTEyYTJhMGFjZTM3OGM4YzBkNWJkNWI0NTYzMDgwZDQ5M2JjODU2ODJjMGE0ZWYiLCJpYXQiOjE1MzE3OTkzNDUsIm5iZiI6MTUzMTc5OTM0NSwiZXhwIjoxODQ3MTU5MzQ1LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.OwAxmy5laJ2YGj8vGd05TgtZTClzhr6Zv06GbE8FzTR8m4_OmrY_8i886LwFJVOku0xHYotTZ9FFaEufSFgw6z_IbYFBbJS1sPFgRkKE_ZqjNGA5hN2ec6QxKPdeYDZiUMUt5N0Q--WSIBuVXNs4H-IFQz5DNXmvPEnpJNRtLjMkG32LcuYWFpg3JGtBXk4c_Ddo92DfpiUAWXrz4P5K_I8pKSV7KKgk9X5QdWSLlKrO9mT5cDYXQdOPgut6H33BULiv6kgm3KFohTOgpuVHlsMd9cNSbspTpjf5QW72_9ZPtDSJhI194h1WoAXHPXubincnO_IIWzbHdJx-57GHuKSc29RF3X4zdVBEpG1uSi8lgEaFP9Eik-2VlRyx7uXkjOG7xQZ-bj7YPppT5OoR6xu4fnahGiE1OM3VCn_eAOGKqRuHoyhI_a7RhcK900P55-WRhroWUG-njZoAr_9bL2atJJ8jkm2yhdeWl73G8E9DLxPrakTvEgphy2i2v2s3xyLDIVFv5fV4nvR8_A03y2c6SbybLeWhzuF7G8vMi-ZSon8x1wqVlvTjZGlZsew0vlY7-zv1T4HBGHRaYsL1ZQDcySJ_xQAyJsIh8vBMHuughAY0Wo0FfX_oABoBP2rn110C7L8wAWOwlXM_WK5UbIVpwnZdGKF2GBd8FuRP7UY"
# authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImIwOTdmOGQ1ZWJmNGNkNTFkZDYxN2IxYjEyMDc0M2NlNTIyYjdjNWRhYmI1ZTFiYzY2OTYyOTcxOTQxNGFjMTdmYWE0YmRjZmZhZjFjNDI3In0.eyJhdWQiOiIyIiwianRpIjoiYjA5N2Y4ZDVlYmY0Y2Q1MWRkNjE3YjFiMTIwNzQzY2U1MjJiN2M1ZGFiYjVlMWJjNjY5NjI5NzE5NDE0YWMxN2ZhYTRiZGNmZmFmMWM0MjciLCJpYXQiOjE1MzE4OTg0ODMsIm5iZiI6MTUzMTg5ODQ4MywiZXhwIjoxODQ3MjU4NDgzLCJzdWIiOiI0OCIsInNjb3BlcyI6W119.MbeA0DJOpKep5oT6h7V4M34wnK4bFE9E5wCtj62IXSfVZ3L8PyjEvmp2ozoxiwuB7VweNMkFvrrE6gZDz4LcGPVAgXBWDfwCOC53ZjcfZ9OR057ABAG4HLPuCI08PHh9qkSMedke8LxCwBwyykNPoA8gi_8z1POvnFZhqtMkoL3uzJkhPc7PJw326yCinUA74DPHDyxauf4ltMxfKGkXTCOtzgIh-OY_C7iRPsAMx853RzCyeTqOHn7Ito9mZI8GH7NQneWjBhq4aS7o_F0Gx9FOrPux9B6fVwtyXg8bqyXBkoQez8EAMD90uaYsRtnn9sCL-Kxm_SFzohGGfEK_qI_ZpTqzA3XxTcfdYKca1UjifpZ1Za2X3S3M2ddoUpVFxFCXdeLIAA1D1MKlVt3l8-VB_jDQdpRpWvHSxqppKafDP-l5-S19AEX_FHCcGb3A0Wp6w153WAsEH3gNBap-cOKza0K8vDZsMU8NF1XeHn14Wr9vZJIn4-Qj_Q_dZCFuxrtyqwfG9JYxDj3pX0c_VxWfQOFBJhr_dqOs27dIGIcoAnu5uKHL_Gm2AFL2nV0wSutSqq8y7f15SuyZyE_y2D_4orcpMNHmKoOReWrjVaPVe0Fr99qTykRxbPWPU2-lwPKnUt-UyaPCe5nKhw5G9aAq_91BmFTbnN8pS_bGm0U"
headers = {'Accept': "application/json", 'Authorization': authorization}
consulting_id = "omx8kwrgl5aep3nv"

def to_specify():
    num = 1
    while num < 54:
        r1 = requests.get(headers=headers,url="http://api.zwphp.test/v1/manage/projects?limit=10&page=1&project_search=测试&consulting_id=%s"\
                          % consulting_id)
        if not r1.ok:
            print("r1-status_code: %s"% r1.status_code)
            print(r1.json())
        
        receive = r1.json()
        projects = receive['data']
        
        print(u"第 %d 轮项目删除: "% num)
        
        i = 1
        
        for project in projects:
            id = project['id']
            data = dict(id=id, project_status="1")
            # 更改项目状态为“未开启”
            r3 = requests.put(url="http://api.zwphp.test/v1/project/%s?consulting_id=%s"\
                              % (id, consulting_id), headers=headers, data=data)
            if r3.ok:
                print(u"  更改第 %d 个项目的状态"% i)
                # 删除项目
                r2 = requests.delete(headers=headers, url="http://api.zwphp.test/v1/project/%s?\
                consulting_id=%s"% (id, consulting_id))
                
                if not r2.ok:
                    print("r2-status_code:%s"% r2.status_code)
                    print(r2.json())
                    print(num)
                    continue
                else:
                    print(u"  删除第 %d 个项目"% i)
                    
            else:
                print("r3-status:%s"% r3.status_code)
                print(r3.json())
                print(num)
                
            i = i + 1
        
        num = num + 1

to_specify()

        

def to_null():
    # 筛选出指定项目
    r1 = requests.get(headers=headers,url="http://api.zwphp.test/v1/manage/projects\
                      ?limit=10&page=1&project_search=测试&consulting_id=%s"% consulting_id)
    if not r1.ok:
        print("r1-status_code: %s"% r1.status_code)
        print(r1.json())
    
    receive = r1.json()
    projects = receive['data']
    
    while projects:
        
        for project in projects:
            id = project['id']
            data = dict(id=id, project_status="1")
            # 更改项目状态为“未开启”
            r3 = requests.put(url="http://api.zwphp.test/v1/project/%s?consulting_id=%s"% (id, consulting_id), headers=headers, data=data)
            if r3.ok:
                # 删除项目
                r2 = requests.delete(headers=headers, url="http://api.zwphp.test/v1/project/%s?\
                consulting_id=%s"% (id, consulting_id))
                if not r2.ok:
                    print("r2-status_code:%s"% r2.status_code)
                    print(r2.json())
                    print(i)
                    continue   
            else:
                print("r3-status:%s"% r3.status_code)
                print(r3.json())
                print(i)
                continue
            
        i = i + 1
        r1 = requests.get(headers=headers, url="http://api.zwphp.test/v1/manage/projects?limit=10&page=1&project_search=测试&consulting_id=%s"% consulting_id)
        if not r1.ok:
            print("r1-status_code: %s"% r1.status_code)
            print(r1.json())
            print(i)
            break
        
        receive = r1.json()
        projects = receive['data']    
        
        
