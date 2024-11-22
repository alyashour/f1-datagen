import time

from data_generator import generate_all
from data_writer.db import main as push_to_db

def count_rows(data):
    total_rows = 0
    tables = {}
    for table_name in data:
        table = data[table_name]
        row_count = 0
        for row in table:
            row_count += 1
        tables[table_name] = row_count
        total_rows += row_count
    return total_rows, tables

def main():
    gen_start_time = time.perf_counter()
    data = generate_all()
    gen_end_time = time.perf_counter()


    push_start_time = time.perf_counter()
    push_to_db(data)
    push_end_time = time.perf_counter()

    print()
    print('| Done! |')

    # calc stats
    total_rows, tables = count_rows(data)
    print('STATS:')
    print('Generated and saved ', total_rows, 'rows in', round(gen_end_time + push_end_time - gen_start_time - push_start_time, 3), 'seconds')

    for table_name in tables.keys():
        row_count = tables[table_name]
        print(f'- {table_name}: {row_count} rows')


if __name__ == '__main__':
    main()