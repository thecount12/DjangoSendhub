# Platform Developer Programming Challenge
=======
<b>Hosted on Madscott.org</b> 

http://www.madscott.org/sendhub/

API using python-django 

Goal to Build an HTTP REST API endpoint that routes messages optimizing for the number of 
network requests. 

|Category	| relay IP subnets	| Throughput	| Cost/Request| 
|:----------	|:----------:		|:------------:	|:---------|
|Small		|10.0.1.0/24		|1msg/req	|$0.01|
|Medium		|10.0.2.0/24		|5msg/req	|$0.05|
|Large		|10.0.3.0/24		|10msg/req	|$0.10|
|Super		|10.0.4.0/24		|25msg/req	|$0.25|

<b>Looks to be coin change problem</b>

http://en.wikipedia.org/wiki/Change-making_problem

http://en.wikipedia.org/wiki/Coin_problem

https://bitbucket.org/trebsirk/algorithms/src/9728989fdff75481cc419593f4189e6e07132287/coinchanging.py?at=master

http://bryceboe.com/2009/11/04/dynamic-programming-%E2%80%93-coin-change-problem-in-python/

	Recursive code samples proof of concept:
	coinsOptions = [1, 2, 3]
	def numberOfWays(target):
		if (target < 0):
			return 0
		elif(target == 0):
			return 1
	else:
		return sum([numberOfWays(target - coin) for coin in coinsOptions])
	print numberOfWays(5)



	Dynamic code samples proof of concept:
	target = 5
	coins = [1,2,3]
	ways = [1]+[0]*target
	for coin in coins:
		for i in range(coin, target+1):
			ways[i]+=ways[i-coin]
	print ways[target]

<b>Solving</b>

Linear programming

Integer Linear Programming is often a quick way to solve this kind of problem, but the time it will take to resolve the problem is not certain, and may be slow in some cases
Greedy method

In the US (and most other) coin systems, a greedy algorithm of picking the largest denomination of coin which is not greater than the remaining amount to be made will always produce the optimal result. This is not automatically the case, though: if the coin denominations were 1, 3 and 4, then to make 6, the greedy algorithm would choose three coins (4,1,1) whereas the optimal solution is two coins (3,3).

Having the total number of categories, we can solve using dynanmic programming. 

<b>Testin with sample code</b>

Greed:

	curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["510-555-5556"]}' http://madscott.org:5000/greed

Dynamic: 

	curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["510-555-5556", "412-555-5555", "412-555-5554", "412-555-5553", "412-555-5552", "412-555-5551"]}' http://madscott.org:5000/dynamic

<b>Improvements</b>

Change Patterns for phone numbers with parenthesis: example (510) 555 - 1212.

<b>Flask Implementation!</b>

http://www.github.com/thecount12/sendhub 
