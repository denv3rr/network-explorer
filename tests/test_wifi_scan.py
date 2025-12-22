import wifi_scan


def test_parse_windows_netsh_networks():
    sample = """
        SSID 1 : HomeNet
            Network type            : Infrastructure
            Authentication          : WPA2-Personal
            Encryption              : CCMP
            BSSID 1                 : aa:bb:cc:dd:ee:ff
            Signal                  : 78%
            Channel                 : 11
        SSID 2 : Guest
            BSSID 1                 : 11:22:33:44:55:66
            Signal                  : 52%
            Channel                 : 6
    """
    nets = wifi_scan.parse_windows_netsh_networks(sample)
    assert len(nets) == 2
    assert nets[0]["ssid"] == "HomeNet"
    assert nets[0]["signal"] == 78
    assert nets[0]["channel"] == 11
    assert "aa:bb:cc:dd:ee:ff" in nets[0]["bssids"]


def test_parse_nmcli_handles_escaped_colon():
    sample = r"My\\:SSID:aa:bb:cc:dd:ee:ff:6:70:WPA2"
    nets = wifi_scan.parse_nmcli(sample)
    assert len(nets) == 1
    assert nets[0]["ssid"] == "My:SSID"
