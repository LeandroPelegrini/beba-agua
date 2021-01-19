import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify
Notify.init("Test Notifier")

notification = Notify.Notification.new(
	"Beba Água!🚰",
	"\nBora beber <b>água</b> para ficar hidratadinho!🥤\n",
	"gtk-dialog-info"
	)

notification.set_urgency(1)

notification.show()
