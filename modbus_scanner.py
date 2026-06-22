import sys
from pymodbus.client import ModbusTcpClient

def safe_modbus_audit(host, port=502):
    print(f"[*] Initiating Safe SCADA/Modbus Security Audit on {host}:{port}...")
    
    # Inizializza il client Modbus TCP
    client = ModbusTcpClient(host, port=port)
    
    try:
        # Tenta solo l'handshake di connessione iniziale
        connection = client.connect()
        
        if not connection:
            print(f"[-] Port {port} is closed or connection refused.")
            print("[*] Result: Node is not exposed via unauthenticated Modbus TCP.")
            return

        print(f"\n[🚨] CRITICAL AUDIT ALERT: Exposed Modbus TCP Service detected on {host}!")
        print("[*] STATUS: Connection handshake successful without any authentication.")
        print("[🛡️] SAFE-PoC COMPLIANCE: Exploitation and data reading are disabled in this tool.")
        print("[*] Disconnecting immediately to prevent industrial telemetry exposure.")
        
    except Exception as e:
        print(f"[-] Error during security handshake: {e}")
    finally:
        client.close()
        print("[*] Audit complete. Connection safely terminated.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python modbus_scanner.py <target_industrial_ip> [port]")
        sys.exit(1)
        
    target_host = sys.argv[1]
    target_port = int(sys.argv[2]) if len(sys.argv) > 2 else 502
    
    safe_modbus_audit(target_host, target_port)