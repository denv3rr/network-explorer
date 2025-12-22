import network_scanner


def test_detect_connection_type():
    assert network_scanner._detect_connection_type("Wi-Fi") == "Wi-Fi"
    assert network_scanner._detect_connection_type("wlan0") == "Wi-Fi"
    assert network_scanner._detect_connection_type("Ethernet") == "Wired"
    assert network_scanner._detect_connection_type("tap0") == "VPN/Tunnel"
    assert network_scanner._detect_connection_type("unknown0") == "Unknown"
