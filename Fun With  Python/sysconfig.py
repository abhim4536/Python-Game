# Know Your System Configrations
import platform
print("="*50, "System Information", "="*50)

uname = platform.uname()

print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
#print(f"OS: {uname.os}")
