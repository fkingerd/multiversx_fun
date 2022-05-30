import random
import linecache

def file_checker(initial_erds, output_erds):
    row_number = 0
    with open(initial_erds, "r") as input:
        with open(output_erds,"w") as output:
            for line in input:
                if line[:3] == 'erd':
                    output.write(line)
                    row_number += 1
    return row_number
    

def random_picker(erds_file, total_rows, winners_count):
    idxs = random.sample(range(total_rows), winners_count)
    return [linecache.getline(erds_file, i) for i in idxs]


def main(initial_erds, checked_erds, how_many_winners, final_file):
    total_rows = file_checker(initial_erds, checked_erds)
    winner_erds_list_uncut = random_picker(checked_erds, total_rows, how_many_winners)
    
    with open(final_file, "w+") as result_file:
        for erd in winner_erds_list_uncut:
            result_file.write(f'{erd[:-2]}\n')
        
        return result_file

print(main("erds_to_pick_from", "ok_erds", 1055, "winners_erds"))
