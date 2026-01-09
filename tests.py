import solution


def test_get_ways():
    G = solution.Graph(directed=False)
    G.add_edge(("A", "B"))
    G.add_edge(("B", "C"))
    G.add_edge(("A", "C"))
    G.add_edge(("C", "D"))

    assert(solution.get_ways(G, "A", "D") == [['A', 'B', 'C', 'D'], ['A', 'C', 'D']])
    print("Все маршруты успешно найдены")


def test_get_zhegakin_pol():
    assert(solution.get_zhegalkin_polynomial([1,1,1,1,0,1,0,0], ["x", "y", "z"]) == "1 + x + xz + xyz")
    print("Тест ПЖ пройден")


def test_func_count():
    assert(solution.get_func_count("T0", 3) == 128)
    assert(solution.get_func_count("T1", 4) == 32768)
    assert(solution.get_func_count("S", 3) == 16)
    assert(solution.get_func_count("L", 4) == 32)
    assert(solution.get_func_count("M", 3) == 20)
    assert (solution.get_func_count("M", 5) == 7581)
    print("Тест функции нахождения количества функций пройден")

def test_get_shortest_ham_cycle():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    assert(solution.get_shortest_ham_cycle(graph) == 80)
    print("Тест нахождения кратчайшего ГЦ пройден")


if __name__ == "__main__":
    test_get_ways()
    test_get_zhegakin_pol()
    test_func_count()
    test_get_shortest_ham_cycle()
