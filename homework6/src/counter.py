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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            InstCounter.inst_counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.inst_counter

        @classmethod
        def reset_instances_counter(cls):
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
