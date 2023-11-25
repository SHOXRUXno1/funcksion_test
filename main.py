import unittest


def kattason(x, y, z):
    return max(x, y, z)


def text_list(*args):
    title_list = []
    for text in args:
        title_list.append(text.title())
    return title_list


class Sontest(unittest.TestCase):
    def sonmax(self):
        son = kattason(3, 4, 5)
        self.assertAlmostEqual(son, 1, 3)


class Matntest(unittest.TestCase):
    def tittle(self):
        matn = text_list("jonibek")
        self.assertEqual(matn, matn, "shox")
        print(matn)


unittest.main()
