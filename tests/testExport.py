from module1 import connectionDetails, ZToken, ZFile

myConnectionDetails = connectionDetails("c2bfc320-bb04-413d-8ce6-91886f7b4d9b","xnAH1Foi03IxaybnuBL1")
myZToken = ZToken()
myZToken.generate(myConnectionDetails)
print("Token is : " + myZToken.value)

myZDataExport1 = ZFile("Export")
myZDataExport1.generate(myConnectionDetails, myZToken)
print("Export Job Id : " + myZDataExport1.runId)
myZDataExport1.retrieve(myConnectionDetails, myZDataExport1.runId, myZToken, 10)

myZDataExport1.downloadCsv(myConnectionDetails,myZToken, myZDataExport1.fileUrl,"download")

