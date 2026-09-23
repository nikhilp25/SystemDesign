from fee_strategy import VehicleBasedFeeStrategy
from vehicle_size import VehicleSize
from parking_spot import ParkingSpot
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from vehicle import Bike, Car, Truck

class ParkingDemo:
    @staticmethod
    def main():
        parking_lot = ParkingLot.get_instance()
    
        floor1 = ParkingFloor(1)
        floor1.add_spot(ParkingSpot(spot_id="F1-S1",spot_size=VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot(spot_id="F1-S2",spot_size=VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot(spot_id="F1-M1",spot_size=VehicleSize.MEDIUM))
        floor1.add_spot(ParkingSpot(spot_id="F1-L1",spot_size=VehicleSize.LARGE))
        
        floor2 = ParkingFloor(2)
        floor2.add_spot(ParkingSpot(spot_id="F2-S1",spot_size=VehicleSize.SMALL))
        floor2.add_spot(ParkingSpot(spot_id="F2-S2",spot_size=VehicleSize.SMALL))
        floor2.add_spot(ParkingSpot(spot_id="F2-M1",spot_size=VehicleSize.MEDIUM))
        floor2.add_spot(ParkingSpot(spot_id="F2-L1",spot_size=VehicleSize.LARGE))
        
        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)

        parking_lot.set_fee_strategy(VehicleBasedFeeStrategy)

        # 2. Simulate vehicle entries
        print("\n--- Vehicle Entries ---")
        floor1.display_availability()
        floor2.display_availability()

        bike = Bike("BIKE-001")
        car = Car("CAR-001")
        truck = Truck("TRUCK-001")

        bike_ticket = parking_lot.park_vehicle(bike)
        car_ticket = parking_lot.park_vehicle(car)
        truck_ticket = parking_lot.park_vehicle(truck)

        print(f"Bike parked with ticket ID {bike_ticket.get_ticket_id()}")
        print(f"Car parked with ticket ID {car_ticket.get_ticket_id()}")
        print(f"Truck parked with ticket ID {truck_ticket.get_ticket_id()}")

        floor1.display_availability()
        floor2.display_availability()

        bike1 = Bike("BIKE-002")
        car1 = Car("CAR-002")
        truck1 = Truck("TRUCK-002")

        bike1_ticket = parking_lot.park_vehicle(bike1)
        car1_ticket = parking_lot.park_vehicle(car1)
        truck1_ticket = parking_lot.park_vehicle(truck1)

        print(f"Bike parked with ticket ID {bike1_ticket.get_ticket_id()}")
        print(f"Car parked with ticket ID {car1_ticket.get_ticket_id()}")
        print(f"Truck parked with ticket ID {truck1_ticket.get_ticket_id()}")

        floor1.display_availability()
        floor2.display_availability()

        bike2 = Bike("BIKE-003")
        bike3 = Bike("BIKE-004")
        # bike6 = Bike("BIKE-005")

        bike2_ticket = parking_lot.park_vehicle(bike2)
        bike3_ticket = parking_lot.park_vehicle(bike3)
        # bike6_ticket = parking_lot.park_vehicle(bike6)

        print(f"Bike parked with ticket ID {bike2_ticket.get_ticket_id()}")

        floor1.display_availability()
        floor2.display_availability()

    

if __name__ == "__main__":
    ParkingDemo.main()