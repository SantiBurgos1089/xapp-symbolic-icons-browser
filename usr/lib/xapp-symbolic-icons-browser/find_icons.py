#!/usr/bin/python3

import json
import pathlib

def find_xsi_icons(directory, pattern_data = "xsi-*", test=False):
    base_directory = pathlib.Path(directory)
    result_info = []

    for id_num, file in enumerate(base_directory.rglob(pattern_data), start=1):
        if file.is_file():
            result_info.append({
                "ID": id_num,
                "IconName": file.stem,
                "FileName": file.name,
                "FilePath": str(file)
            })

            # Test: get only the first 50 elements if test=True
            if test is True:
                if id_num >= 50:
                    break

    return result_info

## Test section: print the information in console
## Comment in case you don't need to show information
#final_data_info = find_icons("/usr/share/icons", "xsi-*", False)
#json_info = json.dumps(final_data_info, indent=4)
#print(json_info)

