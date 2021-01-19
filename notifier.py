import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify
Notify.init("Test Notifier")

notification = Notify.Notification.new(
	"Beba Água!🚰", //título da notificação
	"\nBora beber <b>água</b> para ficar hidratadinho!🥤\n", //mensagem da notificação
	"gtk-dialog-info" //ícone da notificação
	)

notification.set_urgency(1) //urgência da notificação (0,1,2)

notification.show()
