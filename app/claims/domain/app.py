from claims.domain.command.close_claim import CloseClaimCommand, close_claim_command_handler
from claims.domain.command.assign_claim_to_adjuster import AssignClaimToAdjusterCommand, assign_claim_to_adjuster_command_handler
class App:
    command_handlers = {
        CloseClaimCommand: close_claim_command_handler,
        AssignClaimToAdjusterCommand: assign_claim_to_adjuster_command_handler
    }

    query_handlers = {
    }

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)

    def execute_query(self, query):
        handler = self.query_handlers[type(query)]
        return handler(query)


app = App()
