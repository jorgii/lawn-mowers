def parse_file(file_path):
    result = {}
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    result['grid'] = [int(i) for i in lines[0].split()]
    result['lawn_mowers'] = []

    lm_data_start = 1
    lm_data_end = 3
    has_lawn_mowers = True
    while has_lawn_mowers:
        lawn_mower = {}
        try:
            lawn_mower_lines = lines[lm_data_start:lm_data_end]
            lawn_mower['position'] = [
                int(i) for i in lawn_mower_lines[0].split()[0:2]]
            lawn_mower['orientation'] = lawn_mower_lines[0].split()[2]
            lawn_mower['actions'] = list(lawn_mower_lines[1])
            result['lawn_mowers'].append(lawn_mower)
            lm_data_start += 2
            lm_data_end += 2
        except IndexError:
            has_lawn_mowers = False
    return result
