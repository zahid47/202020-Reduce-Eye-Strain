import time
import win10toast

notification = win10toast.ToastNotifier()

print("\nThe program is running... (Do not close this window!)\n")


def notify(notify_after):
    time.sleep(notify_after)

    while True:

        print("Notified!")
        print(f"Next notification in {notify_after/60} mins.\n")
        
        notification.show_toast("20-20-20", "Take your eyes off the screen for 20 secs!", duration=4)
        
        time.sleep(notify_after)

notify(float(input("Notify in every ? minutes: ")) * 60)
