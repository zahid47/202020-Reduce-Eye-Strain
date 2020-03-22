import time
import win10toast

notification = win10toast.ToastNotifier()

notify_after = float(input("(in minutes) Notify after: ")) * 60

print("The program is running... (Do not close this window!)")
print()

time.sleep(notify_after)
while True:

    print("Notified!")
    print(f"Next notification in {notify_after/60} mins.")
    print()
    
    notification.show_toast("20-20-20", "Look Away for 20 seconds!", duration=4)
    time.sleep(notify_after)
