# locust-performance
To do performance testing using locust

## info
language: **Python3**<br/>
framework: **Locust**<br/>

## directories
+ business       闇��鍋氭�鑳芥祴璇曠殑鍔熻兘闆嗗悎
+ locustfiles    鍗曠嫭鎵ц�鐨刲ocustfile鏂囦欢

## use

**no web**

<pre>

//-t 鎴�--run-time閫夐」鏄痩ocust v0.9鐨勬柊鍔熻兘
locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com --no-web -c 10 -r 2 -t 30m

//locust v0.8 浣跨敤 -n閫夐」, 鎸囧畾璇锋眰鏁�
locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com --no-web -c 10 -r 2 -n 1000

</pre>


**web**

> locust -f run.py --csv=foobar --logfile=locust.log --host=http://example.com  

鐒跺悗璁块棶 http://localhost:8089
