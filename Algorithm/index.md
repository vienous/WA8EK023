# 基站选址问题 (20 分)
	
假定有一条很长的直线形河流，在河岸上有 n 个房子。可以将该河流看作一条坐标轴，房
子的位置以一维坐标的形式按严格递增的顺序给出 (单位为公里)。某通信公司希望在河岸的某
些位置搭建手机基站，使得对任意一间房子都存在一个基站到它的距离小于等于 c 公里，c 为给
定的一个常数。请给出一个有效的算法来最小化需要搭建的基站的数量，并证明算法的正确性。
(注：时间复杂度为 O(n) 的正确的算法可得满分)

```javascript
var n = 11;
var S = [3,5,7,50,4,8,1,5,7,4]

function getNum(S,c){
	var num = 0;
	var d =0;
	for(var i = 0;i<S.length;i++){
		d += S[i]
		console.log(d)
		if(i!=S.length-1){//不是最后一个区间
			if(d>2*c){
				num++
				d = 0;	
			}
		}else {//是最后一个区间
			if(S[i]<2*c){
				num++;
			}else{ //最后一个区间比较大的情况
				num+=2;
				a=num-1;
			}
		}
	}
	return num;
}
console.log("一共建：" + getNum(S,5));//6
```

# 最长回文子序列问题 (20 分)

一个子序列被称为回文序列是指：该序列从右往左读和从左往右读如下所示序列：< A, C, G, T, G, T, C, A, A, A, A, T, C, G >包含了许多回文子序列，如 < A, C, G, C, A >，< A, A, A, A >。请设计计算序列 x[1..n] 的最长回文子序列。该算法的时间复杂度应为 O(n
2)

```javascript
var arr = ['A', 'C', 'G', 'T', 'G', 'T', 'G', 'A', 'A', 'A', 'A', 'T', 'C', 'G'];

function find(arr){
    var i=0,j=0;
    var res = [];
    for(var k=0;k<arr.length-1;k++){
        if(arr[k]==arr[k+1]){//相邻的两个相同
            i=k;
            j=k+1;
            while(i>=0&&j<=arr.length-1&&arr[i]==arr[j]){
                i--;
                j++;
            }
        }else{//相邻的两个不相同
            i=k;
            j=k;
            while(i>=0&&j<=arr.length-1&&arr[i]==arr[j]){
                i--;
                j++;
            }
        }
        res.push( [i+1,j-1]); //返回高低位下标
    }
    return res;
}
var result = find(arr);
//下标上界-下标下界最大时，回文最长
var maxIndex = 0
var maxValue = result[0][1]-result[0][0]
//找下标上界-下标下界最大的 
for(var x = 0;x<result.length;x++){
    var r = result[x][1]-result[x][0]
    if(r>maxValue){
        maxValue=r;
        maxIndex = x;
    }
}
var huiwen = []
for(var o = result[maxIndex][0];o<=result[maxIndex][1];o++){
    huiwen.push(arr[o]);
}
console.log(huiwen);//[ 'G', 'T', 'G', 'T', 'G' ]
```


