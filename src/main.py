from flet import *
import datetime
import flet_android_notifications as fan
import flet_permission_handler as fph
async def main(page: Page):
    notify=fan.FletAndroidNotifications()
    
    ph=fph.PermissionHandler()
    requist=await ph.request(fph.Permission.NOTIFICATION)
    async def send():
        await notify.show_notification(
            1,
            "Granted",
            "Thanks for accept"
        )
        await notify.schedule_notification(
            2,
            "Whooo",
            "Its Time",
            datetime.datetime.now().replace(minute=datetime.datetime.now().minute+2)
        )
    page.add(Button("Send", on_click=lambda e:send()))
    if requist==fph.PermissionStatus.GRANTED:
        send()
        page.add(Text("You Will Be Notified after two minuts"))
    
    
    page.update()

    



run(main)
