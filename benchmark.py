from json import loads as json_loads, dumps as json_dumps
from timeit import timeit

try:
    from ujson import loads as ujson_loads, dumps as ujson_dumps
except ImportError:
    print("ujson not installed.")
    exit(-1)

try:
    from simplejson import loads as simplejson_loads, dumps as simplejson_dumps
except ImportError:
    print("simplejson not installed.")
    exit(-1)

if __name__ == '__main__':
    TEST_COUNT = 1000
    test_json = {" large": [TEST_COUNT],
                 "middle": [TEST_COUNT * 10],
                 " small": [TEST_COUNT * 100],
                 }

    for name in test_json:
        with open(name.strip() + ".json", encoding="utf-8") as f:
            large_str = f.read()
            large_obj = json_loads(large_str)
            test_json[name].extend([large_str, large_obj])

    for name, (test_count, json_str, json_obj) in test_json.items():
        print("\n---------------------------------------\n", name)
        print("\t\t\t\t", "loads", "\t", "dumps")
        for m, loads_func, dumps_func in [("ujson", ujson_loads, ujson_dumps),
                                          ("simplejson", simplejson_loads, simplejson_dumps),
                                          ("json", json_loads, json_dumps),
                                          ]:
            loads_time = round(timeit(lambda: loads_func(json_str), number=test_count), 3)
            dumps_time = round(timeit(lambda: dumps_func(json_obj), number=test_count), 3)
            print("%12s" % m, "\t", loads_time, "\t", dumps_time)
