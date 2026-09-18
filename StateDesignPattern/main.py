from bikeMode import BikeMode
from trainMode import TrainMode
from transportService import TransportService

bike = BikeMode()
train = TrainMode()

service = TransportService(train)
service.getETA()
service.getDirection() 