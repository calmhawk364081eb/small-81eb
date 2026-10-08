"""Simple UI state helper: push/pop/inspect UI states."""

class UIStateManager:
    def __init__(self):
        self._stack = []

    def push(self, name, data=None):
        self._stack.append((name, data))

    def pop(self):
        return self._stack.pop() if self._stack else None

    def peek(self):
        return self._stack[-1] if self._stack else None

    def list_states(self):
        return list(self._stack)

    def clear(self):
        self._stack.clear()


def main():
    mgr = UIStateManager()
    print("Simple UI State Helper")
    while True:
        cmd = input(">> ").strip()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == "push":
            if len(parts) >= 2:
                data = " ".join(parts[2:]) if len(parts) > 2 else None
                mgr.push(parts[1], data)
                print("Pushed", parts[1])
            else:
                print("Usage: push <name> [data]")
        elif parts[0] == "pop":
            state = mgr.pop()
            print("Popped", state)
        elif parts[0] == "peek":
            print("Top", mgr.peek())
        elif parts[0] == "list":
            print("Stack:", mgr.list_states())
        elif parts[0] in ("quit", "exit"):
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()