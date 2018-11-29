from module1 import connectionDetails, ZToken, ZFile

myConnectionDetails = connectionDetails("c2bfc320-bb04-413d-8ce6-91886f7b4d9b","xnAH1Foi03IxaybnuBL1")
myZToken = ZToken()
myZToken.generate(myConnectionDetails)
print("Token is : " + myZToken.value)

myZbillingPreviewRun = ZFile("BillingPreviewRun")
myZbillingPreviewRun.download(myConnectionDetails,"https://apisandbox-api.zuora.com/rest/api/file/2c92c08666f737390166ff362fa74573","download")

myZbillingPreviewRun.unzip("download")
