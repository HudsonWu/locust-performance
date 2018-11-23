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

提供了两种方式去执行性能测试<br/>
一种是直接执行run.py对所有接口进行测试<br/>
另一种是进入locustfiles目录, 目录里有很多python文件, 分别对应不同模块, 对不同模块接口分别进行测试<br/>

**no web**
<pre>
//代码中已经集成了log输出功能, 下面的命令执行时可以不用--logfile选项
//使用-f选项指定要执行的文件, 可以执行的文件包括项目根目录下的run.py文件和locustfiles目录下的所有文件

//-t 或 --run-time选项是locust v0.9的新功能
locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com --no-web -c 10 -r 2 -t 30m

//locust v0.8 使用 -n选项, 指定请求数
locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com --no-web -c 10 -r 2 -n 1000
</pre>

**web**
> locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com  

然后访问  http://localhost:8089
