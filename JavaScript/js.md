1.  使用 typeof bar === "object" 判断 bar 是不是一个对象有神马潜在的弊端？如何避免这种弊端？
	使用 typeof 的弊端是显而易见的(这种弊端同使用 instanceof)：
	
	```javascript
	let obj = {};
	let arr = [];
 
	console.log(typeof obj === 'object'); //true
	console.log(typeof arr === 'object'); //true
	console.log(typeof null === 'object'); //true
	```

	从上面的输出结果可知，typeof bar === "object" 并不能准确判断 bar 就是一个 Object。可以通过 Object.prototype.toString.call(bar) === "[object Object]" 来避免这种弊端：
	
	```javascript
	let obj = {};
	let arr = [];
 
	console.log(Object.prototype.toString.call(obj)); //[object Object]
	console.log(Object.prototype.toString.call(arr)); //[object Array]
	console.log(Object.prototype.toString.call(null)); //[object Null]
	```
	另外，为了珍爱生命，请远离 == ,而 [] === false 是返回 false 的。

2.  下面的代码会在 console 输出神马？为什么？

	```javascript
	(function(){
 		var a = b = 3;
	})(); 
	console.log("a defined? " + (typeof a !== 'undefined')); 
	console.log("b defined? " + (typeof b !== 'undefined'));
	```