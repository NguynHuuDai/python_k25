#!/usr/bin/env python3
"""
check_wifi_passwords.py
Liệt kê các profile Wi-Fi đã lưu và (nếu có) hiển thị mật khẩu đã lưu.

HỎI: chỉ dùng trên MÁY CỦA BẠN và cho mạng bạn được phép truy cập.

Chạy:
    python check_wifi_passwords.py
"""

import sys
import subprocess
import re
import os
import shlex
from typing import Dict, List, Tuple

def run_cmd(cmd: List[str]) -> Tuple[int, str]:
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)
        return proc.returncode, proc.stdout
    except Exception as e:
        return 1, str(e)

def get_windows_wifi_passwords() -> Dict[str, str]:
    results = {}
    code, out = run_cmd(["netsh", "wlan", "show", "profiles"])
    if code != 0:
        raise RuntimeError("Không thể chạy 'netsh wlan show profiles'. Hãy chạy terminal với quyền admin.")
    # tìm các profile
    profiles = re.findall(r"All User Profile\s*:\s*(.+)", out)
    profiles = [p.strip() for p in profiles]
    for p in profiles:
        code2, out2 = run_cmd(["netsh", "wlan", "show", "profile", "name=" + p, "key=clear"])
        pwd = None
        m = re.search(r"Key Content\s*:\s*(.+)", out2)
        if m:
            pwd = m.group(1).strip()
        results[p] = pwd or "<Không có hoặc không hiển thị>"
    return results

def get_macos_wifi_passwords() -> Dict[str, str]:
    results = {}
    # Lấy danh sách SSID đã lưu từ keychain (AirPort network password)
    # Lưu ý: trên macOS, lệnh 'security' có thể yêu cầu quyền hiện mật khẩu (sẽ bật prompt)
    code, out = run_cmd(["/usr/bin/security", "find-generic-password", "-D", "AirPort network password", "-a", "", "-g"])
    # Cách khác: liệt kê bằng 'security dump-keychain' rất dài; thay vào đó ta thử lấy danh sách SSID từ /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist nếu có
    # Tuy nhiên cách đơn giản: người dùng nhập SSID muốn check. Thử tự động tìm SSID từ plist nếu có.
    plist_path = "/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist"
    ssids = []
    if os.path.exists(plist_path):
        try:
            code2, out2 = run_cmd(["/usr/bin/defaults", "read", plist_path])
            # tìm pattern "SSIDString" trong dữ liệu
            ssids = re.findall(r"SSIDString = \"([^\"]+)\"", out2)
        except Exception:
            ssids = []
    # dedupe
    ssids = list(dict.fromkeys(ssids))
    # Nếu không tìm được SSID tự động, yêu cầu user nhập tên SSID
    if not ssids:
        print("Không tự động tìm thấy SSID đã lưu trên macOS. Nếu bạn muốn check 1 SSID cụ thể, nhập tên SSID (hoặc ENTER để bỏ qua): ", end="")
        s = input().strip()
        if s:
            ssids = [s]

    for ssid in ssids:
        try:
            # Lệnh security để lấy password: trả ra stderr nên chuyển cả stdout/stderr
            # Cú pháp: security find-generic-password -D "AirPort network password" -a "SSID" -gw
            proc = subprocess.run(["/usr/bin/security", "find-generic-password", "-D", "AirPort network password", "-a", ssid, "-gw"],
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)
            out3 = proc.stdout
            # output có thể là: "password: "thepass"" hoặc chỉ là thepass
            m = re.search(r"password: \"(.*)\"", out3)
            if m:
                pwd = m.group(1)
            else:
                # có khi dòng chứa password không có label
                lines = out3.strip().splitlines()
                pwd = lines[-1].strip() if lines else "<Không tìm thấy>"
            results[ssid] = pwd
        except Exception as e:
            results[ssid] = f"<Lỗi: {e}>"
    return results

def get_linux_wifi_passwords() -> Dict[str, str]:
    results = {}
    # 1) Try nmcli to list connections
    code, out = run_cmd(["nmcli", "-t", "-f", "NAME,TYPE", "connection", "show"])
    if code == 0 and out.strip():
        lines = [l for l in out.strip().splitlines() if l.strip()]
        wifi_names = [l.split(":",1)[0] for l in lines if ":802-11-wireless" in l or ":wifi" in l or True]  # be permissive
        wifi_names = list(dict.fromkeys(wifi_names))
        for name in wifi_names:
            # Try to read psk via nmcli (may require privileges)
            code2, out2 = run_cmd(["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", name])
            pwd = None
            if code2 == 0 and out2.strip():
                pwd = out2.strip()
            else:
                # Fallback: try read file in /etc/NetworkManager/system-connections (may require sudo)
                path = f"/etc/NetworkManager/system-connections/{name}"
                if os.path.exists(path):
                    try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                            data = f.read()
                            m = re.search(r"psk=([^\n\r]+)", data)
                            if m:
                                pwd = m.group(1).strip()
                    except Exception:
                        pwd = "<Không thể đọc (cần quyền root)>"
                else:
                    pwd = "<Không có hoặc không hiển thị>"
            results[name] = pwd or "<Không có>"
        return results
    else:
        # Nếu nmcli không tồn tại, thử đọc files system-connections
        folder = "/etc/NetworkManager/system-connections"
        if os.path.isdir(folder):
            for fname in os.listdir(folder):
                path = os.path.join(folder, fname)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        data = f.read()
                        m_name = re.search(r"^id=(.+)$", data, flags=re.M)
                        name = m_name.group(1).strip() if m_name else fname
                        m = re.search(r"psk=([^\n\r]+)", data)
                        pwd = m.group(1).strip() if m else "<Không có>"
                        results[name] = pwd
                except Exception:
                    results[fname] = "<Không thể đọc (cần root?)>"
            return results
        else:
            raise RuntimeError("Không tìm thấy nmcli hoặc NetworkManager system-connections. Trên Linux, bạn có thể dùng nmcli hoặc đọc /etc/NetworkManager/system-connections/* (cần quyền root).")

def main():
    if sys.platform.startswith("win"):
        try:
            results = get_windows_wifi_passwords()
        except Exception as e:
            print("Lỗi khi lấy mật khẩu trên Windows:", e)
            return
    elif sys.platform == "darwin":
        try:
            results = get_macos_wifi_passwords()
        except Exception as e:
            print("Lỗi khi lấy mật khẩu trên macOS:", e)
            return
    else:
        # assume linux-ish
        try:
            results = get_linux_wifi_passwords()
        except Exception as e:
            print("Lỗi khi lấy mật khẩu trên Linux:", e)
            print("Gợi ý: cài nmcli (NetworkManager) hoặc chạy script với quyền root để đọc /etc/NetworkManager/system-connections/*.")
            return

    print("\n=== Wi-Fi profiles và password (nếu có) ===\n")
    for ssid, pwd in results.items():
        print(f"SSID/Name: {ssid}")
        print(f"Password: {pwd}")
        print("-"*40)

if __name__ == "__main__":
    main()
