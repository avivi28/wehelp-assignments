#request1
def calculate(min,max):
    sum=0
    for x in range(min,(max+1)):
        sum=sum+x
    print(sum)
calculate(1,3)
calculate(4,8)
#request2
def avg(data):
    sum=0
    for n in data["employees"]:
        sum=sum+n["salary"]
    print(sum/data["count"])
    
    
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
#request3
def maxProduct(nums):
    product = []
    for i in range(0,len(nums)):
        for j in range((i+1), len(nums)):
            product.append(nums[i] * nums[j])
    max=product[0]
    for i in range(0,len(product)):
        if product[i]>=max:
            max=product[i]
    print(max)
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])
#request4
def twoSum(nums,target):
    sum=[0]
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            sum=nums[i]+nums[j]
            if sum==target:
                return [i,j]
result=twoSum([2,11,7,15],9)
print(result)
#request5
def maxZeros(nums):
    max_zeroes=0
    count=0
    for i in range(0,len(nums)):
        if nums[i]==0:
            count+=1
            if count>max_zeroes:
                max_zeroes=count
        else:
            count=0          
    print(max_zeroes)
maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])