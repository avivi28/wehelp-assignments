//request1
function calculate(min,max){
    var sum=0;
    for (var min;min<=max;min++){
        sum=sum+min;
    }
    console.log(sum);
}
calculate(1,3)
calculate(4,8)
//request2
function avg(data){
    var sum=0;
    for (var i=0;i<data.count;i++){
        sum=sum+data.employees[i].salary;
    }
    var result=sum/data.count;
    console.log(result);
}
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})
//request3
function maxProduct(nums){

    var product = [];
    for(var i=0;i<nums.length;i++) {
        for(var j=i+1;j<nums.length;j++) {
            product.push(nums[i] * nums[j]);
        }
    }
    
    var max=product[0];
    for (var i=0; i<product.length; i++){
        if (product[i]>=max){
            max=product[i];
        }
    }
    console.log(max);
}
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])
//request4
function twoSum(nums,target){
    var sum
    for (var i=0;i<nums.length;i++){
        for (var j =i+1;i<nums.length;j++){
            sum=nums[i]+nums[j];
            if (sum==target){
                return [i,j];
            }
        }
    }
}
let result=twoSum([2,11,7,15],9);
console.log(result);
//request5
function maxZeros(nums){
    var max_zeroes=0
    var count=0
    for (var i=0;i<nums.length;i++){
        if(nums[i]==0){
            count+=1;
            if(count>max_zeroes){
                max_zeroes=count;
            }
        }else{
            count=0;
        }
    }
    console.log(max_zeroes);
}
maxZeros([0,1,0,0]);
maxZeros([1,0,0,0,0,1,0,1,0,0]);
maxZeros([1,1,1,1,1]);
maxZeros([0,0,0,1,1]);