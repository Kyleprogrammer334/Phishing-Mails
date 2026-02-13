import asyncio
from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f'Meldung von: {envelope.mail_from}')
        print(f'Empfänger: {envelope.rcpt_tos}')
        print(f'Inhalt:\n{envelope.content.decode("utf8")}')
        print("-" * 20)
        return '250 Message accepted for delivery'

if __name__ == '__main__':
    handler = CustomHandler()
    controller = Controller(handler, hostname='127.0.0.1', port=1026)
    controller.start()
    print("SMTP Debugging Server läuft auf localhost:1025. Drücke Strg+C zum Beenden.")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        controller.stop()
