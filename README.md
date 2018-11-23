# locust-performance
To do performance testing using Locust

+ **info**
  + language
      + Python3
  + framework
      + Locust

+ **directories**
  + business      需要做性能测试的功能集合
  + locustfiles   单独执行的locustfile文件

## How To Use

**no web**
<pre>
//代码中已经集成了log输出功能, 下面的命令执行时可以不用--logfile选项

//-t 或 --run-time选项是locust v0.9的新功能
locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com --no-web -c 10 -r 2 -t 30m

//locust v0.8 使用 -n选项, 指定请求数
locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com --no-web -c 10 -r 2 -n 1000
</pre>

**web**
> locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com  

然后访问  http://localhost:8089
