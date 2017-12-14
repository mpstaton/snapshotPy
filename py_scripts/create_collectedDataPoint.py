from models.collectedDataPoint import CollectedDataPoint

newDataPoint = CollectedDataPoint(variableHandle="testHandle", value=3)

newDataPoint.addToDB()
