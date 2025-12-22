import port_scanner


def test_scan_ports_tcp_open(monkeypatch):
    def fake_scan(ip, port, timeout):
        return port if port == 22 else None

    monkeypatch.setattr(port_scanner, "_scan_one_tcp", fake_scan)
    res = port_scanner.scan_ports(
        "1.2.3.4",
        20,
        23,
        scan_type="connect",
        protocol="tcp",
        no_banner=True,
        workers=4,
    )
    assert 22 in res["open_ports"]


def test_scan_ports_udp_no_response(monkeypatch):
    def fake_scan(ip, port, timeout):
        return None

    monkeypatch.setattr(port_scanner, "_scan_one_udp", fake_scan)
    res = port_scanner.scan_ports(
        "1.2.3.4",
        1,
        5,
        scan_type="connect",
        protocol="udp",
        no_banner=True,
        workers=4,
    )
    assert res["protocol"] == "udp"
    assert res["udp_no_response"] == [1, 2, 3, 4, 5]
