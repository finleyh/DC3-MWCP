from uuid import UUID

import mwcp

report = {
    "errors": ["[!] Test error log"],
    "input_file": {
        "architecture": None,
        "compile_time": None,
        "data": None,
        "derivation": None,
        "description": None,
        "file_path": "C:/input_file.bin",
        "md5": "1e50210a0202497fb79bc38b6ade6c34",
        "name": "input_file.bin",
        "sha1": "baf34551fecb48acc3da868eb85e1b6dac9de356",
        "sha256": "1307990e6ba5ca145eb35e99182a9bec46531bc54ddf656a602c780fa0240dee",
        "tags": [],
        "type": "file",
    },
    "logs": ["[+] Test info log", "[!] Test error log", "[*] Test debug log"],
    "metadata": [
        {
            "file_system": None,
            "is_dir": False,
            "path": "C:\\windows\\temp\\1\\log\\keydb.txt",
            "posix": False,
            "tags": [],
            "type": "path",
        },
        {
            "file_system": None,
            "is_dir": True,
            "path": "%APPDATA%\\foo",
            "posix": False,
            "tags": [],
            "type": "path",
        },
        {
            "file_system": None,
            "is_dir": False,
            "path": "C:\\foo\\bar.txt",
            "posix": False,
            "tags": [],
            "type": "path",
        },
        {
            "file_system": None,
            "is_dir": False,
            "path": "malware.exe",
            "posix": None,
            "tags": [],
            "type": "path",
        },
        {"alphabet": "0123456789ABCDEF", "base": 16, "tags": [], "type": "alphabet"},
        {
            "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=",
            "base": 32,
            "tags": [],
            "type": "alphabet",
        },
        {
            "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
            "base": 64,
            "tags": [],
            "type": "alphabet",
        },
        {"tags": [], "type": "command", "value": "cmd.exe /c notepad.exe"},
        {"password": "123456", "tags": [], "type": "credential", "username": "admin"},
        {"password": None, "tags": [], "type": "credential", "username": "mruser"},
        {"password": "secrets", "tags": [], "type": "credential", "username": None},
        {
            "address": "14qViLJfdGaP4EeHnDyJbEGQysnCpwk3gd",
            "symbol": "BTC",
            "tags": [],
            "type": "crypto_address",
        },
        {
            "address": "bad.com",
            "c2": None,
            "listen": None,
            "network_protocol": "tcp",
            "port": 21,
            "tags": [],
            "type": "socket",
        },
        {
            "address": None,
            "c2": None,
            "listen": None,
            "network_protocol": "udp",
            "port": 1635,
            "tags": [],
            "type": "socket",
        },
        {
            "address": None,
            "c2": None,
            "listen": True,
            "network_protocol": "tcp",
            "port": 4568,
            "tags": [],
            "type": "socket",
        },
        {
            "application_protocol": "https",
            "credential": None,
            "path": "/images/baner.jpg",
            "query": "",
            "socket": {
                "address": "10.11.10.13",
                "c2": None,
                "listen": None,
                "network_protocol": None,
                "port": 443,
                "tags": [],
                "type": "socket",
            },
            "tags": [],
            "type": "url",
            "url": "https://10.11.10.13:443/images/baner.jpg",
        },
        {
            "address": "10.11.10.13",
            "c2": None,
            "listen": None,
            "network_protocol": None,
            "port": 443,
            "tags": [],
            "type": "socket",
        },
        {
            "application_protocol": None,
            "credential": {
                "password": "pass",
                "tags": [],
                "type": "credential",
                "username": "admin",
            },
            "path": None,
            "query": None,
            "socket": {
                "address": "192.168.1.1",
                "c2": None,
                "listen": None,
                "network_protocol": "tcp",
                "port": 80,
                "tags": [],
                "type": "socket",
            },
            "tags": ["proxy"],
            "type": "url",
            "url": None,
        },
        {
            "address": "192.168.1.1",
            "c2": None,
            "listen": None,
            "network_protocol": "tcp",
            "port": 80,
            "tags": [],
            "type": "socket",
        },
        {"password": "pass", "tags": [], "type": "credential", "username": "admin"},
        {
            "application_protocol": "ftp",
            "credential": {
                "password": "pass",
                "tags": [],
                "type": "credential",
                "username": "admin",
            },
            "path": None,
            "query": "",
            "socket": {
                "address": "badhost.com",
                "c2": None,
                "listen": None,
                "network_protocol": None,
                "port": 21,
                "tags": [],
                "type": "socket",
            },
            "tags": [],
            "type": "url",
            "url": "ftp://badhost.com:21",
        },
        {
            "address": "badhost.com",
            "c2": None,
            "listen": None,
            "network_protocol": None,
            "port": 21,
            "tags": [],
            "type": "socket",
        },
        {"tags": [], "type": "email_address", "value": "email@bad.com"},
        {"tags": [], "type": "event", "value": "MicrosoftExist"},
        {
            "tags": [],
            "type": "uuid",
            "value": UUID("654e5cff-817c-4e3d-8b01-47a6f45ae09a"),
        },
        {"tags": [], "type": "injection_process", "value": "svchost"},
        {"tags": [], "type": "interval", "value": 3.0},
        {
            "algorithm": "rc4",
            "iv": None,
            "key": b"hello",
            "mode": None,
            "tags": [],
            "type": "encryption_key",
        },
        {
            "algorithm": "aes",
            "iv": b"\x00\x00\x00\x00",
            "key": b"\xff\xff\xff\xff",
            "mode": "ecb",
            "tags": [],
            "type": "encryption_key",
        },
        {
            "encryption_key": None,
            "tags": [],
            "type": "decoded_string",
            "value": "GetProcess",
        },
        {
            "encryption_key": {
                "algorithm": "xor",
                "iv": None,
                "key": b"\xff\xff",
                "mode": None,
                "tags": [],
                "type": "encryption_key",
            },
            "tags": [],
            "type": "decoded_string",
            "value": "badstring",
        },
        {
            "algorithm": "xor",
            "iv": None,
            "key": b"\xff\xff",
            "mode": None,
            "tags": [],
            "type": "encryption_key",
        },
        {"tags": [], "type": "mission_id", "value": "target4"},
        {"tags": [], "type": "mutex", "value": "ithinkimalonenow"},
        {
            "key": "misc_info",
            "tags": ["something"],
            "type": "other",
            "value": "some miscellaneous info",
            "value_format": "string",
        },
        {
            "key": "random_data",
            "tags": [],
            "type": "other",
            "value": b"\xde\xad\xbe\xef",
            "value_format": "bytes",
        },
        {
            "key": "keylogger",
            "tags": [],
            "type": "other",
            "value": True,
            "value_format": "boolean",
        },
        {
            "key": "misc_integer",
            "tags": ["tag1"],
            "type": "other",
            "value": 432,
            "value_format": "integer",
        },
        {
            "tags": [],
            "type": "pipe",
            "value": "\\.\\pipe\\namedpipe",
        },
        {
            "data": "c:\\update.exe",
            "data_type": "REG_SZ",
            "hive": "HKEY_LOCAL_MACHINE",
            "subkey": "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            "tags": [],
            "type": "registry",
            "value": "Updater",
        },
        {
            "data": None,
            "data_type": None,
            "hive": "HKEY_LOCAL_MACHINE",
            "subkey": "Foo\\Bar",
            "tags": [],
            "type": "registry",
            "value": None,
        },
        {
            "data": None,
            "data_type": None,
            "hive": None,
            "subkey": None,
            "tags": ["tag2"],
            "type": "registry",
            "value": "Baz",
        },
        {
            "d_mod_p1": 7,
            "d_mod_q1": 3,
            "modulus": 187,
            "p": 17,
            "private_exponent": 23,
            "public_exponent": 7,
            "q": 11,
            "q_inv_mod_p": 14,
            "tags": [],
            "type": "rsa_private_key",
        },
        {"modulus": 187, "public_exponent": 7, "tags": [], "type": "rsa_public_key"},
        {
            "description": "Provides a common management to access "
            "information about windows user.",
            "display_name": "Windows User Management",
            "dll": None,
            "image": "%System%\\svohost.exe",
            "name": "WindowsUserManagement",
            "tags": [],
            "type": "service",
        },
        {
            "file_system": None,
            "is_dir": False,
            "path": "%System%\\svohost.exe",
            "posix": False,
            "tags": [],
            "type": "path",
        },
        {
            "tags": [],
            "type": "user_agent",
            "value": "Mozilla/4.0 (compatible; MISE 6.0; Windows NT 5.2)",
        },
        {"tags": [], "type": "version", "value": "3.1"},
        {"tags": [], "type": "version", "value": "403.10"},
        {
            "architecture": None,
            "compile_time": None,
            "data": None,
            "derivation": "embedded",
            "description": "Extracted backdoor Foo config file",
            "file_path": None,
            "md5": "8c41f2802904e53469390845cfeb2b28",
            "name": "config.xml",
            "sha1": "ce6519a1dc71510ee15e66b3926fd164a373803a",
            "sha256": "81addbf732d9d6c24b1d3ede7afceef6a1cff59af7b63d01504a0913a6c6701a",
            "tags": [],
            "type": "file",
        },
    ],
    "mwcp_version": mwcp.__version__,
    "parser": "FooParser",
    "recursive": False,
    "external_knowledge": {},
    "tags": ["tagging", "test"],
    "type": "report",
}
