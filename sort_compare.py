from timeit import default_timer as timer
import numpy.random as nprnd

def insertion_sort(a_list):
    start = timer()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
    position = index
    while position > 0 and a_list[position - 1] > current_value:
        a_list[position] = a_list[position - 1]
    position = position - 1
    a_list[position] = current_value
    end = timer()
    return a_list, (end - start)

def shell_sort(a_list):
    start = timer()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
    print("After increments of size", sublist_count, "The list is",
          a_list)
    sublist_count = sublist_count // 2
    return a_list, (end - start)

def gap_insertion_sort(a_list, start, gap):
    for i in range(int(start + gap), int(len(a_list)), int(gap)):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
    return a_list

def python_sort(a_list):
    start = timer()
    a_list.sort()
    end = timer()
    return a_list, (end - start)


if __name__ == '__main__':
    l1 = nprnd.randint(10000, size=10000)
    l2 = nprnd.randint(500, size=500)
    l3 = nprnd.randint(1000, size=1000)

    i = 0
    sum_g = 0
    sum_h = 0
    sum_i = 0
    while i < 100:
        g1, g2 = python_sort(l1)
        sum_g += g2
        h1, h2 = python_sort(l2)
        sum_h += h2
        i1, i2 = python_sort(l3)
        sum_i += i2
        i += 1

    print 'The Python sort took {} seconds to run, on average'.format(sum_g / 100)
    print 'The Python sort took {} seconds to run, on average'.format(sum_h / 100)
    print 'The Python sort took {} seconds to run, on average'.format(sum_i / 100)

    i = 0
    sum_a = 0
    sum_b = 0
    sum_c = 0
    while i < 100:
        a1, a2 = insertion_sort(l1)
        sum_a += a2
        b1, b2 = insertion_sort(l2)
        sum_b += b2
        c1, c2 = insertion_sort(l3)
        sum_c += c2
        i += 1

    print 'The Insertion sort took {} seconds to run, on average'.format(sum_a / 100)
    print 'The Insertion sort took {} seconds to run, on average'.format(sum_b / 100)
    print 'The Insertion sort took {} seconds to run, on average'.format(sum_c / 100)

    i = 0
    sum_d = 0
    sum_e = 0
    sum_f = 0
    while i < 100:
        d1, d2 = shell_sort(l1)
        sum_d += d2
        e1, e2 = shell_sort(l2)
        sum_e += e2
        f1, f2 = shell_sort(l3)
        sum_f += f2
        i += 1

    print 'The Shell sort took {} seconds to run, on average'.format(sum_d / 100)
    print 'The Shell sort took {} seconds to run, on average'.format(sum_e / 100)
    print 'The Shell sort took {} seconds to run, on average'.format(sum_f / 100)