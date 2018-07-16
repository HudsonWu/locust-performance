# locust-performance
To do performance testing using locust

### info
language: **Python3**<br/>
framework: **Locust**<br/>

### directories
+ business       需要做性能测试的功能集合
+ locustfiles    单独执行的locustfile文件

## use
+ no web

> locust -f run.py --csv=foobar --host=http://example.com --no-web -c 10 -r 2 -t 30m

+ web

> locust -f run.py --host=http://example.com
