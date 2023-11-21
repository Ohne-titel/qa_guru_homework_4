import random


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    l = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
         random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
         random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
         random.randint(1, 100)]
    l = sorted(l)
    assert len(l) == 10
    assert l[0] < l[-1]
