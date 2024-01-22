# Dictionaries
myKeyAndValue = {"Key1":"Value1","Key2":"Value2","Key3":"Value3"}
print(myKeyAndValue) #=> {'Key1': 'Value1', 'Key2': 'Value2', 'Key3': 'Value3'}

print(myKeyAndValue['Key1']) #=> Value1

myKeyAndValueDiffType = {"key1" : 123,"key2" : "string","key3" : {1 :['grab'],2: ['shoppee'],4:['line'] }}
print(myKeyAndValueDiffType['key3'][1][0]) #=> grab

myKeyAndValueAddNew = {'lunch':'pizza','bfast':'eggs'}
myKeyAndValueAddNew['lunch'] = 'burger'
print(myKeyAndValueAddNew['lunch']) #=> burger
print(myKeyAndValueAddNew) #=> {'lunch': 'burger', 'bfast': 'eggs'}