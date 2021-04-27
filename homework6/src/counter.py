"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(some_cls):
    class InstCounter(some_cls):
        inst_counter = 0

        @classmethod
        def init_counter(cls):
            if "inst_counter" not in cls.__dict__:
                cls.inst_counter = 0

        def __init__(self, *args, **kwargs):
            self.init_counter()
            super().__init__(*args, **kwargs)
            self.__class__.inst_counter += 1

        @classmethod
        def get_created_instances(cls):
            cls.init_counter()
            return cls.inst_counter

        @classmethod
        def reset_instances_counter(cls):
            cls.init_counter()
            total_objects = cls.inst_counter
            cls.inst_counter = 0
            return total_objects

    return InstCounter


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, *_ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(User.reset_instances_counter())  # 3
    print(User.get_created_instances())
