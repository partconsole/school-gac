import numpy


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.fullness = 8
        self.happiness = 8
        self.cleanliness = 8
        self.alive = True
        self.stage = "egg"
        self.progress = 1

    def feed(self):
        if self.fullness < 10:
            self.fullness += 3
            if self.fullness > 10:
                self.fullness = 10
        else:
            if self.cleanliness > 1:
                self.cleanliness -= 2

    def play(self):
        if self.happiness < 10:
            self.happiness += 3
            if self.happiness > 10:
                self.happiness = 10
        else:
            self.fullness -= 2
            if self.fullness < 1:
                self.fullness = 1

    def bathe(self):
        if self.cleanliness < 10:
            self.cleanliness += 3
            if self.cleanliness > 10:
                self.cleanliness = 10
        else:
            self.happiness -= 2
            if self.happiness < 1:
                self.happiness = 1

    def age_up(self):
        stages = ["egg", "baby", "child", "adult"]
        current_stage_index = stages.index(self.stage)
        if current_stage_index < len(stages) - 1:
            self.stage = stages[current_stage_index + 1]
            self.progress = 1

    def status(self):
        if self.fullness > 5 and self.happiness > 5 and self.cleanliness > 5:
            return "fine"
        elif self.fullness <= 1 or self.happiness <= 1 or self.cleanliness <= 1:
            self.alive = False
            return "dead"
        else:
            return "distress"

    def time_step(self):
        attributes = ["fullness", "happiness", "cleanliness"]
        chosen_attribute = numpy.random.choice(attributes)

        # Decrease the chosen attribute by 1
        if chosen_attribute == "fullness":
            self.fullness = max(1, self.fullness - 1)
        elif chosen_attribute == "happiness":
            self.happiness = max(1, self.happiness - 1)
        elif chosen_attribute == "cleanliness":
            self.cleanliness = max(1, self.cleanliness - 1)

        # Increase progress by 1
        self.progress += 1

        # Check if it's time to age up
        if self.progress == 20:
            self.age_up()

        # Get the status after the time step
        return self.status()


def main():
    # Test 1
    goku = Tamagotchi("Goku")
    goku.bathe()
    goku.play()
    goku.feed()
    assert goku.fullness == 10 and goku.cleanliness == 10 and goku.happiness == 10

    # Test 2
    gohan = Tamagotchi("Gohan")
    gohan.bathe()
    gohan.play()
    gohan.feed()
    gohan.feed()
    gohan.bathe()
    gohan.play()
    assert gohan.fullness == 8 and gohan.cleanliness == 10 and gohan.happiness == 10

    # Test 3
    assert goku.stage == "egg"
    goku.age_up()
    assert goku.stage == "baby"
    goku.age_up()
    assert goku.stage == "child"
    goku.age_up()
    assert goku.stage == "adult"
    goku.age_up()
    assert goku.stage == "adult"

    # Test 4
    vegeta = Tamagotchi("Vegeta")
    vegeta.fullness = 6
    vegeta.happiness = 6
    vegeta.cleanliness = 6
    assert vegeta.status() == "fine"

    vegeta.cleanliness = 3
    assert vegeta.status() == "distress"

    vegeta.fullness = 1
    assert vegeta.status() == "dead"


if __name__ == "__main__":
    main()
