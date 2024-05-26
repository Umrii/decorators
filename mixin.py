class FlyableMixin:
    def fly(self):
        print("I can fly!")

class SwimmableMixin:
    def swim(self):
        print("I can swim!")

class Bird(FlyableMixin):
    def make_sound(self):
        print("Chirp chirp!")

class Duck(FlyableMixin, SwimmableMixin):
    def make_sound(self):
        print("Quack quack!")

# Usage
bird = Bird()
bird.make_sound()  # Output: Chirp chirp!
bird.fly()         # Output: I can fly!