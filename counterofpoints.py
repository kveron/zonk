class CounterOfPoints:
    @staticmethod
    def max_points(values):
        numbers = [0, 0, 0, 0, 0, 0]
        count = 0
        value = 0
        sum = 1
        for i in values:
            if i == 1:
                numbers[0] += 1
            elif i == 2:
                numbers[1] += 1
            elif i == 3:
                numbers[2] += 1
            elif i == 4:
                numbers[3] += 1
            elif i == 5:
                numbers[4] += 1
            elif i == 6:
                numbers[5] += 1
        for i in range(0, 6):
            sum = numbers[i] * sum
            if numbers[i] >= 3 and i != 0:
                value = (i + 1) * 100 + ((numbers[i] - 3) * (i + 1) * 100) + value
            if numbers[i] == 2:
                count += 1
            if count == 3:
                value = 750
        if numbers[0] >= 3:
            value = 1000 + (numbers[0] - 3) * 1000 + value
        if sum == 1:
            value = 1500
        if count != 3 and sum != 1 and numbers[0] < 3:
            value = value + numbers[0] * 100
        if count != 3 and sum != 1 and numbers[4] < 3:
            value = value + numbers[4] * 50
        return value
