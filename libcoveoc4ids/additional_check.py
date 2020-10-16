class AdditionalCheck(object):
    def process(self, data, flat_data):
        """Should Return a dictionary of the output or True if check passed

        Use self.result() to generate the result dictionary.
        """
        raise NotImplementedError

    def result(self, message_id, message, paths):
        """Create a results dictionary to be returned by process function"""
        return {"check_id": message_id, "message": message, "paths": paths}
