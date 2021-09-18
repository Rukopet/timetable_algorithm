__doc__ = """
    timetable_genetic_algorithm can launch like script
    
    ~
    if no arguments pass in launch, script start server
        example:
            python3 -m timetable_genetic_algorithm
    
    ~
    if need start timetable_genetic_algorithm like console script, need pass two arguments
        default filename out_timetable.xlsx
        $arg1 => path to folder with json files
        
        $arg2 => [path + filename] + .xlsx path to save out
        default filename ./out_timetable.xlsx

        
        example:
            python3 -m timetable_genetic_algorithm "/foo/bar/folder_with_json" "../file_out"
          """
