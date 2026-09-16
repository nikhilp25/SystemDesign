from weather_station import WeatherStation
from tv import TV
from mobile import Mobile

ws = WeatherStation()
tv = TV()
mobile = Mobile()

ws.add_observer(tv)
ws.update_temperature(30)

ws.add_observer(mobile)
ws.update_temperature(35)