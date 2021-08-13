import src.devices.board_mock as board_mock
import src.devices.temp_probe_mock as temp_probe_mock


def test_temp_probe_create():
    temp_sensor = temp_probe_mock.Temp_Probe(
        board_mock.SCK, board_mock.MOSI, board_mock.MISO, board_mock.D4, wires=2
    )
    assert temp_sensor is not None


def test_temp_probe_create_null():
    temp_sensor = temp_probe_mock.Temp_Probe(None, None, None, None)
    assert temp_sensor is not None


def test_temp_probe_get_temperature():
    temp_sensor = temp_probe_mock.Temp_Probe(
        board_mock.SCK, board_mock.MOSI, board_mock.MISO, board_mock.D4, wires=2
    )
    assert temp_sensor.get_temperature() == 0


def test_temp_probe_temperature_null():
    temp_sensor = temp_probe_mock.Temp_Probe(None, None, None, None)
    assert temp_sensor.get_temperature() == 0


def test_temp_probe_resistance():
    temp_sensor = temp_probe_mock.Temp_Probe(
        board_mock.SCK, board_mock.MOSI, board_mock.MISO, board_mock.D4, wires=2
    )
    assert temp_sensor.get_resistance() == 1000.0


def test_temp_probe_resistance_null():
    temp_sensor = temp_probe_mock.Temp_Probe(None, None, None, None)
    assert temp_sensor.get_resistance() == 1000.0


def test_temp_probe_set_temperature():
    temp_sensor = temp_probe_mock.Temp_Probe(
        board_mock.SCK, board_mock.MOSI, board_mock.MISO, board_mock.D4, wires=2
    )
    temp_sensor.mock_set_temperature(25)
    assert temp_sensor.get_temperature()


def test_temp_probe_set_resistance():
    temp_sensor = temp_probe_mock.Temp_Probe(
        board_mock.SCK, board_mock.MOSI, board_mock.MISO, board_mock.D4, wires=2
    )
    temp_sensor.mock_set_resistance(500)
    assert temp_sensor.get_resistance() == 500
