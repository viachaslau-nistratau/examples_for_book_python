import mysql.connector


class ConnectionError(Exception):
    pass

class CredentialError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDatabase:

    def __init__(self, config: dict) -> None:
        """
        позволяет выполнить настройки перед тем, как with начнет выполнение
        :param config:
        """
        self.configuration = config

    # код диспетчера контекста
    def __enter(self) -> 'cursor':
        """
        выполняется когда выражение with запустится
        :return:
        """
        """ конструкция защищает код подключения к БД """
        try:
            self.conn = mysql.connector.connect(**self.configaration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            """ возбуждение собственного исключения"""
            raise ConnectionError(err)
            """
            возбуждается исключение при попытке передать неправильное имя пользователя
            или пароль базе данных
            """
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        """
        гарантированно выполняется когда блок кода with завершается
        :param exc_type:
        :param exc_value:
        :param exc_trace:
        :return:
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        """ 
        повторно возбудит любое другое исключение,
        которое может возникнуть
        """
        elif exc_type:
            raise exc_type(exc_value)