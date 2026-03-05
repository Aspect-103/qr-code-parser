import config.ConfigManager as ConfigManager

# Strip comma from end if necessary
def strip_commas(full_str:str) -> str:
    while full_str[-1] == ",":
        full_str = full_str[:-1]
    return full_str

# Get file paths from config
def get_data_file_path():
    return ConfigManager.get_config()['paths']['qr_strings']

def write_full_str(path:str, full_str:str):
    with open(path, 'a') as file:
        file.write(strip_commas(full_str) + "\n")

def replace_last_entry(new_str:str):
    paths = get_data_file_path()
    print(paths)
    for path in paths:
        print("Now replacing a string at " + path)
        with open(path, 'r+') as file:
            lines = file.readlines()
            print("oldlines: " + str(lines))
            # Make sure not to delete the headers
            if len(lines) > 1:
                lines = lines[:-1]
            file.seek(0)
            file.truncate()
            print("newlines: " + str(lines))
            for line in lines:
                file.write(line)
    # 0: qrStrings, 1: eventList, 2: setupList
    write_full_str(paths[0], new_str)

def get_last_full_string():
    path = get_data_file_path()
    with open(path, 'r+') as file:
        lines = file.readlines()
        if len(lines) < 2:
            return ""
        return lines[len(lines)-1]
    

def get_team_number(full_str:str) -> str:
    return full_str.split(",")[1]

def get_match_number(full_str:str) -> str:
    return full_str.split(",")[2]

# Make sure qr string is a csv value with correct number of fields for 2026 (34 fields: Setup + Auton + Teleop + Endgame + Climb)
# 2026 format: Scouter, Team, Match, Alliance, NoShow, Preload, Fellover + A-Collecting through A-ClimbLocation (8) + T- (8) + E- (8) + C- (3) = 34 total
def is_correct_format(full_str:str) -> bool:
    values = full_str.split(',')
    # Check for 34 fields AND contains the Scouter name in position 0 (non-numeric typically)
    # Also check that it has the climb fields at the end (Park, Hang, Barge which are Y/N or S/D/N)
    if len(values) != 34:
        return False
    # Validate by checking expected field positions and patterns
    try:
        # Team number should be numeric (position 1)
        int(values[1])
        # Match number should be numeric (position 2)
        int(values[2])
        # Basic validation passed
        return True
    except (ValueError, IndexError):
        return False