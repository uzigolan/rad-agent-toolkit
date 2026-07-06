# secflow CLI reference (harvested `?` help)

Captured live from lab-sf1p (SF-1p-187 (SecFlow-1p, Sw 6.5.0.35) - pilot lab unit, safe for guarded write tests) on 2026-07-06 by scripts/harvest_cli.py.
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Entries
marked *(not entered)* are parameterized contexts — their inner structure
is in command-tree-secflow.md; use cli_help with a real index for
inner argument syntax.

## <root>

Level help (`?`):
```text
admin                          + Adminstrative commands
      configure                      + Configure device
      file                           + File commands
      logon                          - Logon as Debug user
      on-configuration-error         - Behavior for configuration error
      quick-setup                    + Quick Setup

Global commands:
      copy                           - Copy file
      echo                           - Displays a line of text (command) on the 
                                       screen
      exec                           - Execute script of CLI commands
      exit                           - Returns to the next higher command level 
                                       (context)
      help                           - Displays information regarding commands 
                                       in the current level
      history                        - Displays the history of commands issued 
                                       since the last restart
      info                           - Displays the current device configuration
      level-info                     - Displays the current device configuration
                                        - commands from the current level only
      logout                         - Logs the device off
      ping                           - Ping
 [no] popup-suspend                  - Suspends popup messages
      save                           - Save current settings
 [no] schedule                       - Schedule a command to run in a future 
                                       time
      telnet                         - Open telnet client session
      trace-route                    - Traceroute
      tree                           - Displays the command levels from the 
                                       current context downwards
```

## file

Level help (`?`):
```text
delete                         - Delete file
      delete-from-folder             - Deletes a user file
      delete-user                    - Deletes a file from the device
 [no] description                    - Description of the file
      dir                            - Display file directory
 [no] flash-enable                   - Enable flash (SD card)
      flash-temporarily-enable       - Enable flash until inactivity time is 
                                       reached
      folder-dir                     - List of all user files
      media-dir                      - Execute media dir
      user-file-dir                  - List of all user files in the device

 show banner-text                    - Display banner
 show configuration-files            - Displays configuration files properties
 show copy                           - Display Copy progress
 show factory-default-config         - Display factory-default-config
 show file-details                   - Displays the details of the file
 show file-transfer-status           - Display Copy progress
 show flash-status
 show rollback-config                - Display rollback-config
 show schedule-log                   - Display schedule-log  
 show startup-config                 - Display startup-config
 show sw-pack                        - Display SW packs
 show user-default-config            - Display user-default-config
 show user-dir
```

### delete
```text
<sw-pack-2>          : 
 <startup-config>     : 
 <zero-touch-config-xm: 
 <restore-point-config: 
 <user-script>        : 
 <script-result>      : 


SF-1p-187>file# delete
```

### delete-from-folder
```text
<filename>           : [string]


SF-1p-187>file# delete-from-folder
```

### delete-user
```text
<filename>           : [string]


SF-1p-187>file# delete-user
```

### description
```text
<file-name>          : The name of the file [1..37 chars]


SF-1p-187>file# description
```

### dir
```text
<CR>

SF-1p-187>file# dir
```

### flash-enable
```text
<CR>

SF-1p-187>file# flash-enable
```

### flash-temporarily-enable
```text
inactivity-timeout

SF-1p-187>file# flash-temporarily-enable
```

### folder-dir
```text
<CR>

SF-1p-187>file# folder-dir
```

### media-dir
```text
media

SF-1p-187>file# media-dir
```

### user-file-dir
```text
<CR>

SF-1p-187>file# user-file-dir
```

### show banner-text
```text
<CR>

SF-1p-187>file# show banner-text
```

### show configuration-files
```text
<CR>

SF-1p-187>file# show configuration-files
```

### show copy
```text
<CR>
 <summary>            : 


SF-1p-187>file# show copy
```

### show factory-default-config
```text
<CR>

SF-1p-187>file# show factory-default-config
```

### show file-details
```text
<filename>           : [string]


SF-1p-187>file# show file-details
```

### show file-transfer-status
```text
<CR>

SF-1p-187>file# show file-transfer-status
```

### show flash-status
```text
<CR>

SF-1p-187>file# show flash-status
```

### show rollback-config
```text
<CR>

SF-1p-187>file# show rollback-config
```

### show schedule-log
```text
<CR>

SF-1p-187>file# show schedule-log
```

### show startup-config
```text
<CR>

SF-1p-187>file# show startup-config
```

### show sw-pack
```text
<CR>

SF-1p-187>file# show sw-pack
```

### show user-default-config
```text
<CR>

SF-1p-187>file# show user-default-config
```

### show user-dir
```text
<filename>           : [string]


SF-1p-187>file# show user-dir
```
