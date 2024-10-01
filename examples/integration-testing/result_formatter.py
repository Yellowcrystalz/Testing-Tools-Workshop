# result_formatter.py

class ResultFormatter:
    def format_result(self, operation, result):
        return f"The result of {operation} is: {result}"

    def format_error(self, error_message):
        return f"Error: {error_message}"
