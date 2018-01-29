from module import Module
from extra_functions.load import loadModule

class PayloadModule(Module):
    def __init__(self, opt, info = {}):
        opt["payload"] = ["""If this option is empty open a local root shell\n
                Use -e to encode the shellcode and avoid NULL characters""", "", False]
        super(PayloadModule, self).__init__(opt,info)
        self.payload = None
    
    def put(self, args):
        if args[0] == "payload":
            self.options["payload"][1] = args[1]
            self.payload = loadModule(args[1], "support/payloads")
            if self.payload:
                self.options["encode"] = ["Host to connect the shell", False, False]
                if "-e" in args:
                    self.print_info("Encode enable")
                    self.options["encode"][1] = True
                    self.payload.encode = True
                self.print_info(self.payload.get_info_metasploit())
                self.options["lhost"] = ["Host to connect the shell", "", True]
                self.options["lport"] = ["Port to connect the shell", "", True]
            else:
                self.print_error("Wrong payload")
        else:
            super(PayloadModule, self).put(args)