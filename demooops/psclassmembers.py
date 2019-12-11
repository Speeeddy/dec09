"""demo for the class members"""


class MaxConnectionError(Exception):
    """custom/user defined exception """


"""https://codeshare.io/2jVjpB"""


class Connections:
    max_connections = 5  # class variables
    connection_counter = 0

    def __init__(self, connection_id):
        Connections.connection_counter += 1
        Connections.check_4_limit()
        self.connection_id = connection_id  # instance variable

    @classmethod
    def check_4_limit(cls):
        if cls.connection_counter > cls.max_connections:
            raise MaxConnectionError('reached maximum limit')

    def __str__(self):
        return f'[{self.__class__.__name__} connection id={self.connection_id}]'



if __name__ == '__main__':
    try:
        for c_id in range(11, 17):
            c = Connections(c_id)
            print(c)
            # 1/0
    except MaxConnectionError as err:
        print(err)
    except:   # generic
        from sys import exc_info
        print(exc_info())
