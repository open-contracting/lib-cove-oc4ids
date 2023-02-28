class AdditionalCheck:
    def process(self, data, flat_data):
        """Should Return a dictionary of the output or True if check passed

        Use self.result() to generate the result dictionary.
        """
        raise NotImplementedError

    def result(self, check_id, message, paths):
        """Create a results dictionary to be returned by process function"""
        return {"check_id": check_id, "message": message, "paths": paths}


class ConformanceCheck(AdditionalCheck):
    def result(self, check_id, message, path_values):
        """Create a results dictionary to be returned by process function
        path_values is expected to be a list of { "path": path, "value": value }
        Where path is /the/path/in/the/data and value is the erroneous value from the data
        """
        return {"check_id": check_id, "message":  message, "path_values": path_values}
