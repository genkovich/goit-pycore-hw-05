from collections import defaultdict


def main():
    user_input = input("Enter a path to log file: ").strip().lower()

    try:
        path, *args = user_input.split()
        logs = load_logs(path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        error_lvl = None
        if args:
            error_lvl = args[0].upper()
            acceptable_levels = ['INFO', 'WARNING', 'ERROR', 'CRITICAL']
            if error_lvl not in acceptable_levels:
                print('Acceptable levels are INFO, WARNING, ERROR, CRITICAL')
                raise ValueError('Invalid error level')

        if error_lvl:
            logs = filter_logs_by_level(logs, error_lvl)
            print(f'\n\nLogs with level {error_lvl}:')
            for log in logs:
                print(f'{log["date"]} {log["time"]} {log["error_lvl"]} {log["message"]}')

    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Invalid input')
    except Exception as e:
        print(e)


def parse_log_line(line) -> dict:
    date, time, error_lvl, message = line.split(' ', 3)
    return {
        'date': date,
        'time': time,
        'error_lvl': error_lvl,
        'message': message.strip()
    }


def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return [parse_log_line(line) for line in file]


def count_logs_by_level(logs: list) -> dict:
    levels = defaultdict(int)
    for log in logs:
        levels[log['error_lvl']] += 1
    return levels


def display_log_counts(counts: dict):
    for level, count in counts.items():
        print(f'{level}: {count}')


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['error_lvl'] == level]


if __name__ == '__main__':
    main()
