import sys
import io
import asyncio
import os

# Forzar la codificación UTF-8 para evitar errores en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from unitree_webrtc_connect.webrtc_driver import UnitreeWebRTCConnection, WebRTCConnectionMethod
from aiortc.contrib.media import MediaPlayer

# --- CONFIGURACIÓN ---
# Usamos la IP del Modo AP (Wi-Fi del robot) forzada por LocalSTA
ROBOT_IP = "192.168.12.1"

# Clave AES (32 caracteres exactos)
AES_KEY = "32073772c4b12a1bbac63b40d84b2119e"[:32]

# El archivo de audio que está en tu PC
AUDIO_FILE = "voz.mp3" 

async def main():
    conn = None
    try:
        if not os.path.exists(AUDIO_FILE):
            print(f"❌ Error: El archivo '{AUDIO_FILE}' no está en esta carpeta.")
            return

        print(f"🔗 Conectando al robot en {ROBOT_IP}...")
        
        # Forzamos LocalSTA pero apuntando a la IP del Wi-Fi
        conn = UnitreeWebRTCConnection(
            WebRTCConnectionMethod.LocalSTA,
            ip=ROBOT_IP,
            aes_128_key=AES_KEY
        )

        await conn.connect()
        print("✅ ¡Conexión establecida correctamente!")

        print(f"🎵 Enviando audio: {AUDIO_FILE}")
        player = MediaPlayer(AUDIO_FILE)
        
        if player.audio:
            conn.pc.addTrack(player.audio)
            print("🔊 Audio enviado. El robot debería hablar ahora.")
            
            # Esperamos 10 segundos para que el robot reproduzca el audio
            await asyncio.sleep(10) 
        else:
            print("⚠️ El archivo no es válido.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if conn:
            await conn.disconnect()
            print("🔌 Desconectado del robot.")

if __name__ == "__main__":
    asyncio.run(main())