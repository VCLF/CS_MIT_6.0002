from ps1a import (load_cows, greedy_cow_transport,
                  brute_force_cow_transport,
                  compare_cow_transport_algorithms)

cows_names = load_cows("ps1_cow_data_2.txt")
print(cows_names)

#travel = greedy_cow_transport(cows_names, 10)
#print(travel)

#(travel, names) = brute_force_cow_transport(cows_names,11)
#print(travel)
#print(names)
compare_cow_transport_algorithms()
