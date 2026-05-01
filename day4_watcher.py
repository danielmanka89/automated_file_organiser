import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"CREATED: {event.src_path}")
    
    def on_modified(self, event):
        print(f"MODIFIED: {event.src_path}")
    
    def on_deleted(self, event):
        print(f"DELETED: {event.src_path}")
    
    def on_moved(self, event):
        print(f"MOVED: {event.src_path} -> {event.dest_path}")

# Create the watcher
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)

print("Starting to watch this folder...")
print("Press Ctrl+C to stop")
print("-" * 50)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\nSTOPPED WATCHING.")

observer.join()