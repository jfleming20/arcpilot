from payment_methods.domain.command.select_payment_method import SelectPaymentMethodCommand, select_payment_method_command_handler
class App:
    command_handlers = {
        SelectPaymentMethodCommand: select_payment_method_command_handler
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
