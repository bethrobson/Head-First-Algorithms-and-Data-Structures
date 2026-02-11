from stack import Stack

class Browser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = "home.com"

    def visit(self, url):
        self.back_stack.push(self.current)  
        self.current = url               
        self.forward_stack.clear()       

    def back(self):
        if not self.back_stack.isEmpty():
            self.forward_stack.push(self.current)
            self.current = self.back_stack.pop()
        else:
            print("No page to go back to.")

    def forward(self):
        if not self.forward_stack.isEmpty():
            self.back_stack.push(self.current)
            self.current = self.forward_stack.pop()
        else:
            print("No page to go forward to.")

    def show(self):
        print(f"Back: {self.back_stack.stack} ",
              f"| Current: {self.current} ",
              f"| Forward: {list(reversed(self.forward_stack.stack))}")

browser = Browser()
browser.visit("pets.org")
browser.visit("juggling.com")
browser.visit("pythonrocks.com")
browser.visit("recipes.com")
browser.visit("shop.net")
browser.visit("funnyvideos.xyz")

browser.show()
browser.back()
browser.show()
browser.back()
browser.show()
browser.forward()
browser.show()
browser.visit("gym.info")
browser.show()


