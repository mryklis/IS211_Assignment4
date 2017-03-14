from timeit import default_timer as timer
import numpy.random as nprnd

def sequential_search(a_list, item):
    start = timer()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
    else:
        pos = pos + 1
    end = timer()
    return found, (end - start)

def ordered_sequential_search(a_list, item):
    start = timer()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
    else:
        if a_list[pos] > item:
            stop = True
        else:
            pos = pos + 1
        end = timer()
        return found, (end - start)

def binary_search_iterative(a_list, item):
    start = timer()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
    if a_list[midpoint] == item:
        found = True
    else:
        if item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    end = timer()
    return found, (end - start)


def binary_search_recursive(a_list, item):
    start = timer()
    if len(a_list) == 0:
        end = timer()
        return False, (end - start)
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end = (end - start)
        return True, end
    else:
        if item < a_list[midpoint]:
            end = timer()
            return binary_search_recursive(a_list[:midpoint], item), (end - start)
        else:
            end = timer()
            return binary_search_recursive(a_list[midpoint + 1:], item), (end - start)



if __name__ == '__main__':

    l1 = nprnd.randint(10000, size=10000)
    l2 = nprnd.randint(500, size=500)
    l3 = nprnd.randint(1000, size=1000)

    i = 0
    sum_g = 0
    sum_h = 0
    sum_i = 0
    while i < 100:
        g1, g2 = binary_search_recursive(l1, -1)
        sum_g += g2
        h1, h2 = binary_search_recursive(l2, -1)
        sum_h += h2
        i1, i2 = binary_search_recursive(l3, -1)
        sum_i += i2
        i += 1

    print 'Binary Recursive Search took {} seconds to run, on average'.format(sum_g/100)
    print 'Binary Recursive Search took {} seconds to run, on average'.format(sum_h/100)
    print 'Binary Recursive Search took {} seconds to run, on average'.format(sum_i/100)


    l1.sort()
    l2.sort()
    l3.sort()

    i = 0
    sum_s = 0
    sum_t = 0
    sum_u = 0
    while i < 100:
        s1, s2 = sequential_search(l1, -1)
        sum_s += s2
        t1, t2 = sequential_search(l2, -1)
        sum_t += t2
        u1, u2 = squential_search(l3, -1)
        sum_u += u2
        i += 1

    print 'Sequential Search took {} seconds to run, on average'.format(sum_s/100)
    print 'Sequential Search took {} seconds to run, on average'.format(sum_t/100)
    print 'Sequential Search took {} seconds to run, on average'.format(sum_u/100)

    i = 0
    sum_a = 0
    sum_b = 0
    sum_c = 0
    while i < 100:
        a1, a2 = ordered_sequential_search(l1, -1)
        sum_a += a2
        b1, b2 = ordered_sequential_search(l2, -1)
        sum_b += b2
        c1, c2 = ordered_sequential_search(l3, -1)
        sum_c += c2
        i += 1

    print 'Sequential Search took {} seconds to run, on average'.format(sum_a/100)
    print 'Ordered Sequential Search took {} seconds to run, on average'.format(sum_b/100)
    print 'Ordered Sequential Search took {} seconds to run, on average'.format(sum_c/100)

    i = 0
    sum_d = 0
    sum_e = 0
    sum_f = 0
    while i < 100:
        d1, d2 = binary_search_iterative(l1, -1)
        sum_d += d2
        e1, e2 = binary_search_iterative(l2, -1)
        sum_e += e2
        f1, f2 = binary_search_iterative(l3, -1)
        sum_f += f2
        i += 1

    print 'Binary Iterative Search took {} seconds to run, on average'.format(sum_d/100)
    print 'Binary Iterative Search took {} seconds to run, on average'.format(sum_e/100)
    print 'Binary Iterative Search took {} seconds to run, on average'.format(sum_f/100)